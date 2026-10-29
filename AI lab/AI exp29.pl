:- dynamic fact/1.

fact(a).
fact(b).

rule(c) :- fact(a), fact(b).
rule(d) :- fact(c).

forward :-
    (rule(c), \+ fact(c) -> assertz(fact(c)) ; true),
    (rule(d), \+ fact(d) -> assertz(fact(d)) ; true).