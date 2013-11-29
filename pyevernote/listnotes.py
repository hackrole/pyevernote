#!/usr/bin/env python
# encoding: utf-8

import settings
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotes():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    note_filter = ttypes.NoteFilter()
    # TODO: read notebookGuid from options
    note_filter.notebookGuid = '6ccaa7d7-cbdb-4190-8c28-121e603f0b8c'
    note_result_spc = ttypes.NotesMetadataResultSpec(True, True, True, True, True,)

    notecount = notestore.findNoteCounts(note_filter, True)
    print '==========='
    print notecount.notebookCounts
    print notecount.tagCounts
    print notecount.trashCount
    total_count = sum(notecount.notebookCounts.values(), 0)
    print total_count
    note_list = notestore.findNotesMetadata(note_filter, 0, total_count, )


if __name__ == '__main__':
    listnotes()
