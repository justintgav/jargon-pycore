% Sample prolog statements to est
% running swipl from a subprocess

% Introductory Prolog examples
% N. L. Tinkham

% newmember(?Element, +List)
% Note: member built in to SWI-Prolog

newmember(Element, [Element|_]).
newmember(Element, [_|T]) :- newmember(Element, T).

% sumlist(+List, -Sum)
% Sum is the sum of the elements in List

sumlist([], 0).
sumlist([H|T], Sum) :- sumlist(T, TSum), Sum is H + TSum.

% maxlist(+List, -Biggest)
% Uses max function, built into SWI-Prolog:
% X is max(Y, Z) unifies X with the larger of Y and Z.

maxlist([Big], Big).
maxlist([H|T], Big) :- maxlist(T, TBig), Big is max(H, TBig).

% occurs(+Item, +List, -Count)
% Count is the number of times Item occurs in List.

occurs(_, [], 0).
occurs(Item, [Item|T], Count) :-
	occurs(Item, T, TCount),
		Count is TCount + 1.
		occurs(Item, [H|T], Count) :-
			Item \== H,
				occurs(Item, T, Count).

