
from ..conf import conf


class Core:
    def __init__(self, args):
        self.verbose = args.verbose
        self.command_dict = conf.get_command_word_dict()
        self.ovr_dict = conf.get_ovr_dict()
        # TODO self.ambiguous_commands = conf.get_ambiguous_commands()

        if self.verbose:
            print(self.command_dict)

    def process_query(self, query):
        """Accept and process a string query"""
        args_dict = {}
        # Check for overriding string in the beginning of query
        for command in self.ovr_dict:
            if query.startswith(command):
                module_name = self.ovr_dict[command]
                args_dict['query'] = query.replace(command, '')
                args_dict['verbose'] = self.verbose
                exec("from ..conf.module." + module_name + " import " + module_name)
                module_response = eval(module_name + '.module_main(args_dict)')
                return module_response

        for command in self.command_dict:
            if command in query.lower():
                module_name = self.command_dict[command]
                if self.verbose:
                    print("Passing to module: " + module_name)
                args_dict['query'] = query
                args_dict['verbose'] = self.verbose
                args_dict['command'] = command
                exec("from ..conf.module." + module_name + " import " + module_name)
                module_response = eval(module_name + '.module_main(args_dict)')
                return module_response

        return "Sorry, I don't understand"