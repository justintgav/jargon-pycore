# jtg's keys
# collegiate dictionary: 88c667ec-ca75-4814-b875-105950dab309


from .api import (LearnersDictionary, CollegiateDictionary,
                                 WordNotFoundException)

def lookup(dictionary_class, key, query):
    dictionary = dictionary_class(key)
    try:
        defs = [(entry.word, entry.function, definition)
                for entry in dictionary.lookup(query)
                for definition, examples in entry.senses]
    except WordNotFoundException:
        defs = []
    dname = dictionary_class.__name__.replace('Dictionary', '').upper()
    if defs == []:
        print("{0}: No definitions found for '{1}'".format(dname, query))
    for word, pos, definition in defs:
        print("{0}: {1} [{2}]: {3}".format(dname, word, pos, definition))


def module_main(args):
    # lookup(CollegiateDictionary, collkey, query)
    collkey = "88c667ec-ca75-4814-b875-105950dab309"
    lookup(CollegiateDictionary, collkey, args)