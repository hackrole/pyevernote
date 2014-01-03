#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import time
from evernote.edam.notestore import ttypes


def listnotebooks(notestore):
    notebook_list = notestore.listNotebooks()

    thead = ["notebook_guid", "notebook_name", "create_time"]
    data = [{'notebook_guid': notebook.guid, 'notebook_name': notebook.name,
             'create_time': time.strftime("%Y-%m-%d", time.gmtime(notebook.serviceCreated/1000))}
             for notebook in notebook_list]
    title = "notebook list"
    
    return (thead, data, title)


if __name__ == '__main__':
    import utils
    import settings

    notestore = utils.get_notestore(settings.TOKEN)
    thead, data, title = listnotebooks(notestore)
    utils.json_data_print_totable(thead, data, title)
