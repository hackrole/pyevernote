#!/usr/bin/env python
# encoding: utf-8

import settings
import sys
import time
from optparse import OptionParser
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotes():
    # the option parser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="also write the notes list to file",
                      metavar="FILE")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print "please give the notebook guid for list notes"
        sys.exit(-1)

    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    # get the notes total count
    note_filter = ttypes.NoteFilter()
    note_filter.notebookGuid = args[0]
    note_collections_count = notestore.findNoteCounts(note_filter, True)
    try:
        note_count = sum(note_collections_count.notebookCounts.values())
    except Exception,e:
        print "the notebooks %s has no notes now" % (args[0])
        sys.exit(-1)
    print '=========='
    print "find %s notes" % (note_count)

    # get the notes_list meta data
    note_result_spc = ttypes.NotesMetadataResultSpec(True, True, True, True, True, False, True)
    note_list = notestore.findNotesMetadata(note_filter, 0, note_count,
                                            note_result_spc)
    for note in note_list.notes:
        print '>>>>>>>>'
        print note.guid
        print note.title
        print note.contentLength
        print time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(note.created/1000))
        print time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(note.updated/1000))
        print note.notebookGuid


if __name__ == '__main__':
    listnotes()
