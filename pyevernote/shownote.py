#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes
import settings


def shownote():
    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    notefilter = ttypes.NoteFilter(notebookGuid=settings.NOTEBOOK_GUID_1)
    offset = 0
    limit = 200
    note  =  noteStore.getNote(settings.NOTE_GUID_1, True, True, False, False)
    print note.guid
    print note.title
    print note.content
    print note.created
    print note.updated
    print note.notebookGuid


if __name__ == '__main__':
    shownote()
