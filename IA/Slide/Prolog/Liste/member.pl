% Appartenenza ad una lista

membro(A,[A|_]).

membro(A,[_|C]) :-
	membro(A,C).