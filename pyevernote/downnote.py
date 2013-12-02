#!/usr/bin/env python
# encoding: utf-8

import settings
from optparse import OptionParser, OptionValueError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def downnote():
    # get the opt parser
    usage = "usage: %prog <-f file> note_guid"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="write the note content to file", metavar="FILE")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        raise OptionValueError("must give the note guid.")

    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    note_guid = args[0]
    note  =  noteStore.getNote(note_guid, True, True, False, False)

    print '>>>>>>>>>>>'
    print "note_guid:",note.guid
    print "title:",note.title
    print "create_time:",note.created
    print "update_time:",note.updated
    print "notebook_guid:",note.notebookGuid

    # the note content handle
    content = note.content
    filename = options.filename
    if filename:
        with open(filename, 'w') as f:
            f.write(note.content)
    else:
        print "========== content ========="
        print note.content





if __name__ == '__main__':
    downnote()
