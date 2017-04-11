% Lunghezza di una lista

lungh([],0).

lungh([_|C],N1) :-
	lungh(C,N),
	N1 is N + 1.