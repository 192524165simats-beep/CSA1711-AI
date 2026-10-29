
fact(a).
fact(b).

rule(c) :- fact(a), fact(b).
rule(d) :- rule(c).

backward(X) :- fact(X).
backward(X) :- rule(X).
