%facts
coll(na,rm).
coll(na,rc).
coll(rm,ba).
coll(ba,rc).

%rules
coll(X,Y) :-
	coll(Y,X).
