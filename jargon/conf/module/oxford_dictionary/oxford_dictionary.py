# Author: Ryan Lindsay and Justin Gavin
# Description: A module to handle defining words

import requests
import sys


# Used to create the url for the API call
def url_creator(term):
    base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'
    language = 'en'

    # Create the url for the API call
    api_url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + str(language) + '/' + str(term).lower()

    return api_url


# Used to get the requests return object from the API call
def data_collector(full_api_url):
    app_id = 'e21cb7da'                                                         # Justin needs different id for his own
    app_key = '47ccc72c94af0cd716360d4248336707'                                # Justin needs different key for his own

    # Gather the request object from the website
    request_object = requests.get(full_api_url, headers={'app_id': app_id, 'app_key': app_key})

    return request_object


# Used to define how to get certain information from the json object
def data_organizer(request):
    json_obj = request.json()                                                   # Extract json data from request

    return_data = dict(
        provider=json_obj.get('metadata').get('provider'),
        word=json_obj.get('results')[0].get('id'),
        origin=json_obj.get('results')[0].get('lexicalEntries')[0].get('entries')[0].get('etymologies')[0],
        senses=json_obj.get('results')[0].get('lexicalEntries')[0].get('entries')[0].get('senses'))

    return return_data


# Used to display the important information
def print_definition(definition, info):
    return_string = ''

    # return_string += '\n------------------------------------------------------------------------------'
    return_string += '\nWord of Interest: {}'.format(definition['word'])

    # Opted for if-elif-else statement instead of a dictionary for readability
    if (info == "origin") or (info == "background"):
        return_string += '\nOrigin: {}'.format(definition['origin'])
    elif (info == "definition") or (info == "definitions") or (info == "def"):
        for count in range(0, len(definition['senses'])):
            description = definition['senses'][count]
            return_string += '\nDefinition {}: {}'.format(count, description.get('definitions')[0])
    elif (info == "examples") or (info == "example") or (info == "usage"):
        counter = 1
        for count in range(0, len(definition['senses'])):
            examples = definition['senses'][count].get('examples')
            if examples is not None:
                for inner_count in range(0, len(examples)):
                    single = examples[inner_count].get('text')
                    return_string += '\nExample {}: {}'.format(counter, single)
                    counter += 1
    else:
        return_string += '\nOrigin: {}'.format(definition['origin'])
        return_string += '\nDefinitions: {}'.format(definition['definitions'])
        return_string += '\nExamples: {}'.format(definition['examples'])

    return return_string


# Custom exception to ensure we have enough info to process
class MinInfoLimit(Exception):
    """Must have at least two parameters"""
    pass


def module_main(args):
    # try:
        #if len(sys.argv) < 3:                                                   # Two parameters required min
        #    raise MinInfoLimit

        # Grab what type of data is important
        data_wanted = args['info_requested']

        # Loop through each city and display data
        # for argument in sys.argv[2:]:
        #    main_url = url_creator(argument)                                    # Assumes arguments are all words needed
        #    api_data = data_collector(main_url)                                 # Grab the requests object from the site
        #    api_dict = data_organizer(api_data)                                 # Create a dictionary for the info
        #    final_string = print_definition(api_dict, data_wanted)              # Print information requested

        argument = args['word']
        main_url = url_creator(argument)  # Assumes arguments are all words needed
        api_data = data_collector(main_url)  # Grab the requests object from the site
        api_dict = data_organizer(api_data)  # Create a dictionary for the info
        final_string = print_definition(api_dict, data_wanted)  # Print information requested

        # Print a notice and border bottom
        #final_string += '\n'
        #final_string += '\nSupport provided by: Oxford Dictionaries'
        #final_string += '\n------------------------------------------------------------------------------'

        return final_string
        # final_string should at this point contain all information that should be displayed #

    # I'm not sure what should be done with exceptions
    # except MinInfoLimit:
    #     print('At least 2 parameters required to run')

# Example call:
# print(module_main({'word': 'cat', 'info_requested': 'def'}))
