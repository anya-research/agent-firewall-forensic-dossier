# SentinelAI: Complete Slide-by-Slide Presentation Extraction & Full Transcript

> **Source File:** `SentinelAI_Final_Presentation (1).pptx`  
> **Extracted To Folder:** `sentinelai_presentation_extracted/`  
> **Extracted File:** `SENTINELAI_PRESENTATION_COMPLETE_EXTRACTION.md`  
> **Extracted Media:** `sentinelai_presentation_extracted/assets/`  
> **Authoring Tool:** `PptxGenJS Presentation`  
> **Author:** PptxGenJS  
> **Last Modified By:** Bipin B  
> **Creation Timestamp:** `2026-11-02 15:14:40`  
> **Last Modified Timestamp:** `2026-11-02 15:26:25`  
> **Dimensions:** 10.0" × 5.625" (16:9 Widescreen)  
> **Total Slides:** 15  

---

## Master Slide Index

| Slide # | Title | Subtitle / Section | Speaker Notes Summary | Key Elements |
| :--- | :--- | :--- | :--- | :--- |
| **1** | SentinelAI | FINAL PROJECT PRESENTATION · B.TECH COMPUTER SCIENCE AND ENGINEERING | Welcome. SentinelAI adds two checks around every AI tool call... | Cover, Dual Check diagram, Authors |
| **2** | What we will cover | Our presentation in four simple parts | Four parts: problem, solution, testing, wrap-up. | 4 agenda cards with slide ranges |
| **3** | Background: AI agents act, not just talk | Why this project matters | Chatbots write text. Agents call tools and change real systems... | Chatbot vs Agent comparison cards |
| **4** | Problem statement | Two different things can go wrong | Failure type 1: not permitted. Failure type 2: permitted but did not work... | Authorization vs Outcome failure |
| **5** | Objectives and scope | What we set out to build, and what we kept out | Everything runs locally on synthetic data. No real money or production systems. | 5 Objectives, In-scope, Out-of-scope |
| **6** | Existing approaches and what they miss | Simpler ways to trust an agent | Each simpler method covers only one half of the problem. | 4 naive baselines (1, 2, 3, 4) |
| **7** | Our solution: two layers, two questions | SentinelAI keeps permission and outcome separate | PermissionOS before, WorkflowProof after, audit trail throughout. | PermissionOS (Before) vs WorkflowProof (After) |
| **8** | System architecture | The main building blocks | Core path on top; database, audit and dashboard support it. | 4 pipeline blocks + 3 supporting parts |
| **9** | Pipeline: from request to final result | One request, five steps | Walk through the five steps. Blocked requests stop early... | 5-step horizontal flow + decision paths |
| **10** | PermissionOS: how decisions are made | Deterministic rules, not guesses | Three decisions. The risk score helps explain... | ALLOW, ASK, BLOCK, detectors, 0–100 risk score |
| **11** | WorkflowProof and the audit trail | Example: “Update invoice INV-1001 to Approved” | Three possible verdicts. If we cannot check, we say inconclusive... | VERIFIED, FAILED, INCONCLUSIVE, Audit trail |
| **12** | Methodology: a fair comparison | Four setups, same 12 test scenarios, same starting data | Same inputs and same starting database for every baseline... | 4 Setups (A, B, C, D), scenarios, metrics |
| **13** | Results from the benchmark report | 12 scenarios, 7 of them real failures (preliminary, as reported) | Self-report caught 3 of 7 failures (42.9%); WorkflowProof caught 6 of 7... | Clustered column chart + 3 KPI stat cards |
| **14** | Tools used and honest limitations | What we built with, and what it cannot do | Be honest: this is a student prototype in a controlled setting... | Tech stack + 5 Limitations |
| **15** | Conclusion and next steps | Conclusion and next steps | Summarise: two layers, two questions. Thank the audience... | Contribution, Key finding, Next steps, Closing quote |

---

## Complete Slide-by-Slide Extraction (Line-by-Line, Page-by-Page)

### Slide 1

