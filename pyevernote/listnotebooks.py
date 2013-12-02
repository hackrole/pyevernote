#!/usr/bin/env python
# encoding: utf-8

import settings
import ConfigParser
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotebooks():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    notebook_list = notestore.listNotebooks()

    for notebook in notebook_list:
        print '============'
        print notebook.guid
        print notebook.name
        print notebook.defaultNotebook
        print notebook.serviceCreated
        print notebook.serviceUpdated

if __name__ == '__main__':
    listnotebooks()
