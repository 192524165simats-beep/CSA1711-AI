
diet(fever, 'Drink plenty of water and eat light food').
diet(diabetes, 'Eat vegetables and avoid sugar').
diet(obesity, 'Eat fruits and avoid fatty food').
diet(anemia, 'Eat iron-rich foods').

suggest_diet(Disease) :-
    diet(Disease, Food),
    write('Suggested diet: '),
    write(Food), nl.
