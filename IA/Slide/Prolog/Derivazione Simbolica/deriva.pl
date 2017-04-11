d(sen(x),cos(x),x).
d(cos(x),-sen(x),x).

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