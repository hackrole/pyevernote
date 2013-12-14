#!/usr/bin/env python
# encoding: utf-8

import settings
import ConfigParser
import string
import time
from utils import json_data_print_totable
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotebooks():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    notebook_list = notestore.listNotebooks()

    thead = ["notebook_guid", "notebook_name", "create_time"]
    data = [{'notebook_guid': notebook.guid, 'notebook_name': notebook.name,
             'create_time': time.strftime("%Y-%m-%d", time.gmtime(notebook.serviceCreated/1000))}
             for notebook in notebook_list]
    title = "notebook list"

    # json print
    json_data_print_totable(thead, data, title)


if __name__ == '__main__':
    listnotebooks()
