#!/usr/bin/env python
# encoding: utf-8

import settings
import ConfigParser
import string
import time
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotebooks():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    notebook_list = notestore.listNotebooks()

    print string.ljust("notebook_guid", 50), string.ljust("notebook_name", 30), string.ljust("notebook_create_time", 12)
    print '-' * 100
    for notebook in notebook_list:
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(notebook.serviceCreated/1000))
        print string.ljust(`notebook.guid`, 50), string.ljust(`notebook.name`, 30), string.ljust(create_time, 12)


if __name__ == '__main__':
    listnotebooks()
