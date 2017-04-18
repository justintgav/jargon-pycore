% defines words/phrases that could be common to all modules
%
% Author: Johan Burke

np(Det, Noun) --> det(Det), noun(Noun).

pp(Prep, Noun) --> preposition(Prep), propernoun(Noun).
pp(Prep, Amount, Unit) --> preposition(Prep), num(Amount, Unit).

% this will just accept any single word
noun(X) --> [X].
propernoun(X) --> [X].

preposition(like) --> [like].
preposition(in) --> [in].
preposition(at) --> [at].

question_pronoun(what) --> [what].

be_form(is) --> [is].
be_form(be) --> [be].

aux_verb(will) --> [will].

det(the) --> [the].
det(a) --> [a].

num(Amount, Unit) --> [Amount], [Unit].

future_verb(Aux, Main) --> aux_verb(Aux), be_form(Main).

future_inv_verb(Aux, Det, Noun, Verb) --> aux_verb(Aux), np(Det, Noun), verb(Verb, present).

pronoun(it) --> [it].

time_phrase(Time) --> pp(at, Time).
time_phrase(Time) --> adverb(Time).

adverb(tomorrow) --> [tomorrow].
time_adverb(Amount, Unit) --> preposition(at), num(Amount, Unit).

verb(Verb, Tense) --> [Verb].
