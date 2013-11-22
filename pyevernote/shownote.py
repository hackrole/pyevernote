#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes
from settings import TOKEN


def shownote():
    client = EvernoteClient(token=TOKEN)
    noteStore = client.get_note_store()

    notefilter = ttypes.NoteFilter()
    offset = 0
    limit = 200
    notelist  =  noteStore.findNotes(notefilter, offset, limit)
    print notelist


if __name__ == '__main__':
    shownote()
