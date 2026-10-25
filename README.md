# Government Scheme Eligibility Expert System

## 📌 Project Overview

The **Government Scheme Eligibility Expert System** is a rule-based application designed to demonstrate how users can identify government schemes that may match their personal circumstances.

The application uses **Prolog** to evaluate eligibility rules and a **Flask web dashboard** to collect user responses and display matching sample schemes.

## 🎯 Objectives

- Demonstrate rule-based reasoning using Prolog.
- Build a simple and user-friendly web dashboard.
- Connect Python and Prolog using PySwip.
- Display scheme matches based on applicant responses.
- Explore how expert systems can support access to public services.

## ✨ Features

- Interactive eligibility questionnaire.
- Rule-based inference using Prolog.
- Automatic matching against sample eligibility rules.
- Results displayed through a Flask dashboard.
- Container-based deployment configuration using Docker.

## 🛠️ Technologies Used

- **Python** — application logic
- **Flask** — web application framework
- **Prolog / SWI-Prolog** — inference engine and eligibility rules
- **PySwip** — Python-to-Prolog integration
- **HTML and CSS** — dashboard interface
- **Docker** — deployment environment
- **GitHub** — source code hosting
- **Render** — planned cloud deployment

## 📂 Project Structure

```text
Government-Scheme-Advisor/
├── app.py
├── schemes.pl
├── requirements.txt
├── Dockerfile
├── README.md
└── templates/
    └── index.html
```

## ⚙️ How It Works

1. The user answers questions about their circumstances.
2. Flask receives the submitted responses.
3. Python passes the relevant facts to the Prolog inference engine.
4. Prolog evaluates the eligibility rules.
5. The dashboard displays the matching sample schemes.

## 🧪 Sample Rules

The current prototype demonstrates three example rules:

- **Student Support Scheme:** student and low-income conditions are both met.
- **Farmer Support Scheme:** farmer and farmland-ownership conditions are both met.
- **Skill Training Scheme:** unemployment and skill-training conditions are both met.

These are illustrative rules for demonstrating the expert-system approach, not verified official government scheme criteria.

## 🚀 Running the Project

### Option 1: Using Docker

Install Docker Desktop, then open a terminal in the project directory and run:

```bash
docker build -t government-scheme-advisor .
docker run -p 10000:10000 -e PORT=10000 government-scheme-advisor
```

Open `http://localhost:10000` in your browser.

### Option 2: Using Python and SWI-Prolog

Install Python and SWI-Prolog, then install the Python dependencies:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.

## ☁️ Deployment

The project includes a Dockerfile intended for deployment
