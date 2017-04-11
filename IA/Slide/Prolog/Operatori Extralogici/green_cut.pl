% Appartenenza ad una lista con cut verde

membro(A,[A|_]) :- !.

membro(A,[_|C]) :-
	membro(A,C).