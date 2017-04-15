%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                    %
%  Grammar for simple natural language facts         %
%     and queries.                                   %
%  N. L. Tinkham                                     %
%                                                    %
%  Facts and queries are both Prolog facts.          %
%  The sentences are marked as "fact" or "query".    %
%                                                    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Blocks are {a, b, c, d, e, f, g, h}

% Fact forms:
% a is {red, yellow, blue, green, orange, purple}
% a is {on, beside} b
% a is a {cube, pyramid, sphere}

% Query forms:
% Is {a, b, ...} {on, beside} {a, b, ...}?
% Is {a, b, ...} {red, yellow...}?
% Is {a, b, ...} a {cube, pyramid, sphere}?
% Is {something, anything} {red, yellow...}?
% Is {something, anything} a {cube, pyramid, sphere}?

% Representation of facts and queries:
% red(a), yellow(a), etc.
% on(a, b)
% beside(a, b)

% The arguments to s are 1) the contribution of the
% rule towards the fact/query being constructed and
% 2) whether it's a fact or a query, based on its
% sentence form.

s(PrologFact, fact) --> np(Noun), be_form, complement(Property),
	{PrologFact =.. [Property, Noun]}.
	% Return Property(Noun) as PrologFact
	% Examples: purple(b), cube(e)
s(PrologFact, fact) --> np(Noun1), be_form, pp(Prep, Noun2),
	{PrologFact =.. [Prep, Noun1, Noun2]}.
	% Return Prep(Noun1, Noun2) as PrologFact
	% Examples: on(c, d), beside(a, f)
s(PrologFact, query) --> be_form, np(Noun), complement(Property),
	{PrologFact =.. [Property, Noun]}.
	% Return Property(Noun) as PrologFact
	% Examples: purple(b), cube(e)
s(PrologFact, query) --> be_form, np(Noun1), pp(Prep, Noun2),
	{PrologFact =.. [Prep, Noun1, Noun2]}.
	% Return Prep(Noun1, Noun2) as PrologFact
	% Examples: on(c, d), beside(a, f)
s(PrologFact, query) --> be_form, pronoun, complement(Property),
	{PrologFact =.. [Property, _]}.

np(Noun) --> det, noun(Noun).
np(Noun) --> propernoun(Noun).

pp(Prep, Noun) --> preposition(Prep), propernoun(Noun).

complement(Noun) --> np(Noun).
complement(Adj) --> adjective(Adj).

noun(cube) --> [cube].
noun(pyramid) --> [pyramid].
noun(sphere) --> [sphere].

det --> [a].

be_form --> [is].

preposition(on) --> [on].
preposition(beside) --> [beside].

propernoun(a) --> [a].
propernoun(b) --> [b].
propernoun(c) --> [c].
propernoun(d) --> [d].
propernoun(e) --> [e].
propernoun(f) --> [f].
propernoun(g) --> [g].
propernoun(h) --> [h].

adjective(red) --> [red].
adjective(yellow) --> [yellow].
adjective(blue) --> [blue].
adjective(green) --> [green].
adjective(orange) --> [orange].
adjective(purple) --> [purple].

pronoun --> [something].
pronoun --> [anything].