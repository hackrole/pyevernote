import sys

class ListNotebook(object):
    def syntax(self):
        pass

    def long_desc(self):
        pass

    def print_help(self):
        pass

    def add_options(self, parser):
        parser.add_options()

    def check_options(self, parser):
        return true

    def execute(self, note_store, parser, stdout=sys.stdout):
        opts, args = parser.parse_option()
