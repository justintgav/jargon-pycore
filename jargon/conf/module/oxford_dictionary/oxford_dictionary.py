# Author: Ryan Lindsay and Justin Gavin
# Description: A module to handle defining words
#
# args format:
#   'word': the specific word being looked up
#   'info_requested': what information is descried
#                       Ex: 'definition', 'origin', 'etymology', 'example'
#
# Example NL Queries:
#   What is the definition of cat?
#    +args['info_requested'] = 'definition'
#    +args['word'] = 'cat'
#   >> Word of Interest: cat
#   >> Definition: a small domesticated carnivorous mammal with soft fur, a short snout,
#   >> and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.


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
    if request.status_code == 404:
        return
    json_obj = request.json()                                                   # Extract json data from request

    return_data = dict()
    try:
        return_data['provider'] = json_obj.get('metadata').get('provider')
        return_data['word'] = json_obj.get('results')[0].get('id')
        return_data['senses'] = json_obj.get('results')[0].get('lexicalEntries')[0].get('entries')[0].get('senses')
        return_data['origin'] = json_obj.get('results')[0].get('lexicalEntries')[0].get('entries')[0].get('etymologies')[0]

    except TypeError:
        pass

    return return_data


# Used to display the important information
def print_definition(definition, info):
    return_string = ''

    # return_string += '\n------------------------------------------------------------------------------'
    return_string += '\nWord of Interest: {}'.format(definition['word'])

    # Opted for if-elif-else statement instead of a dictionary for readability
    if (info == "origin") or (info == "background") or (info == "etymology"):
        return_string += '\nOrigin: {}'.format(definition['origin'])
    elif (info == "definition") or (info == "definitions") or (info == "define"):
        # for count in range(0, len(definition['senses'])):
        #    description = definition['senses'][count]
        #    return_string += '\nDefinition {}: {}'.format(count, description.get('definitions')[0])
        return_string += '\nDefinition: ' + definition['senses'][0].get('definitions')[0]
    elif (info == "examples") or (info == "example") or (info == "usage") or (info == "sentence"):
        counter = 1
        for count in range(0, len(definition['senses'])):
            examples = definition['senses'][count].get('examples')
            if examples is not None:
                for inner_count in range(0, len(examples)):
                    single = examples[inner_count].get('text')
                    # return_string += '\nExample {}: {}'.format(counter, single)
                    # temp fix to only grab one example:
                    return single
                    counter += 1
    else:
        return_string += '\nOrigin: {}'.format(definition['origin'])
        return_string += '\nDefinitions: {}'.format(definition['definitions'])
        return_string += '\nExamples: {}'.format(definition['examples'])

    return return_string


def module_main(args):
    command_string = args['command']
    query = args['query'].replace(command_string, '')
    if command_string == 'what is a':
        command_string = 'definition'
    elif command_string == 'word origin':
        command_string = 'origin'
    elif command_string == 'in a sentence':
        command_string = 'example'

    data_wanted = command_string



    # replace meaningless words
    query = query.replace(' use ', '')
    argument = query.strip()
    if args['verbose']:
        print("Looking up:\n" + argument)
    main_url = url_creator(argument)  # Assumes arguments are all words needed
    api_data = data_collector(main_url)  # Grab the requests object from the site
    api_dict = data_organizer(api_data)  # Create a dictionary for the info
    if api_dict:
        final_string = print_definition(api_dict, data_wanted)  # Print information requested
    else:
        final_string = "I could not find that word"

    return final_string


# Example call:
# print(module_main({'word': 'cat', 'info_requested': 'definition'}))
