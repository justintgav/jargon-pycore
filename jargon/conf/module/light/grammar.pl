% grammar for light

light(default_brightness, default_color, Status, light_query) --> [turn], [Status].
light(default_brightness, default_color, Status, light_query) --> [turn], np(the, light), [Status].
light(Brightness, default_color, on, light_query) --> [turn], np(the, light), [to], [Brightness].
light(Brightness, Color, on, light_query) --> [turn], np(the, light), [Color], [brightness], [Brightness].