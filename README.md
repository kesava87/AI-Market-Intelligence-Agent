# 🚀 AI Market Intelligence Agent

An AI-powered Market Intelligence Platform that automatically collects AI-related news and GitHub repositories, generates AI summaries, performs trend analysis, creates an interactive HTML dashboard, and emails daily reports.

---

## 📌 Features

- 📰 Collects latest AI news automatically
- 💻 Fetches trending AI GitHub repositories
- 🤖 Generates AI-powered summaries using Ollama
- 📊 Performs AI market trend analysis
- 📈 Creates an interactive HTML dashboard
- 📧 Sends automated email reports
- ⏰ Supports Windows Task Scheduler automation
- 🗄 Stores collected data in SQLite

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| SQLite | Database |
| Ollama | AI Summarization |
| Jinja2 | HTML Templates |
| HTML/CSS/JavaScript | Dashboard |
| SMTP | Email Reports |
| Windows Task Scheduler | Automation |

---

## 📂 Project Structure

```text
AI-Market-Intelligence-Agent/
│
├── analyzer/
├── collectors/
├── database/
├── models/
├── processors/
├── reports/
│   ├── output/
│   ├── static/
│   └── templates/
│
├── config.py
├── email_sender.py
├── main.py
├── requirements.txt
├── run_agent.bat
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/kesava87/AI-Market-Intelligence-Agent.git
```

### Go to the project

```bash
cd AI-Market-Intelligence-Agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure

Update your configuration in:

```
config.py
```

### Run

```bash
python main.py
```

---

## 📊 Workflow

```text
AI News Sources
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
SQLite Database
        │
        ▼
AI Summarization (Ollama)
        │
        ▼
Trend Analysis
        │
        ▼
HTML Dashboard
        │
        ▼
Email Report
```

---

## 📷 Screenshots

Coming Soon

---

## 🚀 Future Enhancements

- PDF Report Generation
- Web Dashboard
- Live Charts
- User Authentication
- Cloud Deployment
- REST API
- Docker Support
- Azure Deployment

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kesava Reddy**

GitHub: https://github.com/kesava87