**Slide Number:** 1 of 15  
**Slide Internal ID:** `256`  
**Background Color:** `16213E (Dark Navy Blue)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Welcome. SentinelAI adds two checks around every AI tool call: one before (is it allowed?) and one after (did it really happen?).

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] FINAL PROJECT PRESENTATION · B.TECH COMPUTER SCIENCE AND ENGINEERING
[Text 1 | lvl 0] SentinelAI
[Text 2 | lvl 0] A Dual-Layer Authorization and Outcome-Verification Framework for Tool-Using AI Agents
[Text 3 | lvl 0] Two separate checks around every tool call made by an AI agent
[Text 5 | lvl 0] BEFORE
[Text 5 | lvl 0] PermissionOS: Is it allowed?
[Text 8 | lvl 0] Tool call
[Text 11 | lvl 0] AFTER
[Text 11 | lvl 0] WorkflowProof: Did it happen?
[Text 12 | lvl 0] PROJECT GROUP MEMBERS
[Text 13 | lvl 0] Bipin B · Goutham Krishna K · Parthip Ashok · Rithuvarna T P · Theertha A
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 43.2, 28.8, 633.6, 21.6 | `None` | "FINAL PROJECT PRESENTATION · B.TECH COMPUTER SCIENCE AND ENGINEERING" (Calibri, 12.0pt, Normal, #AFB9E8) |
| **Text 1** | TEXT_BOX (17) | 43.2, 68.4, 396.0, 64.8 | `None` | "SentinelAI" (Cambria, 54.0pt, Bold, #FFFFFF) |
| **Text 2** | TEXT_BOX (17) | 43.2, 136.8, 388.8, 72.0 | `None` | "A Dual-Layer Authorization and Outcome-Verification Framework for Tool-Using AI Agents" (Cambria, 20.0pt, Normal, #FFFFFF) |
| **Text 3** | TEXT_BOX (17) | 43.2, 216.0, 374.4, 43.2 | `None` | "Two separate checks around every tool call made by an AI agent" (Calibri, 15.0pt, Normal, #AFB9E8) |
| **Shape 4** | AUTO_SHAPE (1) | 482.4, 68.4, 194.4, 68.4 | `#4A44C6` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 489.6, 68.4, 180.0, 68.4 | `None` | "BEFORE" (Calibri, 11.0pt, Bold, #D5D3F7)<br>"PermissionOS: Is it allowed?" (Calibri, 14.0pt, Bold, #FFFFFF) |
| **Shape 6** | AUTO_SHAPE (1) | 568.8, 140.4, 21.6, 25.2 | `#7C8DB5` | [Empty container] |
| **Shape 7** | AUTO_SHAPE (1) | 482.4, 169.2, 194.4, 50.4 | `#2A3560` | [Empty container] |
| **Text 8** | TEXT_BOX (17) | 482.4, 169.2, 194.4, 50.4 | `None` | "Tool call" (Calibri, 16.0pt, Bold, #FFFFFF) |
| **Shape 9** | AUTO_SHAPE (1) | 568.8, 223.2, 21.6, 25.2 | `#7C8DB5` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 482.4, 252.0, 194.4, 68.4 | `#0B7F72` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 489.6, 252.0, 180.0, 68.4 | `None` | "AFTER" (Calibri, 11.0pt, Bold, #CDEFEA)<br>"WorkflowProof: Did it happen?" (Calibri, 14.0pt, Bold, #FFFFFF) |
| **Text 12** | TEXT_BOX (17) | 43.2, 298.8, 360.0, 18.0 | `None` | "PROJECT GROUP MEMBERS" (Calibri, 11.0pt, Bold, #AFB9E8) |
| **Text 13** | TEXT_BOX (17) | 43.2, 320.4, 633.6, 21.6 | `None` | "Bipin B · Goutham Krishna K · Parthip Ashok · Rithuvarna T P · Theertha A" (Calibri, 14.0pt, Normal, #FFFFFF) |

---

### Slide 2

**Slide Number:** 2 of 15  
**Slide Internal ID:** `257`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** image1.png (The Problem), image2.png (The Solution), image3.png (The Testing), image4.png (The Wrap-up)  

#### 🎙️ Speaker Notes (Verbatim)
> Four parts: problem, solution, testing, wrap-up.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] What we will cover
[Text 1 | lvl 0] Our presentation in four simple parts
[Text 2 | lvl 0] 2
[Text 3 | lvl 0] SentinelAI
[Text 6 | lvl 0] The Problem
[Text 7 | lvl 0] Background, problem statement, objectives
[Text 8 | lvl 0] Slides 3–5
[Text 11 | lvl 0] The Solution
[Text 12 | lvl 0] Idea, architecture, pipeline, rules
[Text 13 | lvl 0] Slides 6–10
[Text 16 | lvl 0] The Testing
[Text 17 | lvl 0] Methodology and results
[Text 18 | lvl 0] Slides 11–12
[Text 21 | lvl 0] The Wrap-up
[Text 22 | lvl 0] Tools, limits, conclusion
[Text 23 | lvl 0] Slides 13–15
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "What we will cover" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Our presentation in four simple parts" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "2" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 115.2, 151.2, 230.4 | `#F6F8FC` | [Empty container] |
| **Shape 5** | AUTO_SHAPE (1) | 86.4, 140.4, 50.4, 50.4 | `#4A44C6` | [Empty container] |
| **Image 0** | PICTURE (13) | 100.5, 154.5, 22.2, 22.2 | `None` | Picture element (name=Image 0) |
| **Text 6** | TEXT_BOX (17) | 43.2, 205.2, 136.8, 28.8 | `None` | "The Problem" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 7** | TEXT_BOX (17) | 46.8, 237.6, 129.6, 57.6 | `None` | "Background, problem statement, objectives" (Calibri, 15.0pt, Normal, #55617A) |
| **Text 8** | TEXT_BOX (17) | 43.2, 309.6, 136.8, 21.6 | `None` | "Slides 3–5" (Calibri, 12.0pt, Bold, #4A44C6) |
| **Shape 9** | AUTO_SHAPE (1) | 201.6, 115.2, 151.2, 230.4 | `#F6F8FC` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 252.0, 140.4, 50.4, 50.4 | `#0B7F72` | [Empty container] |
| **Image 1** | PICTURE (13) | 266.1, 154.5, 22.2, 22.2 | `None` | Picture element (name=Image 1) |
| **Text 11** | TEXT_BOX (17) | 208.8, 205.2, 136.8, 28.8 | `None` | "The Solution" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 12** | TEXT_BOX (17) | 212.4, 237.6, 129.6, 57.6 | `None` | "Idea, architecture, pipeline, rules" (Calibri, 15.0pt, Normal, #55617A) |
| **Text 13** | TEXT_BOX (17) | 208.8, 309.6, 136.8, 21.6 | `None` | "Slides 6–10" (Calibri, 12.0pt, Bold, #0B7F72) |
| **Shape 14** | AUTO_SHAPE (1) | 367.2, 115.2, 151.2, 230.4 | `#F6F8FC` | [Empty container] |
| **Shape 15** | AUTO_SHAPE (1) | 417.6, 140.4, 50.4, 50.4 | `#E39A0B` | [Empty container] |
| **Image 2** | PICTURE (13) | 431.7, 154.5, 22.2, 22.2 | `None` | Picture element (name=Image 2) |
| **Text 16** | TEXT_BOX (17) | 374.4, 205.2, 136.8, 28.8 | `None` | "The Testing" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 17** | TEXT_BOX (17) | 378.0, 237.6, 129.6, 57.6 | `None` | "Methodology and results" (Calibri, 15.0pt, Normal, #55617A) |
| **Text 18** | TEXT_BOX (17) | 374.4, 309.6, 136.8, 21.6 | `None` | "Slides 11–12" (Calibri, 12.0pt, Bold, #E39A0B) |
| **Shape 19** | AUTO_SHAPE (1) | 532.8, 115.2, 151.2, 230.4 | `#F6F8FC` | [Empty container] |
| **Shape 20** | AUTO_SHAPE (1) | 583.2, 140.4, 50.4, 50.4 | `#B8304A` | [Empty container] |
| **Image 3** | PICTURE (13) | 597.3, 154.5, 22.2, 22.2 | `None` | Picture element (name=Image 3) |
| **Text 21** | TEXT_BOX (17) | 540.0, 205.2, 136.8, 28.8 | `None` | "The Wrap-up" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 22** | TEXT_BOX (17) | 543.6, 237.6, 129.6, 57.6 | `None` | "Tools, limits, conclusion" (Calibri, 15.0pt, Normal, #55617A) |
| **Text 23** | TEXT_BOX (17) | 540.0, 309.6, 136.8, 21.6 | `None` | "Slides 13–15" (Calibri, 12.0pt, Bold, #B8304A) |

---

### Slide 3

**Slide Number:** 3 of 15  
**Slide Internal ID:** `258`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** image5.png (Chatbot icon), image6.png (Tool-using agent icon)  

#### 🎙️ Speaker Notes (Verbatim)
> Chatbots write text. Agents call tools and change real systems, so mistakes have real effects.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Background: AI agents act, not just talk
[Text 1 | lvl 0] Why this project matters
[Text 2 | lvl 0] 3
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] CHATBOT
[Text 6 | lvl 0] Only writes text
[Text 7 | lvl 0] A wrong answer can be read and ignored.
[Text 9 | lvl 0] TOOL-USING AI AGENT
[Text 10 | lvl 0] Takes real actions
[Text 11 | lvl 0] Changes records, sends messages, runs code.
[Text 15 | lvl 0] A convincing final answer is not proof that the action was allowed or that it worked.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Background: AI agents act, not just talk" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Why this project matters" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "3" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 273.6, 165.6 | `#F6F8FC` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 50.4, 118.8, 244.8, 21.6 | `None` | "CHATBOT" (Calibri, 12.0pt, Bold, #55617A) |
| **Text 6** | TEXT_BOX (17) | 50.4, 140.4, 244.8, 32.4 | `None` | "Only writes text" (Cambria, 22.0pt, Bold, #16213E) |
| **Text 7** | TEXT_BOX (17) | 50.4, 183.6, 244.8, 64.8 | `None` | "A wrong answer can be read and ignored." (Calibri, 16.0pt, Normal, #55617A) |
| **Shape 8** | AUTO_SHAPE (1) | 410.4, 108.0, 273.6, 165.6 | `#E6E5F8` | [Empty container] |
| **Text 9** | TEXT_BOX (17) | 424.8, 118.8, 244.8, 21.6 | `None` | "TOOL-USING AI AGENT" (Calibri, 12.0pt, Bold, #4A44C6) |
| **Text 10** | TEXT_BOX (17) | 424.8, 140.4, 244.8, 32.4 | `None` | "Takes real actions" (Cambria, 22.0pt, Bold, #16213E) |
| **Text 11** | TEXT_BOX (17) | 424.8, 183.6, 244.8, 64.8 | `None` | "Changes records, sends messages, runs code." (Calibri, 16.0pt, Normal, #16213E) |
| **Shape 12** | AUTO_SHAPE (1) | 324.0, 180.0, 72.0, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 13** | AUTO_SHAPE (1) | 255.6, 115.2, 43.2, 43.2 | `#55617A` | [Empty container] |
| **Image 0** | PICTURE (13) | 267.7, 127.3, 19.0, 19.0 | `None` | Picture element (name=Image 0) |
| **Shape 14** | AUTO_SHAPE (1) | 630.0, 115.2, 43.2, 43.2 | `#4A44C6` | [Empty container] |
| **Image 1** | PICTURE (13) | 642.1, 127.3, 19.0, 19.0 | `None` | Picture element (name=Image 1) |
| **Text 15** | TEXT_BOX (17) | 36.0, 302.4, 648.0, 43.2 | `None` | "A convincing final answer is not proof that the action was allowed or that it worked." (Calibri, 16.0pt, Bold, #B8304A) |

---

### Slide 4

**Slide Number:** 4 of 15  
**Slide Internal ID:** `259`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** image7.png (Authorization failure / Shield-cross icon), image8.png (Outcome failure / Broken-gear icon)  

#### 🎙️ Speaker Notes (Verbatim)
> Failure type 1: not permitted. Failure type 2: permitted but did not work. One check cannot cover both.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Problem statement
[Text 1 | lvl 0] Two different things can go wrong
[Text 2 | lvl 0] 4
[Text 3 | lvl 0] SentinelAI
[Text 6 | lvl 0] Authorization failure
[Text 7 | lvl 0] The agent tries something it is not allowed to do, e.g. deleting an invoice without permission.
[Text 10 | lvl 0] Outcome failure
[Text 11 | lvl 0] An allowed action times out or half-completes, yet the agent says “done”.
[Text 13 | lvl 0] The agent’s own message cannot be trusted as proof of what really happened.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Problem statement" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Two different things can go wrong" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "4" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 309.6, 180.0 | `#F6F8FC` | [Empty container] |
| **Shape 5** | AUTO_SHAPE (1) | 50.4, 122.4, 43.2, 43.2 | `#B8304A` | [Empty container] |
| **Image 0** | PICTURE (13) | 62.5, 134.5, 19.0, 19.0 | `None` | Picture element (name=Image 0) |
| **Text 6** | TEXT_BOX (17) | 104.4, 122.4, 230.4, 43.2 | `None` | "Authorization failure" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 7** | TEXT_BOX (17) | 50.4, 176.4, 280.8, 100.8 | `None` | "The agent tries something it is not allowed to do, e.g. deleting an invoice without permission." (Calibri, 15.0pt, Normal, #55617A) |
| **Shape 8** | AUTO_SHAPE (1) | 374.4, 108.0, 309.6, 180.0 | `#F6F8FC` | [Empty container] |
| **Shape 9** | AUTO_SHAPE (1) | 388.8, 122.4, 43.2, 43.2 | `#E39A0B` | [Empty container] |
| **Image 1** | PICTURE (13) | 400.9, 134.5, 19.0, 19.0 | `None` | Picture element (name=Image 1) |
| **Text 10** | TEXT_BOX (17) | 442.8, 122.4, 230.4, 43.2 | `None` | "Outcome failure" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 11** | TEXT_BOX (17) | 388.8, 176.4, 280.8, 100.8 | `None` | "An allowed action times out or half-completes, yet the agent says “done”." (Calibri, 15.0pt, Normal, #55617A) |
| **Shape 12** | AUTO_SHAPE (1) | 36.0, 302.4, 648.0, 54.0 | `#16213E` | [Empty container] |
| **Text 13** | TEXT_BOX (17) | 50.4, 302.4, 619.2, 54.0 | `None` | "The agent’s own message cannot be trusted as proof of what really happened." (Calibri, 16.0pt, Bold, #FFFFFF) |

---

### Slide 5

**Slide Number:** 5 of 15  
**Slide Internal ID:** `260`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Everything runs locally on synthetic data. No real money or production systems.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Objectives and scope
[Text 1 | lvl 0] What we set out to build, and what we kept out
[Text 2 | lvl 0] 5
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] OBJECTIVES
[Text 6 | lvl 0] Check permission before a tool runs
[Text 6 | lvl 0] Check the real result after it runs
[Text 6 | lvl 0] Say clearly: verified, failed, or unsure
[Text 6 | lvl 0] Keep a tamper-evident audit record
[Text 6 | lvl 0] Compare fairly with simpler methods
[Text 8 | lvl 0] IN SCOPE
[Text 9 | lvl 0] A simulated invoice workflow with a mock agent and a test database.
[Text 11 | lvl 0] OUT OF SCOPE
[Text 12 | lvl 0] Real payments, production data and real credentials.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Objectives and scope" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "What we set out to build, and what we kept out" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "5" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 316.8, 244.8 | `#F6F8FC` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 50.4, 116.6, 288.0, 21.6 | `None` | "OBJECTIVES" (Calibri, 12.0pt, Bold, #4A44C6) |
| **Text 6** | TEXT_BOX (17) | 50.4, 144.0, 288.0, 201.6 | `None` | "Check permission before a tool runs" (Calibri, 15.0pt, Normal, #16213E)<br>"Check the real result after it runs" (Calibri, 15.0pt, Normal, #16213E)<br>"Say clearly: verified, failed, or unsure" (Calibri, 15.0pt, Normal, #16213E)<br>"Keep a tamper-evident audit record" (Calibri, 15.0pt, Normal, #16213E)<br>"Compare fairly with simpler methods" (Calibri, 15.0pt, Normal, #16213E) |
| **Shape 7** | AUTO_SHAPE (1) | 367.2, 108.0, 316.8, 115.2 | `#E4F3F1` | [Empty container] |
| **Text 8** | TEXT_BOX (17) | 381.6, 115.2, 288.0, 21.6 | `None` | "IN SCOPE" (Calibri, 12.0pt, Bold, #0B7F72) |
| **Text 9** | TEXT_BOX (17) | 381.6, 140.4, 288.0, 75.6 | `None` | "A simulated invoice workflow with a mock agent and a test database." (Calibri, 15.0pt, Normal, #16213E) |
| **Shape 10** | AUTO_SHAPE (1) | 367.2, 237.6, 316.8, 115.2 | `#F8E6EA` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 381.6, 244.8, 288.0, 21.6 | `None` | "OUT OF SCOPE" (Calibri, 12.0pt, Bold, #B8304A) |
| **Text 12** | TEXT_BOX (17) | 381.6, 270.0, 288.0, 75.6 | `None` | "Real payments, production data and real credentials." (Calibri, 15.0pt, Normal, #16213E) |

---

### Slide 6

**Slide Number:** 6 of 15  
**Slide Internal ID:** `261`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Each simpler method covers only one half of the problem.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Existing approaches and what they miss
[Text 1 | lvl 0] Simpler ways to trust an agent
[Text 2 | lvl 0] 6
[Text 3 | lvl 0] SentinelAI
[Text 6 | lvl 0] 1
[Text 7 | lvl 0] Trust the agent’s message
[Text 8 | lvl 0] Simple, but the agent can be wrong about what happened.
[Text 11 | lvl 0] 2
[Text 12 | lvl 0] Check the tool’s response
[Text 13 | lvl 0] Uses status codes, but may not confirm the final stored data.
[Text 16 | lvl 0] 3
[Text 17 | lvl 0] Check permission only
[Text 18 | lvl 0] Blocks forbidden calls, but an allowed call can still fail.
[Text 21 | lvl 0] 4
[Text 22 | lvl 0] Check the result only
[Text 23 | lvl 0] Finds failed updates, but cannot stop a forbidden action first.
[Text 24 | lvl 0] Our gap: use both checks together.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Existing approaches and what they miss" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Simpler ways to trust an agent" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "6" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 648.0, 50.4 | `#F6F8FC` | [Empty container] |
| **Shape 5** | AUTO_SHAPE (1) | 46.8, 115.2, 36.0, 36.0 | `#B8304A` | [Empty container] |
| **Text 6** | TEXT_BOX (17) | 46.8, 115.2, 36.0, 36.0 | `None` | "1" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 7** | TEXT_BOX (17) | 97.2, 108.0, 230.4, 50.4 | `None` | "Trust the agent’s message" (Calibri, 16.0pt, Bold, #16213E) |
| **Text 8** | TEXT_BOX (17) | 331.2, 108.0, 345.6, 50.4 | `None` | "Simple, but the agent can be wrong about what happened." (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 9** | AUTO_SHAPE (1) | 36.0, 167.0, 648.0, 50.4 | `#F6F8FC` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 46.8, 174.2, 36.0, 36.0 | `#E39A0B` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 46.8, 174.2, 36.0, 36.0 | `None` | "2" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 12** | TEXT_BOX (17) | 97.2, 167.0, 230.4, 50.4 | `None` | "Check the tool’s response" (Calibri, 16.0pt, Bold, #16213E) |
| **Text 13** | TEXT_BOX (17) | 331.2, 167.0, 345.6, 50.4 | `None` | "Uses status codes, but may not confirm the final stored data." (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 14** | AUTO_SHAPE (1) | 36.0, 226.1, 648.0, 50.4 | `#F6F8FC` | [Empty container] |
| **Shape 15** | AUTO_SHAPE (1) | 46.8, 233.3, 36.0, 36.0 | `#4A44C6` | [Empty container] |
| **Text 16** | TEXT_BOX (17) | 46.8, 233.3, 36.0, 36.0 | `None` | "3" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 17** | TEXT_BOX (17) | 97.2, 226.1, 230.4, 50.4 | `None` | "Check permission only" (Calibri, 16.0pt, Bold, #16213E) |
| **Text 18** | TEXT_BOX (17) | 331.2, 226.1, 345.6, 50.4 | `None` | "Blocks forbidden calls, but an allowed call can still fail." (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 19** | AUTO_SHAPE (1) | 36.0, 285.1, 648.0, 50.4 | `#F6F8FC` | [Empty container] |
| **Shape 20** | AUTO_SHAPE (1) | 46.8, 292.3, 36.0, 36.0 | `#0B7F72` | [Empty container] |
| **Text 21** | TEXT_BOX (17) | 46.8, 292.3, 36.0, 36.0 | `None` | "4" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 22** | TEXT_BOX (17) | 97.2, 285.1, 230.4, 50.4 | `None` | "Check the result only" (Calibri, 16.0pt, Bold, #16213E) |
| **Text 23** | TEXT_BOX (17) | 331.2, 285.1, 345.6, 50.4 | `None` | "Finds failed updates, but cannot stop a forbidden action first." (Calibri, 14.0pt, Normal, #55617A) |
| **Text 24** | TEXT_BOX (17) | 36.0, 345.6, 648.0, 21.6 | `None` | "Our gap: use both checks together." (Calibri, 15.0pt, Bold, #4A44C6) |

---

### Slide 7

**Slide Number:** 7 of 15  
**Slide Internal ID:** `262`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** image9.png (PermissionOS / Shield-lock icon), image10.png (WorkflowProof / Checkmark-database icon)  

#### 🎙️ Speaker Notes (Verbatim)
> PermissionOS before, WorkflowProof after, audit trail throughout.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Our solution: two layers, two questions
[Text 1 | lvl 0] SentinelAI keeps permission and outcome separate
[Text 2 | lvl 0] 7
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] BEFORE THE TOOL RUNS
[Text 7 | lvl 0] PermissionOS
[Text 8 | lvl 0] “Is it allowed?”
[Text 9 | lvl 0] Rules decide ALLOW, ASK or BLOCK before anything changes.
[Text 11 | lvl 0] AFTER THE TOOL RUNS
[Text 13 | lvl 0] WorkflowProof
[Text 14 | lvl 0] “Did it happen?”
[Text 15 | lvl 0] Reads the database itself and compares it with what was expected.
[Text 16 | lvl 0] Plus: an audit trail that records every decision and result.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Our solution: two layers, two questions" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "SentinelAI keeps permission and outcome separate" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "7" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 309.6, 201.6 | `#E6E5F8` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 50.4, 116.6, 288.0, 21.6 | `None` | "BEFORE THE TOOL RUNS" (Calibri, 12.0pt, Bold, #4A44C6) |
| **Shape 6** | AUTO_SHAPE (1) | 288.0, 115.2, 43.2, 43.2 | `#4A44C6` | [Empty container] |
| **Image 0** | PICTURE (13) | 300.1, 127.3, 19.0, 19.0 | `None` | Picture element (name=Image 0) |
| **Text 7** | TEXT_BOX (17) | 50.4, 140.4, 288.0, 36.0 | `None` | "PermissionOS" (Cambria, 26.0pt, Bold, #16213E) |
| **Text 8** | TEXT_BOX (17) | 50.4, 180.0, 288.0, 28.8 | `None` | "“Is it allowed?”" (Calibri, 18.0pt, Normal, #4A44C6) |
| **Text 9** | TEXT_BOX (17) | 50.4, 216.0, 280.8, 72.0 | `None` | "Rules decide ALLOW, ASK or BLOCK before anything changes." (Calibri, 15.0pt, Normal, #16213E) |
| **Shape 10** | AUTO_SHAPE (1) | 374.4, 108.0, 309.6, 201.6 | `#E4F3F1` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 388.8, 116.6, 288.0, 21.6 | `None` | "AFTER THE TOOL RUNS" (Calibri, 12.0pt, Bold, #0B7F72) |
| **Shape 12** | AUTO_SHAPE (1) | 626.4, 115.2, 43.2, 43.2 | `#0B7F72` | [Empty container] |
| **Image 1** | PICTURE (13) | 638.5, 127.3, 19.0, 19.0 | `None` | Picture element (name=Image 1) |
| **Text 13** | TEXT_BOX (17) | 388.8, 140.4, 288.0, 36.0 | `None` | "WorkflowProof" (Cambria, 26.0pt, Bold, #16213E) |
| **Text 14** | TEXT_BOX (17) | 388.8, 180.0, 288.0, 28.8 | `None` | "“Did it happen?”" (Calibri, 18.0pt, Normal, #0B7F72) |
| **Text 15** | TEXT_BOX (17) | 388.8, 216.0, 280.8, 72.0 | `None` | "Reads the database itself and compares it with what was expected." (Calibri, 15.0pt, Normal, #16213E) |
| **Text 16** | TEXT_BOX (17) | 36.0, 324.0, 648.0, 28.8 | `None` | "Plus: an audit trail that records every decision and result." (Calibri, 17.0pt, Bold, #16213E) |

---

### Slide 8

**Slide Number:** 8 of 15  
**Slide Internal ID:** `263`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Core path on top; database, audit and dashboard support it.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] System architecture
[Text 1 | lvl 0] The main building blocks
[Text 2 | lvl 0] 8
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] Agent / Client
[Text 5 | lvl 0] Sends the invoice request
[Text 8 | lvl 0] PermissionOS
[Text 8 | lvl 0] Rules + security detectors
[Text 11 | lvl 0] Workflow Service
[Text 11 | lvl 0] Runs allowed actions
[Text 14 | lvl 0] WorkflowProof
[Text 14 | lvl 0] Checks the database
[Text 16 | lvl 0] Database
[Text 16 | lvl 0] Stores invoices and records
[Text 18 | lvl 0] Audit Service
[Text 18 | lvl 0] Hash-linked event log
[Text 20 | lvl 0] Dashboard (React)
[Text 20 | lvl 0] Shows workflows and results
[Text 21 | lvl 0] SUPPORTING PARTS
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "System architecture" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "The main building blocks" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "8" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 115.2, 136.8, 93.6 | `#55617A` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 36.0, 115.2, 136.8, 93.6 | `None` | "Agent / Client" (Calibri, 15.0pt, Bold, #FFFFFF)<br>"Sends the invoice request" (Calibri, 12.0pt, Normal, #FFFFFF) |
| **Shape 6** | AUTO_SHAPE (1) | 175.0, 151.2, 27.4, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 7** | AUTO_SHAPE (1) | 205.2, 115.2, 136.8, 93.6 | `#4A44C6` | [Empty container] |
| **Text 8** | TEXT_BOX (17) | 205.2, 115.2, 136.8, 93.6 | `None` | "PermissionOS" (Calibri, 15.0pt, Bold, #FFFFFF)<br>"Rules + security detectors" (Calibri, 12.0pt, Normal, #FFFFFF) |
| **Shape 9** | AUTO_SHAPE (1) | 344.2, 151.2, 27.4, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 374.4, 115.2, 136.8, 93.6 | `#16213E` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 374.4, 115.2, 136.8, 93.6 | `None` | "Workflow Service" (Calibri, 15.0pt, Bold, #FFFFFF)<br>"Runs allowed actions" (Calibri, 12.0pt, Normal, #FFFFFF) |
| **Shape 12** | AUTO_SHAPE (1) | 513.4, 151.2, 27.4, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 13** | AUTO_SHAPE (1) | 543.6, 115.2, 136.8, 93.6 | `#0B7F72` | [Empty container] |
| **Text 14** | TEXT_BOX (17) | 543.6, 115.2, 136.8, 93.6 | `None` | "WorkflowProof" (Calibri, 15.0pt, Bold, #FFFFFF)<br>"Checks the database" (Calibri, 12.0pt, Normal, #FFFFFF) |
| **Shape 15** | AUTO_SHAPE (1) | 36.0, 244.8, 208.8, 86.4 | `#F6F8FC` | [Empty container] |
| **Text 16** | TEXT_BOX (17) | 46.8, 244.8, 187.2, 86.4 | `None` | "Database" (Calibri, 16.0pt, Bold, #16213E)<br>"Stores invoices and records" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 17** | AUTO_SHAPE (1) | 259.2, 244.8, 208.8, 86.4 | `#F6F8FC` | [Empty container] |
| **Text 18** | TEXT_BOX (17) | 270.0, 244.8, 187.2, 86.4 | `None` | "Audit Service" (Calibri, 16.0pt, Bold, #16213E)<br>"Hash-linked event log" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 19** | AUTO_SHAPE (1) | 482.4, 244.8, 208.8, 86.4 | `#F6F8FC` | [Empty container] |
| **Text 20** | TEXT_BOX (17) | 493.2, 244.8, 187.2, 86.4 | `None` | "Dashboard (React)" (Calibri, 16.0pt, Bold, #16213E)<br>"Shows workflows and results" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 21** | TEXT_BOX (17) | 36.0, 223.2, 288.0, 18.0 | `None` | "SUPPORTING PARTS" (Calibri, 11.0pt, Bold, #55617A) |

---

### Slide 9

**Slide Number:** 9 of 15  
**Slide Internal ID:** `264`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** image11.png (Request icon), image2.png (Policy gate icon), image12.png (Execute icon), image1.png (Verify icon), image13.png (Audit icon)  

#### 🎙️ Speaker Notes (Verbatim)
> Walk through the five steps. Blocked requests stop early; allowed requests are still verified.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Pipeline: from request to final result
[Text 1 | lvl 0] One request, five steps
[Text 2 | lvl 0] 9
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] Request
[Text 6 | lvl 0] Invoice operation arrives
[Text 9 | lvl 0] Policy gate
[Text 10 | lvl 0] ALLOW / ASK / BLOCK
[Text 13 | lvl 0] Execute
[Text 14 | lvl 0] Mock workflow runs it
[Text 17 | lvl 0] Verify
[Text 18 | lvl 0] Read real database state
[Text 21 | lvl 0] Audit
[Text 22 | lvl 0] Save the full record
[Text 24 | lvl 0] If BLOCKED
[Text 24 | lvl 0] Stops before execution. Nothing changes.
[Text 26 | lvl 0] If ALLOWED
[Text 26 | lvl 0] Can still fail, so we always verify.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Pipeline: from request to final result" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "One request, five steps" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "9" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 64.8, 111.6, 50.4, 50.4 | `#55617A` | [Empty container] |
| **Image 0** | PICTURE (13) | 78.9, 125.7, 22.2, 22.2 | `None` | Picture element (name=Image 0) |
| **Text 5** | TEXT_BOX (17) | 36.0, 169.2, 108.0, 25.2 | `None` | "Request" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 6** | TEXT_BOX (17) | 32.4, 195.8, 115.2, 46.8 | `None` | "Invoice operation arrives" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 7** | AUTO_SHAPE (1) | 123.8, 126.0, 36.0, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 8** | AUTO_SHAPE (1) | 195.8, 111.6, 50.4, 50.4 | `#4A44C6` | [Empty container] |
| **Image 1** | PICTURE (13) | 210.0, 125.7, 22.2, 22.2 | `None` | Picture element (name=Image 1) |
| **Text 9** | TEXT_BOX (17) | 167.0, 169.2, 108.0, 25.2 | `None` | "Policy gate" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 10** | TEXT_BOX (17) | 163.4, 195.8, 115.2, 46.8 | `None` | "ALLOW / ASK / BLOCK" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 11** | AUTO_SHAPE (1) | 254.9, 126.0, 36.0, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 12** | AUTO_SHAPE (1) | 326.9, 111.6, 50.4, 50.4 | `#16213E` | [Empty container] |
| **Image 2** | PICTURE (13) | 341.0, 125.7, 22.2, 22.2 | `None` | Picture element (name=Image 2) |
| **Text 13** | TEXT_BOX (17) | 298.1, 169.2, 108.0, 25.2 | `None` | "Execute" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 14** | TEXT_BOX (17) | 294.5, 195.8, 115.2, 46.8 | `None` | "Mock workflow runs it" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 15** | AUTO_SHAPE (1) | 385.9, 126.0, 36.0, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 16** | AUTO_SHAPE (1) | 457.9, 111.6, 50.4, 50.4 | `#0B7F72` | [Empty container] |
| **Image 3** | PICTURE (13) | 472.0, 125.7, 22.2, 22.2 | `None` | Picture element (name=Image 3) |
| **Text 17** | TEXT_BOX (17) | 429.1, 169.2, 108.0, 25.2 | `None` | "Verify" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 18** | TEXT_BOX (17) | 425.5, 195.8, 115.2, 46.8 | `None` | "Read real database state" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 19** | AUTO_SHAPE (1) | 517.0, 126.0, 36.0, 21.6 | `#9AA5C0` | [Empty container] |
| **Shape 20** | AUTO_SHAPE (1) | 589.0, 111.6, 50.4, 50.4 | `#E39A0B` | [Empty container] |
| **Image 4** | PICTURE (13) | 603.1, 125.7, 22.2, 22.2 | `None` | Picture element (name=Image 4) |
| **Text 21** | TEXT_BOX (17) | 560.2, 169.2, 108.0, 25.2 | `None` | "Audit" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 22** | TEXT_BOX (17) | 556.6, 195.8, 115.2, 46.8 | `None` | "Save the full record" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 23** | AUTO_SHAPE (1) | 36.0, 259.2, 316.8, 93.6 | `#F8E6EA` | [Empty container] |
| **Text 24** | TEXT_BOX (17) | 50.4, 259.2, 288.0, 93.6 | `None` | "If BLOCKED" (Calibri, 15.0pt, Bold, #B8304A)<br>"Stops before execution. Nothing changes." (Calibri, 15.0pt, Normal, #16213E) |
| **Shape 25** | AUTO_SHAPE (1) | 367.2, 259.2, 316.8, 93.6 | `#FDF1DA` | [Empty container] |
| **Text 26** | TEXT_BOX (17) | 381.6, 259.2, 288.0, 93.6 | `None` | "If ALLOWED" (Calibri, 15.0pt, Bold, #9A6606)<br>"Can still fail, so we always verify." (Calibri, 15.0pt, Normal, #16213E) |

---

### Slide 10

**Slide Number:** 10 of 15  
**Slide Internal ID:** `265`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Three decisions. The risk score helps explain, but permission rules have the final word.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] PermissionOS: how decisions are made
[Text 1 | lvl 0] Deterministic rules, not guesses
[Text 2 | lvl 0] 10
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] ALLOW
[Text 5 | lvl 0] Proceed with the action
[Text 7 | lvl 0] ASK
[Text 7 | lvl 0] Pause for approval
[Text 9 | lvl 0] BLOCK
[Text 9 | lvl 0] Stop before execution
[Text 11 | lvl 0] What it checks
[Text 12 | lvl 0] Commands, files and network use
[Text 12 | lvl 0] Secrets and data leaks
[Text 12 | lvl 0] Prompt-injection signs
[Text 12 | lvl 0] Invoice rules: negative amount, restricted vendor
[Text 14 | lvl 0] Risk score (0–100)
[Text 15 | lvl 0] Adds up severity and context, and is explainable. It raises scrutiny but never overrides a hard denial. Rules live in a YAML policy file.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "PermissionOS: how decisions are made" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Deterministic rules, not guesses" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "10" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 208.8, 79.2 | `#0B7F72` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 36.0, 108.0, 208.8, 79.2 | `None` | "ALLOW" (Calibri, 22.0pt, Bold, #FFFFFF)<br>"Proceed with the action" (Calibri, 14.0pt, Normal, #FFFFFF) |
| **Shape 6** | AUTO_SHAPE (1) | 259.2, 108.0, 208.8, 79.2 | `#E39A0B` | [Empty container] |
| **Text 7** | TEXT_BOX (17) | 259.2, 108.0, 208.8, 79.2 | `None` | "ASK" (Calibri, 22.0pt, Bold, #16213E)<br>"Pause for approval" (Calibri, 14.0pt, Normal, #16213E) |
| **Shape 8** | AUTO_SHAPE (1) | 482.4, 108.0, 208.8, 79.2 | `#B8304A` | [Empty container] |
| **Text 9** | TEXT_BOX (17) | 482.4, 108.0, 208.8, 79.2 | `None` | "BLOCK" (Calibri, 22.0pt, Bold, #FFFFFF)<br>"Stop before execution" (Calibri, 14.0pt, Normal, #FFFFFF) |
| **Shape 10** | AUTO_SHAPE (1) | 36.0, 208.8, 316.8, 144.0 | `#F6F8FC` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 50.4, 216.0, 288.0, 21.6 | `None` | "What it checks" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 12** | TEXT_BOX (17) | 50.4, 241.2, 288.0, 108.0 | `None` | "Commands, files and network use" (Calibri, 14.0pt, Normal, #16213E)<br>"Secrets and data leaks" (Calibri, 14.0pt, Normal, #16213E)<br>"Prompt-injection signs" (Calibri, 14.0pt, Normal, #16213E)<br>"Invoice rules: negative amount, restricted vendor" (Calibri, 14.0pt, Normal, #16213E) |
| **Shape 13** | AUTO_SHAPE (1) | 367.2, 208.8, 316.8, 144.0 | `#F6F8FC` | [Empty container] |
| **Text 14** | TEXT_BOX (17) | 381.6, 216.0, 288.0, 21.6 | `None` | "Risk score (0–100)" (Cambria, 16.0pt, Bold, #16213E) |
| **Text 15** | TEXT_BOX (17) | 381.6, 241.2, 288.0, 108.0 | `None` | "Adds up severity and context, and is explainable. It raises scrutiny but never overrides a hard denial. Rules live in a YAML policy file." (Calibri, 14.0pt, Normal, #16213E) |

---

### Slide 11

**Slide Number:** 11 of 15  
**Slide Internal ID:** `266`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Three possible verdicts. If we cannot check, we say inconclusive, never success. Audit log is tamper-evident.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] WorkflowProof and the audit trail
[Text 1 | lvl 0] Example: “Update invoice INV-1001 to Approved”
[Text 2 | lvl 0] 11
[Text 3 | lvl 0] SentinelAI
[Text 6 | lvl 0] VERIFIED
[Text 7 | lvl 0] Database shows Approved
[Text 10 | lvl 0] FAILED
[Text 11 | lvl 0] Database still shows Pending
[Text 14 | lvl 0] INCONCLUSIVE
[Text 15 | lvl 0] Database unavailable, cannot tell
[Text 16 | lvl 0] Unsure is never treated as success.
[Text 18 | lvl 0] Audit trail
[Text 19 | lvl 0] Each event is linked to the last using SHA-256 hashes
[Text 19 | lvl 0] Changing a record breaks the chain, so tampering is visible
[Text 19 | lvl 0] Sensitive values are scrubbed
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "WorkflowProof and the audit trail" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Example: “Update invoice INV-1001 to Approved”" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "11" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 388.8, 57.6 | `#F6F8FC` | [Empty container] |
| **Shape 5** | AUTO_SHAPE (1) | 46.8, 118.8, 136.8, 36.0 | `#0B7F72` | [Empty container] |
| **Text 6** | TEXT_BOX (17) | 46.8, 118.8, 136.8, 36.0 | `None` | "VERIFIED" (Calibri, 14.0pt, Bold, #FFFFFF) |
| **Text 7** | TEXT_BOX (17) | 194.4, 108.0, 223.2, 57.6 | `None` | "Database shows Approved" (Calibri, 14.0pt, Normal, #16213E) |
| **Shape 8** | AUTO_SHAPE (1) | 36.0, 176.4, 388.8, 57.6 | `#F6F8FC` | [Empty container] |
| **Shape 9** | AUTO_SHAPE (1) | 46.8, 187.2, 136.8, 36.0 | `#B8304A` | [Empty container] |
| **Text 10** | TEXT_BOX (17) | 46.8, 187.2, 136.8, 36.0 | `None` | "FAILED" (Calibri, 14.0pt, Bold, #FFFFFF) |
| **Text 11** | TEXT_BOX (17) | 194.4, 176.4, 223.2, 57.6 | `None` | "Database still shows Pending" (Calibri, 14.0pt, Normal, #16213E) |
| **Shape 12** | AUTO_SHAPE (1) | 36.0, 244.8, 388.8, 57.6 | `#F6F8FC` | [Empty container] |
| **Shape 13** | AUTO_SHAPE (1) | 46.8, 255.6, 136.8, 36.0 | `#E39A0B` | [Empty container] |
| **Text 14** | TEXT_BOX (17) | 46.8, 255.6, 136.8, 36.0 | `None` | "INCONCLUSIVE" (Calibri, 14.0pt, Bold, #FFFFFF) |
| **Text 15** | TEXT_BOX (17) | 194.4, 244.8, 223.2, 57.6 | `None` | "Database unavailable, cannot tell" (Calibri, 14.0pt, Normal, #16213E) |
| **Text 16** | TEXT_BOX (17) | 36.0, 316.8, 388.8, 28.8 | `None` | "Unsure is never treated as success." (Calibri, 15.0pt, Bold, #4A44C6) |
| **Shape 17** | AUTO_SHAPE (1) | 446.4, 108.0, 237.6, 237.6 | `#E6E5F8` | [Empty container] |
| **Text 18** | TEXT_BOX (17) | 460.8, 115.2, 208.8, 28.8 | `None` | "Audit trail" (Cambria, 18.0pt, Bold, #16213E) |
| **Text 19** | TEXT_BOX (17) | 460.8, 151.2, 208.8, 187.2 | `None` | "Each event is linked to the last using SHA-256 hashes" (Calibri, 14.0pt, Normal, #16213E)<br>"Changing a record breaks the chain, so tampering is visible" (Calibri, 14.0pt, Normal, #16213E)<br>"Sensitive values are scrubbed" (Calibri, 14.0pt, Normal, #16213E) |

---

### Slide 12

**Slide Number:** 12 of 15  
**Slide Internal ID:** `267`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Same inputs and same starting database for every baseline. Inconclusive is never counted as verified.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Methodology: a fair comparison
[Text 1 | lvl 0] Four setups, same 12 test scenarios, same starting data
[Text 2 | lvl 0] 12
[Text 3 | lvl 0] SentinelAI
[Text 6 | lvl 0] A
[Text 7 | lvl 0] Agent self-report
[Text 8 | lvl 0] Trust what the agent says
[Text 11 | lvl 0] B
[Text 12 | lvl 0] Tool response
[Text 13 | lvl 0] Trust the API status
[Text 16 | lvl 0] C
[Text 17 | lvl 0] WorkflowProof only
[Text 18 | lvl 0] Check the result afterward
[Text 21 | lvl 0] D
[Text 22 | lvl 0] Combined SentinelAI
[Text 23 | lvl 0] Permission check + result check
[Text 25 | lvl 0] Test scenarios
[Text 26 | lvl 0] Normal, missing write, rollback, wrong value, partial update, duplicate, timeout, outage, policy-denied.
[Text 28 | lvl 0] What we measure
[Text 29 | lvl 0] False-success accepted, failures detected, unauthorized actions blocked, inconclusive rate, latency.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Methodology: a fair comparison" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "Four setups, same 12 test scenarios, same starting data" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "12" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 151.2, 126.0 | `#F6F8FC` | [Empty container] |
| **Shape 5** | AUTO_SHAPE (1) | 44.6, 116.6, 36.0, 36.0 | `#B8304A` | [Empty container] |
| **Text 6** | TEXT_BOX (17) | 44.6, 116.6, 36.0, 36.0 | `None` | "A" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 7** | TEXT_BOX (17) | 44.6, 158.4, 136.8, 25.2 | `None` | "Agent self-report" (Calibri, 14.0pt, Bold, #16213E) |
| **Text 8** | TEXT_BOX (17) | 44.6, 183.6, 136.8, 43.2 | `None` | "Trust what the agent says" (Calibri, 12.0pt, Normal, #55617A) |
| **Shape 9** | AUTO_SHAPE (1) | 201.6, 108.0, 151.2, 126.0 | `#F6F8FC` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 210.2, 116.6, 36.0, 36.0 | `#E39A0B` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 210.2, 116.6, 36.0, 36.0 | `None` | "B" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 12** | TEXT_BOX (17) | 210.2, 158.4, 136.8, 25.2 | `None` | "Tool response" (Calibri, 14.0pt, Bold, #16213E) |
| **Text 13** | TEXT_BOX (17) | 210.2, 183.6, 136.8, 43.2 | `None` | "Trust the API status" (Calibri, 12.0pt, Normal, #55617A) |
| **Shape 14** | AUTO_SHAPE (1) | 367.2, 108.0, 151.2, 126.0 | `#F6F8FC` | [Empty container] |
| **Shape 15** | AUTO_SHAPE (1) | 375.8, 116.6, 36.0, 36.0 | `#0B7F72` | [Empty container] |
| **Text 16** | TEXT_BOX (17) | 375.8, 116.6, 36.0, 36.0 | `None` | "C" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 17** | TEXT_BOX (17) | 375.8, 158.4, 136.8, 25.2 | `None` | "WorkflowProof only" (Calibri, 14.0pt, Bold, #16213E) |
| **Text 18** | TEXT_BOX (17) | 375.8, 183.6, 136.8, 43.2 | `None` | "Check the result afterward" (Calibri, 12.0pt, Normal, #55617A) |
| **Shape 19** | AUTO_SHAPE (1) | 532.8, 108.0, 151.2, 126.0 | `#F6F8FC` | [Empty container] |
| **Shape 20** | AUTO_SHAPE (1) | 541.4, 116.6, 36.0, 36.0 | `#4A44C6` | [Empty container] |
| **Text 21** | TEXT_BOX (17) | 541.4, 116.6, 36.0, 36.0 | `None` | "D" (Cambria, 16.0pt, Bold, #FFFFFF) |
| **Text 22** | TEXT_BOX (17) | 541.4, 158.4, 136.8, 25.2 | `None` | "Combined SentinelAI" (Calibri, 14.0pt, Bold, #16213E) |
| **Text 23** | TEXT_BOX (17) | 541.4, 183.6, 136.8, 43.2 | `None` | "Permission check + result check" (Calibri, 12.0pt, Normal, #55617A) |
| **Shape 24** | AUTO_SHAPE (1) | 36.0, 252.0, 316.8, 100.8 | `#F6F8FC` | [Empty container] |
| **Text 25** | TEXT_BOX (17) | 50.4, 257.8, 288.0, 21.6 | `None` | "Test scenarios" (Cambria, 15.0pt, Bold, #16213E) |
| **Text 26** | TEXT_BOX (17) | 50.4, 280.8, 288.0, 68.4 | `None` | "Normal, missing write, rollback, wrong value, partial update, duplicate, timeout, outage, policy-denied." (Calibri, 13.0pt, Normal, #55617A) |
| **Shape 27** | AUTO_SHAPE (1) | 367.2, 252.0, 316.8, 100.8 | `#F6F8FC` | [Empty container] |
| **Text 28** | TEXT_BOX (17) | 381.6, 257.8, 288.0, 21.6 | `None` | "What we measure" (Cambria, 15.0pt, Bold, #16213E) |
| **Text 29** | TEXT_BOX (17) | 381.6, 280.8, 288.0, 68.4 | `None` | "False-success accepted, failures detected, unauthorized actions blocked, inconclusive rate, latency." (Calibri, 13.0pt, Normal, #55617A) |

---

### Slide 13

**Slide Number:** 13 of 15  
**Slide Internal ID:** `268`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Self-report caught 3 of 7 failures (42.9%); WorkflowProof caught 6 of 7 (85.7%). One false success still got through. These are reported results from a small SQLite run and must be reproduced before calling them validated.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Results from the benchmark report
[Text 1 | lvl 0] 12 scenarios, 7 of them real failures (preliminary, as reported)
[Text 2 | lvl 0] 13
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] 3 of 7 → 6 of 7
[Text 6 | lvl 0] failures caught
[Text 8 | lvl 0] 4 → 1
[Text 9 | lvl 0] false successes accepted
[Text 11 | lvl 0] 11.88 ms
[Text 12 | lvl 0] mean verification time
[Text 13 | lvl 0] Small test, one setup. Results need re-running from a clean environment.
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Results from the benchmark report" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "12 scenarios, 7 of them real failures (preliminary, as reported)" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "13" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Chart 0** | CHART (3) | 36.0, 104.4, 331.2, 230.4 | `None` | Chart: Failure detection rate (%) |
| **Shape 4** | AUTO_SHAPE (1) | 388.8, 104.4, 295.2, 72.0 | `#F6F8FC` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 399.6, 108.0, 273.6, 36.0 | `None` | "3 of 7 → 6 of 7" (Cambria, 24.0pt, Bold, #0B7F72) |
| **Text 6** | TEXT_BOX (17) | 399.6, 144.0, 273.6, 25.2 | `None` | "failures caught" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 7** | AUTO_SHAPE (1) | 388.8, 187.2, 295.2, 72.0 | `#F6F8FC` | [Empty container] |
| **Text 8** | TEXT_BOX (17) | 399.6, 190.8, 273.6, 36.0 | `None` | "4 → 1" (Cambria, 24.0pt, Bold, #4A44C6) |
| **Text 9** | TEXT_BOX (17) | 399.6, 226.8, 273.6, 25.2 | `None` | "false successes accepted" (Calibri, 14.0pt, Normal, #55617A) |
| **Shape 10** | AUTO_SHAPE (1) | 388.8, 270.0, 295.2, 72.0 | `#F6F8FC` | [Empty container] |
| **Text 11** | TEXT_BOX (17) | 399.6, 273.6, 273.6, 36.0 | `None` | "11.88 ms" (Cambria, 24.0pt, Bold, #E39A0B) |
| **Text 12** | TEXT_BOX (17) | 399.6, 309.6, 273.6, 25.2 | `None` | "mean verification time" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 13** | TEXT_BOX (17) | 36.0, 345.6, 619.2, 21.6 | `None` | "Small test, one setup. Results need re-running from a clean environment." (Calibri, 12.0pt, Normal, #55617A) |

---

### Slide 14

**Slide Number:** 14 of 15  
**Slide Internal ID:** `269`  
**Background Color:** `FFFFFF (Pure White)`  
**Embedded Icons / Images:** None  

#### 🎙️ Speaker Notes (Verbatim)
> Be honest: this is a student prototype in a controlled setting, not a universal security boundary.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Tools used and honest limitations
[Text 1 | lvl 0] What we built with, and what it cannot do
[Text 2 | lvl 0] 14
[Text 3 | lvl 0] SentinelAI
[Text 5 | lvl 0] Technology stack
[Text 6 | lvl 0] Python 3.11 + FastAPI
[Text 6 | lvl 0] SQLAlchemy, PostgreSQL / SQLite
[Text 6 | lvl 0] React 19 + TypeScript + Vite
[Text 6 | lvl 0] YAML policies, Docker Compose
[Text 6 | lvl 0] Pytest, Vitest, GitHub Actions
[Text 8 | lvl 0] Limitations
[Text 9 | lvl 0] Pattern-based detectors can miss new attacks
[Text 9 | lvl 0] Only the checked conditions are proven
[Text 9 | lvl 0] Hash chain shows tampering, does not prevent it
[Text 9 | lvl 0] Extra checks add some delay
[Text 9 | lvl 0] Tested only on a simulated invoice demo
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 21.6, 648.0, 46.8 | `None` | "Tools used and honest limitations" (Cambria, 30.0pt, Bold, #16213E) |
| **Text 1** | TEXT_BOX (17) | 36.0, 68.4, 648.0, 25.2 | `None` | "What we built with, and what it cannot do" (Calibri, 14.0pt, Normal, #55617A) |
| **Text 2** | TEXT_BOX (17) | 662.4, 374.4, 28.8, 21.6 | `None` | "14" (Calibri, 11.0pt, Normal, #55617A) |
| **Text 3** | TEXT_BOX (17) | 36.0, 374.4, 216.0, 21.6 | `None` | "SentinelAI" (Calibri, 11.0pt, Normal, #55617A) |
| **Shape 4** | AUTO_SHAPE (1) | 36.0, 108.0, 316.8, 244.8 | `#F6F8FC` | [Empty container] |
| **Text 5** | TEXT_BOX (17) | 50.4, 115.2, 288.0, 25.2 | `None` | "Technology stack" (Cambria, 17.0pt, Bold, #16213E) |
| **Text 6** | TEXT_BOX (17) | 50.4, 147.6, 288.0, 194.4 | `None` | "Python 3.11 + FastAPI" (Calibri, 17.0pt, Normal, #16213E)<br>"SQLAlchemy, PostgreSQL / SQLite" (Calibri, 17.0pt, Normal, #16213E)<br>"React 19 + TypeScript + Vite" (Calibri, 17.0pt, Normal, #16213E)<br>"YAML policies, Docker Compose" (Calibri, 17.0pt, Normal, #16213E)<br>"Pytest, Vitest, GitHub Actions" (Calibri, 17.0pt, Normal, #16213E) |
| **Shape 7** | AUTO_SHAPE (1) | 367.2, 108.0, 316.8, 244.8 | `#F8E6EA` | [Empty container] |
| **Text 8** | TEXT_BOX (17) | 381.6, 115.2, 288.0, 25.2 | `None` | "Limitations" (Cambria, 17.0pt, Bold, #B8304A) |
| **Text 9** | TEXT_BOX (17) | 381.6, 147.6, 288.0, 194.4 | `None` | "Pattern-based detectors can miss new attacks" (Calibri, 16.0pt, Normal, #16213E)<br>"Only the checked conditions are proven" (Calibri, 16.0pt, Normal, #16213E)<br>"Hash chain shows tampering, does not prevent it" (Calibri, 16.0pt, Normal, #16213E)<br>"Extra checks add some delay" (Calibri, 16.0pt, Normal, #16213E)<br>"Tested only on a simulated invoice demo" (Calibri, 16.0pt, Normal, #16213E) |

---

### Slide 15

**Slide Number:** 15 of 15  
**Slide Internal ID:** `270`  
**Background Color:** `16213E (Dark Navy Blue)`  
**Embedded Icons / Images:** image5.png (Contribution icon), image10.png (Key finding icon), image4.png (Next steps icon)  

#### 🎙️ Speaker Notes (Verbatim)
> Summarise: two layers, two questions. Thank the audience and open for questions.

#### 📄 Verbatim Text on Slide (Exact Appearance Order)
```text
[Text 0 | lvl 0] Conclusion and next steps
[Text 3 | lvl 0] Contribution
[Text 4 | lvl 0] Working prototype with a policy gate, state verifier, audit trail and benchmark harness.
[Text 7 | lvl 0] Key finding
[Text 8 | lvl 0] Checking the real result caught more failures than trusting the agent (6 of 7 vs 3 of 7).
[Text 11 | lvl 0] Next steps
[Text 12 | lvl 0] Re-run benchmark cleanly, fix report inconsistencies, test more scenarios.
[Text 13 | lvl 0] Ask: Is it allowed?  Then check: Did it happen?
```

#### 🔍 Detailed Shape & Typography Breakdown
| Shape Name | Shape Type | Position (L, T, W, H in pt) | Fill Color | Content & Runs (Font, Size, Weight, Color) |
| :--- | :--- | :--- | :--- | :--- |
| **Text 0** | TEXT_BOX (17) | 36.0, 25.2, 648.0, 46.8 | `None` | "Conclusion and next steps" (Cambria, 30.0pt, Bold, #FFFFFF) |
| **Shape 1** | AUTO_SHAPE (1) | 36.0, 93.6, 208.8, 158.4 | `#1F2D55` | [Empty container] |
| **Shape 2** | AUTO_SHAPE (1) | 194.4, 100.8, 36.0, 36.0 | `#4A44C6` | [Empty container] |
| **Image 0** | PICTURE (13) | 204.5, 110.9, 15.8, 15.8 | `None` | Picture element (name=Image 0) |
| **Text 3** | TEXT_BOX (17) | 50.4, 104.4, 144.0, 28.8 | `None` | "Contribution" (Cambria, 18.0pt, Bold, #B8B5F5) |
| **Text 4** | TEXT_BOX (17) | 50.4, 140.4, 180.0, 104.4 | `None` | "Working prototype with a policy gate, state verifier, audit trail and benchmark harness." (Calibri, 15.0pt, Normal, #FFFFFF) |
| **Shape 5** | AUTO_SHAPE (1) | 259.2, 93.6, 208.8, 158.4 | `#1F2D55` | [Empty container] |
| **Shape 6** | AUTO_SHAPE (1) | 417.6, 100.8, 36.0, 36.0 | `#0B7F72` | [Empty container] |
| **Image 1** | PICTURE (13) | 427.7, 110.9, 15.8, 15.8 | `None` | Picture element (name=Image 1) |
| **Text 7** | TEXT_BOX (17) | 273.6, 104.4, 144.0, 28.8 | `None` | "Key finding" (Cambria, 18.0pt, Bold, #0B7F72) |
| **Text 8** | TEXT_BOX (17) | 273.6, 140.4, 180.0, 104.4 | `None` | "Checking the real result caught more failures than trusting the agent (6 of 7 vs 3 of 7)." (Calibri, 15.0pt, Normal, #FFFFFF) |
| **Shape 9** | AUTO_SHAPE (1) | 482.4, 93.6, 208.8, 158.4 | `#1F2D55` | [Empty container] |
| **Shape 10** | AUTO_SHAPE (1) | 640.8, 100.8, 36.0, 36.0 | `#E39A0B` | [Empty container] |
| **Image 2** | PICTURE (13) | 650.9, 110.9, 15.8, 15.8 | `None` | Picture element (name=Image 2) |
| **Text 11** | TEXT_BOX (17) | 496.8, 104.4, 144.0, 28.8 | `None` | "Next steps" (Cambria, 18.0pt, Bold, #E39A0B) |
| **Text 12** | TEXT_BOX (17) | 496.8, 140.4, 180.0, 104.4 | `None` | "Re-run benchmark cleanly, fix report inconsistencies, test more scenarios." (Calibri, 15.0pt, Normal, #FFFFFF) |
| **Text 13** | TEXT_BOX (17) | 36.0, 280.8, 648.0, 32.4 | `None` | "Ask: Is it allowed?  Then check: Did it happen?" (Cambria, 20.0pt, Normal, #AFB9E8) |

---

## Slide 13 Chart Specification & Raw Benchmark Data

Slide 13 embeds an actual PowerPoint native chart object (`Chart 0`):
- **Chart Type:** `COLUMN_CLUSTERED` (Excel Clustered Column)
- **Chart Title:** `Failure detection rate (%)`
- **X-Axis Categories:**
  1. `Agent self-report`
  2. `WorkflowProof`
- **Series Name:** `Failures detected (%)`
- **Numeric Values:**
  - `Agent self-report`: **42.9%** (3 of 7 failures caught)
  - `WorkflowProof`: **85.7%** (6 of 7 failures caught)

### Accompanying KPI Stat Cards on Slide 13:
1. **Failures Caught:** `3 of 7 → 6 of 7` (failures caught)
2. **False Successes Accepted:** `4 → 1` (false successes accepted)
3. **Mean Latency:** `11.88 ms` (mean verification time)
4. **Footer Caveat:** `Small test, one setup. Results need re-running from a clean environment.`

---

## Master Linear Transcript (Verbatim Line-by-Line for Entire PPT)

Below is the complete verbatim text content from Slide 1 to Slide 15 in exact chronological order without any omissions:

```text
=== [SLIDE 1] ===
SPEAKER NOTES: Welcome. SentinelAI adds two checks around every AI tool call: one before (is it allowed?) and one after (did it really happen?).
FINAL PROJECT PRESENTATION · B.TECH COMPUTER SCIENCE AND ENGINEERING
SentinelAI
A Dual-Layer Authorization and Outcome-Verification Framework for Tool-Using AI Agents
Two separate checks around every tool call made by an AI agent
BEFORE
PermissionOS: Is it allowed?
Tool call
AFTER
WorkflowProof: Did it happen?
PROJECT GROUP MEMBERS
Bipin B · Goutham Krishna K · Parthip Ashok · Rithuvarna T P · Theertha A

=== [SLIDE 2] ===
SPEAKER NOTES: Four parts: problem, solution, testing, wrap-up.
What we will cover
Our presentation in four simple parts
2
SentinelAI
The Problem
Background, problem statement, objectives
Slides 3–5
The Solution
Idea, architecture, pipeline, rules
Slides 6–10
The Testing
Methodology and results
Slides 11–12
The Wrap-up
Tools, limits, conclusion
Slides 13–15

=== [SLIDE 3] ===
SPEAKER NOTES: Chatbots write text. Agents call tools and change real systems, so mistakes have real effects.
Background: AI agents act, not just talk
Why this project matters
3
SentinelAI
CHATBOT
Only writes text
A wrong answer can be read and ignored.
TOOL-USING AI AGENT
Takes real actions
Changes records, sends messages, runs code.
A convincing final answer is not proof that the action was allowed or that it worked.

=== [SLIDE 4] ===
SPEAKER NOTES: Failure type 1: not permitted. Failure type 2: permitted but did not work. One check cannot cover both.
Problem statement
Two different things can go wrong
4
SentinelAI
Authorization failure
The agent tries something it is not allowed to do, e.g. deleting an invoice without permission.
Outcome failure
An allowed action times out or half-completes, yet the agent says “done”.
The agent’s own message cannot be trusted as proof of what really happened.

=== [SLIDE 5] ===
SPEAKER NOTES: Everything runs locally on synthetic data. No real money or production systems.
Objectives and scope
What we set out to build, and what we kept out
5
SentinelAI
OBJECTIVES
Check permission before a tool runs
Check the real result after it runs
Say clearly: verified, failed, or unsure
Keep a tamper-evident audit record
Compare fairly with simpler methods
IN SCOPE
A simulated invoice workflow with a mock agent and a test database.
OUT OF SCOPE
Real payments, production data and real credentials.

=== [SLIDE 6] ===
SPEAKER NOTES: Each simpler method covers only one half of the problem.
Existing approaches and what they miss
Simpler ways to trust an agent
6
SentinelAI
1
Trust the agent’s message
Simple, but the agent can be wrong about what happened.
2
Check the tool’s response
Uses status codes, but may not confirm the final stored data.
3
Check permission only
Blocks forbidden calls, but an allowed call can still fail.
4
Check the result only
Finds failed updates, but cannot stop a forbidden action first.
Our gap: use both checks together.

=== [SLIDE 7] ===
SPEAKER NOTES: PermissionOS before, WorkflowProof after, audit trail throughout.
Our solution: two layers, two questions
SentinelAI keeps permission and outcome separate
7
SentinelAI
BEFORE THE TOOL RUNS
PermissionOS
“Is it allowed?”
Rules decide ALLOW, ASK or BLOCK before anything changes.
AFTER THE TOOL RUNS
WorkflowProof
“Did it happen?”
Reads the database itself and compares it with what was expected.
Plus: an audit trail that records every decision and result.

=== [SLIDE 8] ===
SPEAKER NOTES: Core path on top; database, audit and dashboard support it.
System architecture
The main building blocks
8
SentinelAI
Agent / Client
Sends the invoice request
PermissionOS
Rules + security detectors
Workflow Service
Runs allowed actions
WorkflowProof
Checks the database
Database
Stores invoices and records
Audit Service
Hash-linked event log
Dashboard (React)
Shows workflows and results
SUPPORTING PARTS

=== [SLIDE 9] ===
SPEAKER NOTES: Walk through the five steps. Blocked requests stop early; allowed requests are still verified.
Pipeline: from request to final result
One request, five steps
9
SentinelAI
Request
Invoice operation arrives
Policy gate
ALLOW / ASK / BLOCK
Execute
Mock workflow runs it
Verify
Read real database state
Audit
Save the full record
If BLOCKED
Stops before execution. Nothing changes.
If ALLOWED
Can still fail, so we always verify.

=== [SLIDE 10] ===
SPEAKER NOTES: Three decisions. The risk score helps explain, but permission rules have the final word.
PermissionOS: how decisions are made
Deterministic rules, not guesses
10
SentinelAI
ALLOW
Proceed with the action
ASK
Pause for approval
BLOCK
Stop before execution
What it checks
Commands, files and network use
Secrets and data leaks
Prompt-injection signs
Invoice rules: negative amount, restricted vendor
Risk score (0–100)
Adds up severity and context, and is explainable. It raises scrutiny but never overrides a hard denial. Rules live in a YAML policy file.

=== [SLIDE 11] ===
SPEAKER NOTES: Three possible verdicts. If we cannot check, we say inconclusive, never success. Audit log is tamper-evident.
WorkflowProof and the audit trail
Example: “Update invoice INV-1001 to Approved”
11
SentinelAI
VERIFIED
Database shows Approved
FAILED
Database still shows Pending
INCONCLUSIVE
Database unavailable, cannot tell
Unsure is never treated as success.
Audit trail
Each event is linked to the last using SHA-256 hashes
Changing a record breaks the chain, so tampering is visible
Sensitive values are scrubbed

=== [SLIDE 12] ===
SPEAKER NOTES: Same inputs and same starting database for every baseline. Inconclusive is never counted as verified.
Methodology: a fair comparison
Four setups, same 12 test scenarios, same starting data
12
SentinelAI
A
Agent self-report
Trust what the agent says
B
Tool response
Trust the API status
C
WorkflowProof only
Check the result afterward
D
Combined SentinelAI
Permission check + result check
Test scenarios
Normal, missing write, rollback, wrong value, partial update, duplicate, timeout, outage, policy-denied.
What we measure
False-success accepted, failures detected, unauthorized actions blocked, inconclusive rate, latency.

=== [SLIDE 13] ===
SPEAKER NOTES: Self-report caught 3 of 7 failures (42.9%); WorkflowProof caught 6 of 7 (85.7%). One false success still got through. These are reported results from a small SQLite run and must be reproduced before calling them validated.
Results from the benchmark report
12 scenarios, 7 of them real failures (preliminary, as reported)
13
SentinelAI
3 of 7 → 6 of 7
failures caught
4 → 1
false successes accepted
11.88 ms
mean verification time
Small test, one setup. Results need re-running from a clean environment.

=== [SLIDE 14] ===
SPEAKER NOTES: Be honest: this is a student prototype in a controlled setting, not a universal security boundary.
Tools used and honest limitations
What we built with, and what it cannot do
14
SentinelAI
Technology stack
Python 3.11 + FastAPI
SQLAlchemy, PostgreSQL / SQLite
React 19 + TypeScript + Vite
YAML policies, Docker Compose
Pytest, Vitest, GitHub Actions
Limitations
Pattern-based detectors can miss new attacks
Only the checked conditions are proven
Hash chain shows tampering, does not prevent it
Extra checks add some delay
Tested only on a simulated invoice demo

=== [SLIDE 15] ===
SPEAKER NOTES: Summarise: two layers, two questions. Thank the audience and open for questions.
Conclusion and next steps
Contribution
Working prototype with a policy gate, state verifier, audit trail and benchmark harness.
Key finding
Checking the real result caught more failures than trusting the agent (6 of 7 vs 3 of 7).
Next steps
Re-run benchmark cleanly, fix report inconsistencies, test more scenarios.
Ask: Is it allowed?  Then check: Did it happen?

```

---

## Master Speaker Notes Reference

| Slide # | Title | Verbatim Speaker Notes |
| :--- | :--- | :--- |
| **Slide 1** | FINAL PROJECT PRESENTATION · B.TECH COMPUTER SCIENCE AND ENGINEERING | Welcome. SentinelAI adds two checks around every AI tool call: one before (is it allowed?) and one after (did it really happen?). |
| **Slide 2** | What we will cover | Four parts: problem, solution, testing, wrap-up. |
| **Slide 3** | Background: AI agents act, not just talk | Chatbots write text. Agents call tools and change real systems, so mistakes have real effects. |
| **Slide 4** | Problem statement | Failure type 1: not permitted. Failure type 2: permitted but did not work. One check cannot cover both. |
| **Slide 5** | Objectives and scope | Everything runs locally on synthetic data. No real money or production systems. |
| **Slide 6** | Existing approaches and what they miss | Each simpler method covers only one half of the problem. |
| **Slide 7** | Our solution: two layers, two questions | PermissionOS before, WorkflowProof after, audit trail throughout. |
| **Slide 8** | System architecture | Core path on top; database, audit and dashboard support it. |
| **Slide 9** | Pipeline: from request to final result | Walk through the five steps. Blocked requests stop early; allowed requests are still verified. |
| **Slide 10** | PermissionOS: how decisions are made | Three decisions. The risk score helps explain, but permission rules have the final word. |
| **Slide 11** | WorkflowProof and the audit trail | Three possible verdicts. If we cannot check, we say inconclusive, never success. Audit log is tamper-evident. |
| **Slide 12** | Methodology: a fair comparison | Same inputs and same starting database for every baseline. Inconclusive is never counted as verified. |
| **Slide 13** | Results from the benchmark report | Self-report caught 3 of 7 failures (42.9%); WorkflowProof caught 6 of 7 (85.7%). One false success still got through. These are reported results from a small SQLite run and must be reproduced before calling them validated. |
| **Slide 14** | Tools used and honest limitations | Be honest: this is a student prototype in a controlled setting, not a universal security boundary. |
| **Slide 15** | Conclusion and next steps | Summarise: two layers, two questions. Thank the audience and open for questions. |

---

## Extracted Media & Asset Inventory

All 13 visual PNG image assets embedded within the presentation were extracted directly from `ppt/media/` to `sentinelai_presentation_extracted/assets/`:

| File Name | Format | Dimensions | Used In Slides | Functional Representation |
| :--- | :--- | :--- | :--- | :--- |
| `image1.png` | PNG (RGBA) | 256 × 256 | Slide 2 (Card 1), Slide 9 (Step 4) | Problem / Verification Icon |
| `image2.png` | PNG (RGBA) | 256 × 256 | Slide 2 (Card 2), Slide 9 (Step 2) | Solution / Policy Gate Icon |
| `image3.png` | PNG (RGBA) | 256 × 256 | Slide 2 (Card 3) | Testing / Benchmark Icon |
| `image4.png` | PNG (RGBA) | 256 × 256 | Slide 2 (Card 4), Slide 15 (Card 3) | Wrap-up / Next Steps Icon |
| `image5.png` | PNG (RGBA) | 256 × 256 | Slide 3 (Card 1), Slide 15 (Card 1) | Chatbot / Contribution Icon |
| `image6.png` | PNG (RGBA) | 256 × 256 | Slide 3 (Card 2) | Tool-Using AI Agent Icon |
| `image7.png` | PNG (RGBA) | 256 × 256 | Slide 4 (Card 1) | Authorization Failure Icon |
| `image8.png` | PNG (RGBA) | 256 × 256 | Slide 4 (Card 2) | Outcome Failure Icon |
| `image9.png` | PNG (RGBA) | 256 × 256 | Slide 7 (Card 1) | PermissionOS Pre-execution Icon |
| `image10.png` | PNG (RGBA) | 256 × 256 | Slide 7 (Card 2), Slide 15 (Card 2) | WorkflowProof Post-execution / Key Finding Icon |
| `image11.png` | PNG (RGBA) | 256 × 256 | Slide 9 (Step 1) | Pipeline Request Icon |
| `image12.png` | PNG (RGBA) | 256 × 256 | Slide 9 (Step 3) | Pipeline Execute Icon |
| `image13.png` | PNG (RGBA) | 256 × 256 | Slide 9 (Step 5) | Pipeline Audit Icon |