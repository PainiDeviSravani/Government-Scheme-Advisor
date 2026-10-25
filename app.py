
from flask import Flask, render_template, request
from pyswip import Prolog
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_FILE = os.path.join(BASE_DIR, "schemes.pl")

PREDICATES = [
    "student",
    "low_income",
    "farmer",
    "owns_farmland",
    "unemployed",
    "seeking_skill_training",
]


def check_eligibility(answers):
    prolog = Prolog()
    prolog.consult(RULES_FILE)

    person = "applicant"

    # Convert the submitted form answers into Prolog facts.
    facts = {
        field: answers.get(field, "no") == "yes"
        for field in PREDICATES
    }

    try:
        # Clear any old facts for this applicant.
        for predicate in PREDICATES:
            
          list(prolog.query(f"retractall({predicate}({person}))"))


        # Add facts for answers marked Yes.
        for predicate, answer in facts.items():
            if answer:
                prolog.assertz(f"{predicate}({person})")

        # Read scheme records from schemes.pl.
        records = list(prolog.query(
            "scheme_info(ID, Name, Category, Government, URL)"
        ))

        scheme_data = {}
        for record in records:
            scheme_id = str(record["ID"])
            scheme_data[scheme_id] = {
                "name": str(record["Name"]),
                "category": str(record["Category"]).replace("_", " ").title(),
                "government": str(record["Government"]).replace("_", " ").title(),
                "url": str(record["URL"]),
            }

        # Ask Prolog to identify potential matches.
        matches = list(prolog.query(
            f"possible_match({person}, SchemeID)"
        ))

        matched_schemes = []
        for result in matches:
            scheme_id = str(result["SchemeID"])
            if scheme_id in scheme_data:
                matched_schemes.append(scheme_data[scheme_id])

        return matched_schemes

    finally:
        # Remove temporary applicant facts.
        for predicate in PREDICATES:
            
          list(prolog.query(f"retractall({predicate}({person}))"))


@app.route("/", methods=["GET", "POST"])
def home():
    matches = []
    checked = False
    error = None

    if request.method == "POST":
        checked = True
        answers = {
            field: request.form.get(field, "no")
            for field in PREDICATES
        }

        try:
            matches = check_eligibility(answers)
        except Exception:
            app.logger.exception("Scheme matching failed")
            error = (
                "Unable to check schemes right now. "
                "Please try again later."
            )

    return render_template(
        "index.html",
        matches=matches,
        checked=checked,
        error=error,
    )


@app.route("/healthz")
def health_check():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
