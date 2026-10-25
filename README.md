# Government Scheme Advisor

A web-based expert system that helps users discover potentially relevant government scheme information based on their circumstances.

## Project Overview

The Government Scheme Advisor combines **Prolog-based rule matching** with a **Flask web application** to provide preliminary scheme recommendations.

Users answer questions about their education, income, farming status, and employment situation. The system applies Prolog rules to identify potentially relevant scheme information and displays official information links.

## Features

- Interactive eligibility questionnaire
- Rule-based inference using Prolog
- Python Flask web dashboard
- Central Government and Andhra Pradesh scheme information
- Links to official government portals
- Clear notice that matches are not official eligibility decisions

## Technologies Used

- Python
- Flask
- SWI-Prolog
- PySwip
- HTML and CSS
- Docker
- Render for deployment

## Scheme Information Sources

The current prototype includes links to:

- National Scholarship Portal: https://scholarships.gov.in/
- PM-KISAN: https://www.pmkisan.gov.in/
- Andhra Pradesh Agriculture Department: https://apagrisnet.gov.in/
- Andhra Pradesh JnanaBhumi portal: https://jnanabhumi.ap.gov.in/
- Skill India Digital Hub: https://www.skillindiadigital.gov.in/

These links provide official information. The application does not automatically retrieve live scheme records from these websites.

## How It Works

1. The user completes the questionnaire.
2. Flask collects the submitted answers.
3. PySwip connects the Python application to the Prolog engine.
4. Prolog evaluates the rules defined in `schemes.pl`.
5. The application displays potential matches and their information links.

## Project Structure

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

## Running the Project

The recommended deployment uses Docker with SWI-Prolog installed inside the container.

To run locally, install Python, SWI-Prolog, and the dependencies listed in `requirements.txt`, then run:

```bash
pip install -r requirements.txt
python app.py
```

Open the local URL printed by Flask in your browser.

## Limitations

- Results are preliminary matches based on simplified, manually defined rules.
- The prototype does not verify every official eligibility condition.
- Government scheme information, application windows, and requirements can change.
- The application does not make official eligibility decisions or submit applications.
- Users should verify details on the linked government portals.

## Disclaimer

This is an educational project and is not an official government service. Scheme matches should not be treated as confirmation of eligibility.
