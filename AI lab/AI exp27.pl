
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 2).
edge(c, d, 1).

heuristic(a, 4).
heuristic(b, 2).
heuristic(c, 1).
heuristic(d, 0).

best_first(Start, Goal) :-
    heuristic(Start, H),
    search([(H, Start)], Goal, []).

search([(_, Goal)|_], Goal, _) :-
    write('Goal reached: '), write(Goal), nl.

search([(_, Node)|Rest], Goal, Visited) :-
    findall((H, Next),
        (edge(Node, Next, _),
         \+ member(Next, Visited),
         heuristic(Next, H)),
        Children),
    append(Rest, Children, NewList),
    sort(NewList, Sorted),
    search(Sorted, Goal, [Node|Visited]).
