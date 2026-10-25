
% Government Scheme Advisor
% Educational prototype: results are preliminary matches, not
% official eligibility decisions. Verify all conditions on official sites.

:- dynamic student/1.
:- dynamic low_income/1.
:- dynamic farmer/1.
:- dynamic owns_farmland/1.
:- dynamic unemployed/1.
:- dynamic seeking_skill_training/1.

% Scheme records:
% scheme_info(ID, Name, Category, Government, OfficialURL).

scheme_info(
    student_scholarship,
    'National Scholarship Portal',
    education,
    central,
    'https://scholarships.gov.in/'
).

scheme_info(
    pm_kisan,
    'PM-KISAN',
    agriculture,
    central,
    'https://www.pmkisan.gov.in/'
).

scheme_info(
    ap_agriculture_directory,
    'Andhra Pradesh Agriculture Scheme Directory',
    agriculture,
    andhra_pradesh,
    'https://apagrisnet.gov.in/'
).

scheme_info(
    skill_india,
    'Skill India Digital Hub',
    employment,
    central,
    'https://www.skillindiadigital.gov.in/'
).

% Preliminary matching rules.
% These rules do NOT replace each scheme's official eligibility criteria.

possible_match(Person, student_scholarship) :-
    student(Person).

possible_match(Person, pm_kisan) :-
    farmer(Person),
    owns_farmland(Person).

possible_match(Person, ap_agriculture_directory) :-
    farmer(Person).

possible_match(Person, skill_india) :-
    unemployed(Person),
    seeking_skill_training(Person).
