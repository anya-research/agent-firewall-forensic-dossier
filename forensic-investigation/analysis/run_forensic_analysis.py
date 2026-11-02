import os
import sys
import ast
import json
import csv
import re
import hashlib
import pathlib
from collections import defaultdict

root_a = pathlib.Path("forensic-investigation/evidence/project-a/repo")
root_b = pathlib.Path("forensic-investigation/evidence/project-b/agent_firewall1-0.1.0")

def get_files(root, exclude_egg=True):
    res = {}
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root))
        if any(part.startswith(".") for part in p.parts):
            continue
        if exclude_egg and ".egg-info" in rel:
            continue
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
            raw = p.read_bytes()
        except Exception:
            continue
        res[rel] = {
            "path": p,
            "rel": rel,
            "raw": raw,
            "content": content,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "lines": content.splitlines(),
            "is_python": p.suffix == ".py"
        }
    return res

files_a = get_files(root_a)
files_b = get_files(root_b)

print(f"Total analyzed files: Project A = {len(files_a)}, Project B = {len(files_b)}")

# 1. SHA256 Exact Matches
exact_matches = []
for rel_b, data_b in files_b.items():
    for rel_a, data_a in files_a.items():
        if data_b["sha256"] == data_a["sha256"]:
            exact_matches.append((rel_a, rel_b, data_b["sha256"]))

print(f"Exact file hash matches: {len(exact_matches)}")
for m in exact_matches:
    print(f"  Match: {m[0]} == {m[1]} ({m[2]})")

# 2. Python AST extraction
def extract_ast_items(content):
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return None
    
    classes = {}
    functions = {}
    imports = []
    constants = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            bases = [ast.unparse(b) for b in node.bases]
            classes[node.name] = {
                "name": node.name,
                "bases": bases,
                "methods": methods,
                "lineno": node.lineno
            }
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Check if top-level or method
            args = [a.arg for a in node.args.args]
            functions[node.name] = {
                "name": node.name,
                "args": args,
                "is_async": isinstance(node, ast.AsyncFunctionDef),
                "lineno": node.lineno
            }
        elif isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            for n in node.names:
                imports.append(f"{mod}.{n.name}")
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float, str)):
                constants.append(node.value)

    return {
        "tree": tree,
        "classes": classes,
        "functions": functions,
        "imports": imports,
        "constants": constants
    }

py_a = {rel: extract_ast_items(d["content"]) for rel, d in files_a.items() if d["is_python"]}
py_b = {rel: extract_ast_items(d["content"]) for rel, d in files_b.items() if d["is_python"]}

# Filter out None asts
py_a = {k: v for k, v in py_a.items() if v is not None}
py_b = {k: v for k, v in py_b.items() if v is not None}

all_classes_a = {c: rel for rel, data in py_a.items() for c in data["classes"]}
all_classes_b = {c: rel for rel, data in py_b.items() for c in data["classes"]}
shared_classes = set(all_classes_a.keys()) & set(all_classes_b.keys())
print(f"Total unique classes: A={len(all_classes_a)}, B={len(all_classes_b)}, Shared={len(shared_classes)}")
for sc in shared_classes:
    print(f"  Shared class: {sc} in A({all_classes_a[sc]}) and B({all_classes_b[sc]})")

all_funcs_a = {f: rel for rel, data in py_a.items() for f in data["functions"]}
all_funcs_b = {f: rel for rel, data in py_b.items() for f in data["functions"]}
shared_funcs = set(all_funcs_a.keys()) & set(all_funcs_b.keys())
print(f"Total unique functions/methods: A={len(all_funcs_a)}, B={len(all_funcs_b)}, Shared={len(shared_funcs)}")
for sf in sorted(shared_funcs):
    print(f"  Shared func: {sf} in A({all_funcs_a[sf]}) and B({all_funcs_b[sf]})")

# 3. Line by line matching
def normalize_line(line):
    line = re.sub(r"#.*$", "", line)
    line = line.strip()
    return line

lines_a_set = defaultdict(set)
for rel, d in files_a.items():
    if not d["is_python"]:
        continue
    for idx, l in enumerate(d["lines"]):
        norm = normalize_line(l)
        if len(norm) >= 20: # Non-trivial lines
            lines_a_set[norm].add((rel, idx + 1))

exact_line_matches = []
for rel, d in files_b.items():
    if not d["is_python"]:
        continue
    for idx, l in enumerate(d["lines"]):
        norm = normalize_line(l)
        if len(norm) >= 20 and norm in lines_a_set:
            exact_line_matches.append({
                "line": norm,
                "file_b": rel,
                "line_b": idx + 1,
                "file_a_matches": list(lines_a_set[norm])
            })

print(f"Non-trivial normalized line matches (len >= 20): {len(exact_line_matches)}")
for elm in exact_line_matches[:25]:
    print(f"  B: {elm['file_b']}:{elm['line_b']} -> '{elm['line']}' matches in A: {elm['file_a_matches'][0]}")

# 4. Token 4-gram / 6-gram similarity
def tokenize(text):
    return re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", text)

def ngrams(tokens, n=4):
    return set(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

tokens_a = {rel: tokenize(d["content"]) for rel, d in files_a.items()}
tokens_b = {rel: tokenize(d["content"]) for rel, d in files_b.items()}

pair_similarities = []
for rel_b, tok_b in tokens_b.items():
    if len(tok_b) < 10:
        continue
    set_b = set(tok_b)
    ng_b_4 = ngrams(tok_b, 4)
    for rel_a, tok_a in tokens_a.items():
        if len(tok_a) < 10:
            continue
        set_a = set(tok_a)
        jaccard_tokens = len(set_a & set_b) / len(set_a | set_b) if (set_a | set_b) else 0
        ng_a_4 = ngrams(tok_a, 4)
        jaccard_4gram = len(ng_a_4 & ng_b_4) / len(ng_a_4 | ng_b_4) if (ng_a_4 | ng_b_4) else 0
        if jaccard_tokens > 0.15 or jaccard_4gram > 0.05:
            pair_similarities.append({
                "file_a": rel_a,
                "file_b": rel_b,
                "jaccard_tokens": jaccard_tokens,
                "jaccard_4gram": jaccard_4gram,
                "common_4grams": len(ng_a_4 & ng_b_4)
            })

pair_similarities.sort(key=lambda x: x["jaccard_4gram"], reverse=True)
print(f"Top 10 file pairs by 4-gram similarity:")
for ps in pair_similarities[:10]:
    print(f"  A: {ps['file_a']} <-> B: {ps['file_b']} | 4-gram Jaccard: {ps['jaccard_4gram']:.4f}, Token Jaccard: {ps['jaccard_tokens']:.4f}, Shared 4-grams: {ps['common_4grams']}")

