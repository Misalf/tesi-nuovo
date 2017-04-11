d(X,1,X).
d(sen(X),cos(X)*DX,Y):-
	d(X,DX,Y).
d(cos(X),-sen(X)*DX,Y):-
	d(X,DX,Y).

d(F*G,DF*G+F*DG,X):-
	d(F,DF,X),
	d(G,DG,X).
d(F+G,DF+DG,X):-
	d(F,DF,X),
	d(G,DG,X).
d(F-G,DF-DG,X):-
	d(F,DF,X),
	d(G,DG,X).
d(F/G,(DF*G-F*DG)/G*G,X):-
	d(F,DF,X),
	d(G,DG,X).