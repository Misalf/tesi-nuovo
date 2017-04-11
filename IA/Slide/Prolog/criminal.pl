%facts

missile(m1).
american(west).
owns(nono,m1).
enemy(nono,america).


%rules

weapon(X) :- 
	missile(X).

hostile(X) :- 
	enemy(X,america).

sells(west,X,nono) :- 
	missile(X),
	owns(nono,X).

criminal(X) :- 
	american(X), 
	weapon(Y), 
	sells(X,Y,Z), 
	hostile(Z).
