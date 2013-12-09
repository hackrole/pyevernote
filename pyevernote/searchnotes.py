#!/usr/bin/env python
#coding=utf-8

import settings
from optparse import OptionParser, OptionValueError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def search_notes():
    # TODO: more search options
    usage = "usage: %prog words"
    parser = OptionParser(usage=usage)
    options, args = parser.parse_args()
    if len(args) != 1:
        raise OptionParser("only support one word search, give \"\" for space")
    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    words = args[0]
    note_filter = ttypes.NoteFilter(words=words)

    count = noteStore.findNoteCounts(note_filter, False)
    resc = ttypes.NotesMetadataResultSpec(True, False, True, True, False, False, True, True)
    notes = noteStore.findNotesMetadata(note_filter, 0, count, resc)

    print '>>>>>>>>> find %s notes' % count
    for note in notes.notes:
        print '==========='
        print note.guid
        print note.title
        print note.created
        print note.updated
        print note.tagGuids
