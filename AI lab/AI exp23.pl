
parent(ravi, arun).
parent(ravi, priya).
parent(arun, kumar).
parent(priya, meena).

father(X, Y) :- parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
