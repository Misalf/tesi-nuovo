a(1).
a(2). 
 
b(1).
b(2).

c(1).
c(2).
c(3).

d(1).
d(2).
d(3).

e(8).

% senza cut
%
% p(X,Y) :-
%	a(X),
%	b(X),
%	c(Y),
%	d(Y).

p(X,Y) :-
	a(X),
	b(X),
	!,
	c(Y),
	d(Y).


p(X,Y) :-
	e(X),
	e(Y).