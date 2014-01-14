import sys

class BaseCommand(object):
    def __init__(self, parse, stdout=sys.stdout):
        self.parse = parse

    def syntax(self):
        return parser.Usage

    def long_desc(self):
        return ""

    def add_options(self):
        """ add some pubic options. if children rewrite this, remember to call super"""
        self.parse.add_options('-v', '--verbose')

    def check_options(self):
        """ check if opt is right, rewrite on subclass.
        should return errcode and message """
        return True, "sucess"

    def execute(self, note_store):
        """ rewrite on subclass, the main command func """
        raise NotImplementedError("not implemented")

    def run(self):
        """ should not rewrite this, you may want to see the execute func """
        self.add_options()
        self.check_options()
        self.execute()