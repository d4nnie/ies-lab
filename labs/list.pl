/* Print list. */

printls_([]) :- !.
printls_(List) :-
    List = [Head | Tail],
    write(', '),
    write(Head),
    printls_(Tail).
printls(List) :-
    write('['),
    List = [Head | Tail],
    write(Head),
    printls_(Tail),
    write(']').

/* Find element in list. */

contains_(_, Element, Element) :- !.
contains_(List, Element, _) :-
    List = [Head | Tail],
    contains_(Tail, Element, Head).
contains(List, Element) :-
    List = [Head | Tail],
    contains_(Tail, Element, Head).

/* Push element in list beginning. */

push(List, Element, New) :-
    New = [Element | List].

/* Pop element from list beginning. */

pop(List, New) :-
    List = [_ | Tail],
    New = Tail.

/* Concatenate lists. */

add_([], Right, Right) :- !.
add_(Left, Right, New) :-
    Left = [Head | Tail],
    push(Right, Head, What),
    add_(Tail, What, New).
add(Left, Right, New) :-
    reverse(Left, What),
    add_(What, Right, New).

/* Delete all elements equals Element. */

deleteall([], Next, Next, []).
deleteall([], Next, _, [Next]).
deleteall(List, Current, Current, New) :-
    List = [Next | Tail],
    deleteall(Tail, Next, Current, New).
deleteall(List, Current, Element, New) :-
    List = [Next | Tail],
    deleteall(Tail, Next, Element, What),
    push(What, Current, New).
deleteall(List, Element, New) :-
    List = [Head | Tail],
    deleteall(Tail, Head, Element, New).

/* Cast list to set. */

set([], []).
set([Head | Tail], X) :-
    contains(Tail, Head), !,
    set(Tail, X).
set([Head | Tail], [Head | X]) :- set(Tail, X).

/* Union of two sets. */

union(Left, Right, New) :-
    add(Left, Right, What),
    set(What, New).

/* Intersection of two sets. */

intersection([], _, []).
intersection([Head | Tail], List, [Head | X]) :-
    contains(List, Head),
    intersection(Tail, List, X).
intersection([_ | Tail], List, X) :-
    intersection(Tail, List, X).

