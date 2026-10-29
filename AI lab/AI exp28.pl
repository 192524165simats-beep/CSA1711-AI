
symptom(fever, high_temperature).
symptom(cold, sneezing).
symptom(flu, fever).
symptom(flu, cough).

diagnosis(patient1, flu) :-
    has_symptom(patient1, fever),
    has_symptom(patient1, cough).

has_symptom(patient1, fever).
has_symptom(patient1, cough).
