% grammars specifying different types of question phrases
% use leftovers to find words that the question are asking about
%
% Author: Johan Burke

s(what_query) --> interrogative_word, be_form.

interrogative_word --> [what].
be_form --> [is].
be_form --> [are].
