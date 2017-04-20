
from ..conf import conf


class Core:
    def __init__(self, args):
        self.verbose = args.verbose
        self.command_dict = conf.get_command_word_dict()
        # TODO self.ambiguous_commands = conf.get_ambiguous_commands()

        if self.verbose:
            print(self.command_dict)

    def process_query(self, query):
        """Accept and process a string query"""
        for command in self.command_dict:
            if command in query:
                module_name = self.command_dict[command]
                if self.verbose:
                    print("Passing to module: " + module_name)
                args_dict = {}
                args_dict['command'] = query
                args_dict['verbose'] = self.verbose
                exec("from ..conf.module." + module_name + " import " + module_name)
                module_response = ""
                exec("module_response = " + module_name + ".module_main(args_dict)")
                return module_response

        return "Sorry, I don't understand"