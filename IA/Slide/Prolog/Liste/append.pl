% La terza lista è ottenuta accodando
% la seconda alla prima.

appendi([],L,L).

appendi([T1|C1],L2,[T1|C3]) :-
	appendi(C1,L2,C3).