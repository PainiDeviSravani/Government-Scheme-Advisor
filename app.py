
from flask import Flask, render_template, request
from pyswip import Prolog
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_FILE = os.path.join(BASE_DIR, "schemes.pl")

SCHEME_NAMES = {
    "student_support": "Student Support Scheme",
    "farmer_support": "Farmer Support Scheme",
    "skill_training": "Skill Training Scheme",
}

PREDICATES = [
    "student",
    "low_income",
    "farmer",
    "owns_farmland",
    "unemployed",
    "seeking_skill_training",
]


def check_eligibility(applicant):
    prolog = Prolog()
    prolog.consult(RULES_FILE)

    person = "applicant"

    answers = {
        "student": applicant.get("student") == "yes",
        "low_income": applicant.get("low_income") == "yes",
        "farmer": applicant.get("farmer") == "yes",
        "owns_farmland": applicant.get("owns_farmland") == "yes",
        "unemployed": applicant.get("unemployed") == "yes",
        "seeking_skill_training":
            applicant.get("seeking_skill_training") == "yes",
    }

    # Remove any previous facts for this applicant.
    for predicate in PREDICATES:
        list(prolog.query(
            f"retractall({predicate}({person}))"
        ))

    try:
        # Add facts based on the submitted form.
        for predicate, answer in answers.items():
            if answer:
                prolog.assertz(f"{predicate}({person})")

        # Ask Prolog which schemes match.
        results = list(
            prolog.query(f"eligible({person}, Scheme)")
        )

        return [
            SCHEME_NAMES.get(
                str(result["Scheme"]),
                str(result["Scheme"])
            )
            for result in results
        ]

    finally:
        # Clean up applicant facts after the query.
        for predicate in PREDICATES:
            list(prolog.query(
                f"retractall({predicate}({person}))"
            ))


@app.route("/", methods=["GET", "POST"])
def home():
    matches = []
    checked = False
    error = None

    if request.method == "POST":
        checked = True

        applicant = {
            field: request.form.get(field, "no")
            for field in PREDICATES
        }

        try:
            matches = check_eligibility(applicant)
        except Exception:
            app.logger.exception("Eligibility check failed")
            error = (
                "The eligibility engine could not run. "
                "Please check the Prolog configuration."
            )

    return render_template(
        "index.html",
        matches=matches,
        checked=checked,
        error=error,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
