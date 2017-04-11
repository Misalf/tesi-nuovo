% Verifica che un oggetto non appartenga ad una lista

membro(A,[A|_]).

membro(A,[_|C]) :-
	membro(A,C).

notmembro(A,C):-
	not(membro(A,C)).