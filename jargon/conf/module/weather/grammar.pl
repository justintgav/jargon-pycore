% grammar rules specific for the weather module
%
% Author: Johan Burke

% Queries to be accepted:
% What is the weather like [in {location}]?
% What will the weather be like [in {location}] [time_phrase]?
% Is it raining [in {location}]?
% Is it snowing [in {location}]?
% Will it be raining/snowing [in {location}] [time_phrase]?
% What is the temperature [in {location}]?
% What will the temperature be [in {location}] [time_phrase]?

% IMPORTANT NOTE: for time phrases, pass 5pm or whatever without spaces!!!!!

% What is the weather like?
s(default_location, now, default_type, weather_query) --> question_pronoun(what), be_form(is), np(the, weather), preposition(like).

% What will the weather be like?
s(defualt_location, five_day, default_type, weather_query) --> question_pronoun(what), future_inv_verb(will, the, weather, be), preposition(like).

% What is the weather like in [Location]?
s(Location, now, default_type, weather_query) --> question_pronoun(what), be_form(is), np(the, weather), preposition(like), pp(in, Location).
s(default_location, Time, default_type, weather_query) --> question_pronoun(what), future_inv_verb(will, the, weather, be), preposition(like), pp(at, Time).
s(Location, Time, default_type, weather_query) --> question_pronoun(what), future_inv_verb(will, the, weather, be), preposition(like), pp(in, Location), pp(at, Time).
s(Location, five_day, default_type, weather_query) --> question_pronoun(what), future_inv_verb(will, the, weather, be), preposition(like), pp(in, Location).

s(default_location, now, Type, weather_query) --> be_form(is), pronoun(it), weather_verb(Type, pparticiple).
s(Location, now, Type, weather_query) --> be_form(is), pronoun(it), weather_verb(Type, pparticiple), pp(in, Location).
s(default_location, five_day, Type, weather_query) --> future_inv_weather_verb(it, Type).
s(default_location, Time, Type, weather_query) --> future_inv_weather_verb(it, Type), pp(at, Time).
s(Location, Time, Type, weather_query) --> future_inv_weather_verb(it, Type), pp(in, Location), pp(at, Time).

s(default_location, now, temperature, weather_query) --> question_pronoun(what), be_form(is), np(the, temperature).
s(Location, now, temperature, weather_query) --> question_pronoun(what), be_form(is), np(the, temperature), pp(in, Location).
s(default_location, Time, temperature, weather_query) --> question_pronoun(what), future_inv_verb(will, the, temperature, be), pp(at, Time).
s(Location, Time, temperature, weather_query) --> question_pronoun(what), future_inv_verb(will, the, temperature, be), pp(in, Location), pp(at, Time).

future_inv_weather_verb(Pronoun, Weather) --> aux_verb(will), pronoun(Pronoun), be_form(be), weather_verb(Weather, pparticiple).

weather_verb(snow, pparticiple) --> verb(snowing, pparticiple).
weather_verb(rain, pparticiple) --> verb(raining, pparticiple).
weather_verb(snow, present) --> verb(snow, pparticiple).
weather_verb(rain, present) --> verb(rain, pparticiple).
