% grammar rules specific for the dictionary module
%
% Author: Johan Burke

% Queries to be accepted:
% Define [word]
% What is the definition of [word]
% What is the origin of the word [word]
% What is the history of the word [word]
% Use [Word] in a sentence


oxford_dictionary(definition, Word, blank, oxford_dictionary_query) --> [define], [Word].
oxford_dictionary(definition, Word, blank, oxford_dictionary_query) --> question_pronoun(what), be_form(is), np(the, definition), pp(of, Word).
oxford_dictionary(definition, Word, blank, oxford_dictionary_query) --> question_pronoun(what), be_form(is), np(the, definition), pp_det(of, word), [Word].
oxford_dictionary(Origin, Word, blank, oxford_dictionary_query) --> question_pronoun(what), be_form(is), origin_np(Origin), pp(of, Word).
oxford_dictionary(Origin, Word, blank, oxford_dictionary_query) --> question_pronoun(what), be_form(is), origin_np(Origin), pp_det(of, word), [Word].

oxford_dictionary(examples, Word, blank, oxford_dictionary_query) --> [use], [Word], pp_indet(in, sentence).

origin_np(origin) --> np(the, origin).
origin_np(background) --> np(the, background).
origin_np(etymology) --> np(the, etymology).
