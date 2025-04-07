# AETHER - Automated API Vulnerability Scanner

**AETHER** is a powerful, automated API vulnerability scanner built to identify OWASP Top 10 API security issues. Designed for security researchers, developers, and DevSecOps engineers, AETHER makes it easy to detect vulnerabilities in REST APIs through an interactive dashboard, deep scan logic, and modular architecture.

---

## 🚀 Features

- ✅ **OWASP Top 10 API Vulnerability Detection**:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Broken Authentication
  - CORS Misconfiguration
  - CSRF
  - CRLF Injection
  - Server-Side Request Forgery (SSRF)
  - XML External Entity (XXE)
  - Rate Limiting Issues
  - Missing Security Headers

- 📊 **Interactive Dashboard**:
  - Scan APIs in real time
  - Check scan status (`Completed` / `In Progress`)
  - Download full PDF reports

- 📁 **Scan Input Modes**:
  - Raw API Endpoint (via form or cURL)
  - Postman Collection File Upload

- 📦 **MongoDB Integration** for storing scan results
- 🧰 **Celery Queue** to handle async tasks
- 🧾 **ReportLab PDF Generator** for exportable scan summaries
- 🔁 **Re-scan Support** with previous results reuse

---

## 🧪 How It Works

1. User submits a new API scan with method, headers, and optional body.
2. A unique `scanid` is generated for this scan.
3. Each vulnerability module (XSS, SQLi, CORS, etc.) is triggered asynchronously via Celery workers.
4. Vulnerabilities are stored in MongoDB (`scanids`, `vulnerabilities`).
5. Frontend periodically fetches scan status and renders results.
6. Reports can be exported to PDF, per scan.

---

## 🛠️ Installation

### 📋 Requirements

- Python 3.8+
- MongoDB
- Redis (for Celery background tasks)
- [Optional] `sqlmapapi.py` for SQLi detection
- [Optional] `ssrfmap` for SSRF detection
- Linux-based system (recommended for full SSRF simulation)
- Postman (for collection scan feature)

---

## 📦 Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/AETHER.git
cd AETHER

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Ensure MongoDB and Redis are running
# (adjust based on OS and install method)

# 5. Start the backend Flask server
cd API
python3 app.py

#6. You can now access the dashboard at:
http://localhost:8094
