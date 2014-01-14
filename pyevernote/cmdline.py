import argparse
from evernote.api.client import EvernoteClient


def execute(argv=None, settings=None):
    if argv is None:
        argv = sys.argv

    if settings is None and 'pyevernote.conf' in sys.modules:
        from pyevernote import conf
        if hasattr(conf, 'settings'):
            settings = conf.settings

    if settings is None:
        settings = get_project_settings()
    check_deprecated_settings(settinngs)

    cmds = _get_commands_dict(settings)
    cmdname = _pop_command_name(argv)
    parser = argparse.ArgumentParser()
    if not cmdname:
        _print_commands(settings)
        sys.exit(0)
    elif cmdname not in cmds:
        _print_unknown_command(settings, cmdname)
        sys.exit(2)

    cms = cmds[cmdname]
    parser.usage = "pyevernote %s %s" % (cmdname, cmd.syntac())
    parser.description = cmd.long_desc()
    settings.defaults.update(cmd.defaults_settings)
    cmd.settings = settings
    cmd.add_options(parser)
    opts, args = parser.parse_args(args=argv[1:])
    cmd.run()


if __name__ == '__main__':
    execute()