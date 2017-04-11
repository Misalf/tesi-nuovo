%facts
coll1(na,rm,220).
coll1(rm,fi,200).
coll1(fi,bo,100).
coll1(na,sa,60).
coll1(sa,rm,280).


%rules
coll(X,Y,C) :-
	coll1(X,Y,C).

coll(X,Y,C) :-
	coll1(Y,X,C).

