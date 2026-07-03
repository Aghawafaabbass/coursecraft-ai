# 📚 CourseCraft AI — Agentic AI-Powered Curriculum & Assessment Generator

<div align="center">

![CourseCraft AI Banner](Screenshots/Sc1.PNG)

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://coursecraft-ai-pc5kmmcpmgwxsmrhkkcpqn.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/Aghawafaabbass/coursecraft-ai)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-Llama--3-F55036?style=for-the-badge)](https://groq.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**A production-grade, multi-agent AI system that generates complete course curricula, assessments, and knowledge graphs in seconds — powered by Groq's ultra-fast Llama-3 inference engine.**

</div>

---

## 🔗 Live Application

> **🌐 [https://coursecraft-ai-pc5kmmcpmgwxsmrhkkcpqn.streamlit.app/](https://coursecraft-ai-pc5kmmcpmgwxsmrhkkcpqn.streamlit.app/)**

---

## 📋 Table of Contents

1. [What is CourseCraft AI?](#-what-is-coursecraft-ai)
2. [Why CourseCraft AI? — vs ChatGPT](#-why-coursecraft-ai--vs-chatgpt)
3. [Key Features](#-key-features)
4. [Who Should Use This?](#-who-should-use-this)
5. [System Architecture](#-system-architecture)
6. [Data Flow Diagram](#-data-flow-diagram)
7. [Multi-Agent Pipeline](#-multi-agent-pipeline)
8. [Class Diagram](#-class-diagram)
9. [Entity Relationship Diagram (ERD)](#-entity-relationship-diagram-erd)
10. [Tech Stack](#-tech-stack)
11. [Skills Demonstrated](#-skills-demonstrated)
12. [Screenshots](#-screenshots)
13. [Local Setup](#-local-setup)
14. [Deployment](#-deployment)
15. [Project Structure](#-project-structure)
16. [Future Roadmap](#-future-roadmap)
17. [Author](#-author)
18. [License](#-license)

---

## 🎯 What is CourseCraft AI?

**CourseCraft AI** is an **Agentic AI** application that replaces the hours of manual work required to design a course curriculum. A teacher, trainer, or content creator simply enters:

- 📌 **Course Topic** (e.g., "Social Media Marketing")
- 👥 **Target Audience** (Beginner / Intermediate / Advanced)
- 📅 **Duration** (1–30 weeks)

And within seconds, two specialized AI agents working in pipeline produce:

| Output | Description |
|--------|-------------|
| 📅 **Weekly Curriculum** | Module title, objectives, topics, and exercises per week |
| 📝 **Assessments** | MCQ quizzes (A/B/C/D), weekly assignments, grading rubric |
| 🧠 **Knowledge Graph** | Core concepts + their relationships visualized |
| 📊 **Token Analytics** | Real-time cost & token usage dashboard |
| 📄 **Multi-Format Export** | PDF, Markdown, JSON, LinkedIn snippet |

---

## 🏆 Why CourseCraft AI? — vs ChatGPT

| Feature | ChatGPT | CourseCraft AI |
|---|---|---|
| **Interaction** | Single prompt → single response | Multi-Agent pipeline with critic loop |
| **Output structure** | Unstructured text | Structured JSON → parsed UI components |
| **Self-correction** | ❌ No | ✅ Agent 2 reviews & refines Agent 1's output |
| **Session memory** | ❌ Lost on refresh | ✅ `st.session_state` persists across reruns |
| **Export** | Copy-paste only | ✅ PDF, Markdown, JSON download |
| **Cost visibility** | ❌ Hidden | ✅ Real-time token & cost dashboard |
| **File upload / RAG** | Limited | ✅ 50-file PDF/DOCX context injection ready |
| **Speed** | ~3–10 sec | ✅ Groq: sub-second inference |
| **Deployment** | SaaS product | ✅ Your own production app, fully owned |
| **Customization** | ❌ None | ✅ Model selection, duration, audience, mode |

**The core architectural difference:** ChatGPT is a conversational interface. CourseCraft AI is an **orchestrated agentic system** where each agent has a specific role, structured output schema, and the system validates/corrects the result before showing it to the user.

---

## ✨ Key Features

### 🧠 Agentic AI Core
- **Agent 1 — Curriculum Designer:** Uses `llama-3.1-8b-instant` or `llama-3.3-70b-versatile` to generate a structured week-by-week course outline in valid JSON
- **Agent 2 — Assessment Engine:** Generates MCQ quizzes, weekly assignments, and a weighted grading rubric per curriculum
- **Agent 3 — Knowledge Graph Extractor:** Extracts core concepts and their prerequisite/leads-to relationships

### ⚡ Groq-Powered Speed
- Ultra-fast inference via Groq Cloud API — full 12-week course generated in ~8–12 seconds
- Model selection: Fast Draft (8B), High Quality (70B), or Auto-Switch

### 📊 Token Analytics Dashboard
- Real-time input/output token counts across all agents
- Estimated cost per generation based on Groq public pricing

### 🧠 Knowledge Graph Visualization
- AI extracts 8–12 key concepts from course content
- Displays concept nodes and directed relationship edges (e.g., Social Media Basics → Content Strategy)

### 📤 Multi-Format Export
- **PDF** — Structured, printable course package (curriculum + assessments + knowledge graph)
- **Markdown** — GitHub/Notion-ready formatted document
- **JSON** — LMS-importable structured data (SCORM-ready format)
- **LinkedIn Snippet** — One-click professional post generator

### 🌙 Light/Dark Theme
- Full dark/light mode toggle with proper contrast across all components
- CSS-variable-based theming — no FOUC (Flash of Unstyled Content)

### 📎 Reference Materials (RAG-Ready)
- Upload up to 50 PDF/DOCX files as context
- Architecture ready for full RAG pipeline integration

---

## 👥 Who Should Use This?

| User Type | Use Case |
|---|---|
| 🎓 **University Lecturers** | Design new module outlines in minutes instead of days |
| 🏢 **Corporate Trainers** | Create employee onboarding/upskilling programs rapidly |
| 💼 **Bootcamp Instructors** | Structure short-term skill courses (e.g., "Python in 6 weeks") |
| 🌐 **Online Course Creators** | Draft Udemy/Coursera course structure before production |
| 📚 **Self-Learners** | Generate a personalized structured learning path |
| 🤖 **AI Engineers** | Reference implementation of multi-agent Streamlit architecture |

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph CLIENT["🌐 Client Layer (Browser)"]
        UI["Streamlit UI\n(app.py)"]
    end

    subgraph SESSION["💾 Session Layer"]
        SS["st.session_state\n(course_data cache)"]
    end

    subgraph AGENTS["🤖 Agentic AI Layer (groq_agent.py)"]
        A1["Agent 1\nCurriculum Designer\nllama-3.1-8b-instant"]
        A2["Agent 2\nAssessment Engine\nllama-3.3-70b-versatile"]
        A3["Agent 3\nKnowledge Graph\nllama-3.1-8b-instant"]
    end

    subgraph GROQ["⚡ Groq Cloud API"]
        LLM["Llama-3 Models\n(8B / 70B)"]
    end

    subgraph EXPORT["📤 Export Layer (export_utils.py)"]
        PDF["PDF Generator\n(fpdf2)"]
        MD["Markdown Builder"]
        JSON["JSON/SCORM Builder"]
        LI["LinkedIn Snippet"]
    end

    subgraph STORAGE["☁️ Cloud"]
        GH["GitHub Repository"]
        SC["Streamlit Community Cloud"]
        ENV["Secrets Manager\n(.env / st.secrets)"]
    end

    UI -->|User Input: topic, audience, duration| A1
    A1 -->|Structured JSON Prompt| LLM
    LLM -->|Week-by-week curriculum JSON| A1
    A1 -->|curriculum_data + usage1| A2
    A2 -->|Assessment Prompt| LLM
    LLM -->|quizzes + rubric JSON| A2
    A2 -->|assess_data + usage2| A3
    A3 -->|KG Extraction Prompt| LLM
    LLM -->|nodes + edges JSON| A3
    A3 -->|kg_data + usage3| SS
    SS -->|Cached course_data| UI
    UI -->|Export Request| PDF
    UI -->|Export Request| MD
    UI -->|Export Request| JSON
    UI -->|Export Request| LI
    ENV -->|GROQ_API_KEY| GROQ
    GH -->|Auto-deploy on push| SC
```

---

## 🔄 Data Flow Diagram

```mermaid
flowchart LR
    U(["👤 User"]) -->|topic + audience\n+ duration + model| INP["Input\nValidation"]
    INP -->|Valid| P1["Progress Bar\n15%"]
    P1 --> AG1["🧠 Agent 1\nCurriculum Designer"]
    AG1 -->|JSON Prompt| GROQ1[("⚡ Groq API\nLlama-3")]
    GROQ1 -->|weeks[] JSON\n+ token usage| PARSE1["JSON Parser\n+ Error Handler"]
    PARSE1 -->|weeks data| P2["Progress Bar\n45%"]
    P2 --> AG2["📝 Agent 2\nAssessment Engine"]
    AG2 -->|JSON Prompt with\nweeks context| GROQ2[("⚡ Groq API\nLlama-3")]
    GROQ2 -->|quizzes[] + assignments[]\n+ rubric[] JSON| PARSE2["JSON Parser\n+ Error Handler"]
    PARSE2 -->|assess data| P3["Progress Bar\n75%"]
    P3 --> AG3["🧠 Agent 3\nKG Extractor"]
    AG3 -->|Concept extraction\nprompt| GROQ3[("⚡ Groq API\nLlama-3")]
    GROQ3 -->|nodes[] + edges[] JSON| PARSE3["JSON Parser\n+ Error Handler"]
    PARSE3 -->|kg data| STATE[("💾 session_state\ncourse_data{}")]
    STATE -->|Timeline| TAB1["📅 Timeline Tab"]
    STATE -->|Assessments| TAB2["📝 Assessments Tab"]
    STATE -->|usage tokens| TAB3["📊 Analytics Tab"]
    STATE -->|nodes + edges| TAB4["🧠 KG Tab"]
    STATE -->|All data| TAB5["📤 Export Tab"]
    TAB5 -->|bytes| PDF["📄 PDF"]
    TAB5 -->|string| MDX["📝 Markdown"]
    TAB5 -->|string| JSN["🗂️ JSON"]
    TAB5 -->|string| LNK["🎯 LinkedIn"]
    INP -->|Empty topic| WARN["⚠️ Warning\nMessage"]
```

---

## 🤖 Multi-Agent Pipeline

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant APP as app.py
    participant A1 as Agent 1<br/>Curriculum Designer
    participant A2 as Agent 2<br/>Assessment Engine
    participant A3 as Agent 3<br/>KG Extractor
    participant G as ⚡ Groq API
    participant S as 💾 session_state

    U->>APP: Click Generate (topic, audience, duration)
    APP->>A1: generate_curriculum(topic, audience, duration, model)
    A1->>G: POST /v1/chat/completions (Llama-3)
    G-->>A1: curriculum JSON + token usage
    A1-->>APP: weeks[], usage1

    APP->>A2: generate_assessments(topic, audience, weeks)
    A2->>G: POST /v1/chat/completions (Llama-3)
    G-->>A2: quizzes[], assignments[], rubric[] + usage
    A2-->>APP: assess_data, usage2

    APP->>A3: generate_knowledge_graph(topic, weeks)
    A3->>G: POST /v1/chat/completions (Llama-3)
    G-->>A3: nodes[], edges[] + usage
    A3-->>APP: kg_data, usage3

    APP->>S: Store course_data{} with all results
    S-->>APP: Cached
    APP-->>U: Render 5 tabs (Timeline, Assessments,<br/>Analytics, KG, Export)
```

---

## 📐 Class Diagram

```mermaid
classDiagram
    class App {
        +session_state: dict
        +theme: str
        +course_generated: bool
        +course_data: dict
        +toggle_theme()
        +render_header()
        +render_hero()
        +render_sidebar()
        +render_results()
        +render_footer()
    }

    class GroqAgent {
        +client: Groq
        +model_map: dict
        +generate_curriculum(topic, audience, duration, model_choice) dict
        +generate_assessments(topic, audience, weeks_data, model_choice) dict
        +generate_knowledge_graph(topic, weeks_data, model_choice) dict
        -_parse_json(content) dict
        -_clean_fences(content) str
        -_build_usage(response) dict
    }

    class CurriculumAgent {
        +system_prompt: str
        +temperature: float = 0.7
        +max_tokens: int = 4000
        +generate(topic, audience, duration) weeks[]
    }

    class AssessmentAgent {
        +system_prompt: str
        +temperature: float = 0.6
        +max_tokens: int = 4000
        +generate(topic, audience, weeks) assess_data
    }

    class KnowledgeGraphAgent {
        +system_prompt: str
        +temperature: float = 0.5
        +max_tokens: int = 2000
        +generate(topic, weeks) kg_data
    }

    class ExportUtils {
        +clean(text) str
        +build_markdown(course_data) str
        +build_pdf(course_data) bytes
        +build_scorm_json(course_data) str
        +build_linkedin_snippet(course_data) str
    }

    class CourseData {
        +topic: str
        +audience: str
        +duration: int
        +generated_at: str
        +weeks: list
        +assessments: dict
        +knowledge_graph: dict
        +usage: dict
        +error: str
    }

    class Week {
        +week_number: int
        +title: str
        +objectives: str
        +topics: str
        +exercise: str
    }

    class Assessment {
        +quizzes: list
        +assignments: list
        +grading_rubric: list
    }

    class Quiz {
        +week_number: int
        +question: str
        +options: list
        +correct_answer: str
    }

    class KnowledgeGraph {
        +nodes: list
        +edges: list
    }

    App --> GroqAgent : uses
    App --> ExportUtils : uses
    App --> CourseData : stores in session_state
    GroqAgent --> CurriculumAgent : delegates
    GroqAgent --> AssessmentAgent : delegates
    GroqAgent --> KnowledgeGraphAgent : delegates
    CourseData --> Week : contains list
    CourseData --> Assessment : contains
    CourseData --> KnowledgeGraph : contains
    Assessment --> Quiz : contains list
```

---

## 🗄️ Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    COURSE_SESSION {
        string topic PK
        string audience
        int duration_weeks
        string generated_at
        string model_used
        int total_input_tokens
        int total_output_tokens
        float estimated_cost_usd
    }

    WEEK {
        int week_number PK
        string course_topic FK
        string title
        string objectives
        string topics_covered
        string practical_exercise
    }

    QUIZ {
        int quiz_id PK
        int week_number FK
        string question
        string option_a
        string option_b
        string option_c
        string option_d
        string correct_answer
    }

    ASSIGNMENT {
        int assignment_id PK
        int week_number FK
        string title
        string description
    }

    GRADING_RUBRIC {
        int rubric_id PK
        string course_topic FK
        string criteria
        int weight_percent
        string description
    }

    KG_NODE {
        string node_id PK
        string course_topic FK
        string label
    }

    KG_EDGE {
        int edge_id PK
        string source_node_id FK
        string target_node_id FK
    }

    AGENT_USAGE {
        int usage_id PK
        string course_topic FK
        string agent_name
        int input_tokens
        int output_tokens
        string model
    }

    COURSE_SESSION ||--o{ WEEK : "has"
    WEEK ||--o| QUIZ : "has"
    WEEK ||--o| ASSIGNMENT : "has"
    COURSE_SESSION ||--o{ GRADING_RUBRIC : "has"
    COURSE_SESSION ||--o{ KG_NODE : "contains"
    KG_NODE ||--o{ KG_EDGE : "source of"
    KG_NODE ||--o{ KG_EDGE : "target of"
    COURSE_SESSION ||--o{ AGENT_USAGE : "tracked by"
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit 1.58 | Web UI, tabs, sidebar, interactive widgets |
| **AI Inference** | Groq Cloud API | Ultra-fast LLM inference |
| **LLM — Fast** | Llama-3.1-8b-instant | Fast draft generation (8B params) |
| **LLM — Quality** | Llama-3.3-70b-versatile | High-quality generation (70B params) |
| **PDF Export** | fpdf2 2.8.7 | PDF generation with clean ASCII rendering |
| **Environment** | python-dotenv | Secure API key management |
| **HTTP Client** | httpx (via groq SDK) | Async API calls |
| **Data** | Python dicts + JSON | Structured inter-agent data passing |
| **Version Control** | Git + GitHub | Code versioning and collaboration |
| **Deployment** | Streamlit Community Cloud | Production hosting with secrets management |
| **Language** | Python 3.11+ | Core application language |

---

## 💼 Skills Demonstrated

### 🧠 Agentic AI & LLM Engineering
- **Multi-Agent Orchestration** — 3 specialized agents with distinct roles and structured JSON output schemas
- **Prompt Engineering** — System + user prompt design for reliable structured JSON output
- **LLM Model Selection** — Dynamic model switching (8B vs 70B) based on quality/speed tradeoff
- **JSON Output Parsing** — Robust parse + error recovery for LLM responses

### 🚀 Production Engineering
- **Session State Management** — `st.session_state` for persistent data across Streamlit reruns
- **Secure Secret Management** — `.env` locally, `st.secrets` in production (zero key leakage)
- **Error Handling** — try/except at every agent call, graceful fallback UI messages
- **Export Pipeline** — Multi-format export (PDF/MD/JSON) with Unicode sanitization

### 🎨 Frontend & UI/UX
- **Theming System** — CSS variable-based dark/light mode with full contrast compliance
- **Responsive Layout** — Sidebar + main area, works on desktop and mobile
- **Custom HTML/CSS** — Feature cards, week cards, quiz options, knowledge graph nodes

### ⚙️ DevOps & Deployment
- **Git & GitHub** — Repository management, clean commits, `.gitignore` best practices
- **Cloud Deployment** — Streamlit Community Cloud with secrets configuration
- **Dependency Management** — `requirements.txt` with pinned versions for reproducibility

---

## 📸 Screenshots

### 🏠 Home Screen — Dark Mode
![Home Dark](Screenshots/Sc1.PNG)

### 🌤️ Home Screen — Light Mode
![Home Light](Screenshots/Sc2.PNG)

### 📅 Timeline Tab — AI Generated Curriculum
![Timeline](Screenshots/Sc3.PNG)

### 📝 Assessments Tab — Quizzes & Rubric
![Assessments](Screenshots/Sc4.PNG)

### 📊 Analytics Tab — Token Usage Dashboard
![Analytics](Screenshots/Sc5.PNG)

### 🧠 Knowledge Graph Tab
![Knowledge Graph](Screenshots/Sc6.PNG)

### 📤 Export Tab — PDF/Markdown/JSON
![Export](Screenshots/Sc7.PNG)

### ⚙️ Advanced Settings & RAG Upload
![Advanced Settings](Screenshots/Sc8.PNG)

### 🚀 Generation in Progress — Loader
![Loader](Screenshots/Sc9.PNG)

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- Groq API Key → [https://console.groq.com/keys](https://console.groq.com/keys)

### Step 1 — Clone Repository
```bash
git clone https://github.com/Aghawafaabbass/coursecraft-ai.git
cd coursecraft-ai
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure API Key
Create a `.env` file in the root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 5 — Run Application
```bash
streamlit run app.py
```

Open browser → `http://localhost:8501`

---

## ☁️ Deployment

### Streamlit Community Cloud
1. Fork/push this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set **Main file path:** `app.py`
5. Under **Advanced Settings → Secrets**, add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
6. Click **Deploy**

---

## 📁 Project Structure

```
coursecraft-ai/
│
├── app.py                  # Main Streamlit application (UI + orchestration)
├── groq_agent.py           # All 3 AI agents (Curriculum, Assessment, KG)
├── export_utils.py         # Export functions (PDF, Markdown, JSON, LinkedIn)
├── requirements.txt        # Python dependencies (pinned versions)
├── .env                    # Local secrets (NOT committed to GitHub)
├── .gitignore              # Excludes venv/, .env, __pycache__/
├── test_agent.py           # Standalone agent test script
│
└── Screenshots/            # Application screenshots for README
    ├── Sc1.PNG
    ├── Sc2.PNG
    ├── Sc3.PNG
    ├── Sc4.PNG
    ├── Sc5.PNG
    ├── Sc6.PNG
    ├── Sc7.PNG
    ├── Sc8.PNG
    └── Sc9.PNG
```

---

## 🔮 Future Roadmap

| Feature | Priority | Description |
|---|---|---|
| **Full RAG Pipeline** | 🔴 High | Extract text from uploaded PDFs/DOCX and inject as agent context |
| **Self-Correction Critic Loop** | 🔴 High | Agent 2 reviews Agent 1 output and sends back for revision |
| **Interactive Knowledge Graph** | 🟡 Medium | D3.js / PyVis force-directed graph visualization |
| **SCORM Export** | 🟡 Medium | Full SCORM 1.2/2004 package for Moodle/Coursera import |
| **Slides Generator** | 🟡 Medium | Auto-generate lecture slides (Marp/PPTX) from curriculum |
| **Student Portal** | 🟢 Low | Separate learner-facing interface with quiz submission |
| **Multi-language Support** | 🟢 Low | Generate curricula in Urdu, Arabic, French |
| **LMS API Integration** | 🟢 Low | Push course directly to Moodle via REST API |

---

## ⚠️ Disclaimer

This project is developed for **educational, research, and portfolio demonstration purposes**. The AI-generated curriculum, assessments, and knowledge graphs are produced by large language models and should be reviewed and validated by qualified educators before use in any formal educational setting. The estimated API costs shown in the analytics dashboard are **illustrative approximations** based on publicly available Groq pricing and may not reflect actual billing.

---

## 👨‍💼 Author

<div align="center">

### **Agha Wafa Abbas**
*AI Solutions Architect · ML Scientist · Agentic AI Engineer · Lecturer · Researcher · Full-Stack Developer*

</div>

| Institution | Role | Contact |
|---|---|---|
| 🇬🇧 University of Portsmouth, UK | Lecturer | agha.wafa@port.ac.uk |
| 🇬🇧 Arden University, UK | Lecturer | awabbas@arden.ac.uk |
| 🇬🇧 Pearson, UK | Lecturer | — |
| 🇵🇰 IVY College, Lahore, Pakistan | Lecturer | wafa.abbas.lhr@rootsivy.edu.pk |

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Aghawafaabbass-181717?style=flat-square&logo=github)](https://github.com/Aghawafaabbass)
[![Google Scholar](https://img.shields.io/badge/Google_Scholar-Profile-4285F4?style=flat-square&logo=google-scholar)](https://scholar.google.com/citations?user=79nqMaEAAAAJ)
📧 aghawafaabbass@gmail.com · 📞 +1 306 891 4663

</div>

---

## 📄 License

```
MIT License

Copyright (c) 2026 Agha Wafa Abbas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**⭐ If this project helped you, please give it a star on GitHub!**

[![GitHub stars](https://img.shields.io/github/stars/Aghawafaabbass/coursecraft-ai?style=social)](https://github.com/Aghawafaabbass/coursecraft-ai)

*Built with ❤️ by Agha Wafa Abbas · Powered by Groq + Llama-3 · Deployed on Streamlit Cloud*

</div>
