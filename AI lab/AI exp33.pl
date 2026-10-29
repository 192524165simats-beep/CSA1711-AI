
count_vowels([], 0).

count_vowels([H|T], N) :-
    count_vowels(T, N1),
    (member(H, [a,e,i,o,u]) ->
        N is N1 + 1 ;
        N is N1).
