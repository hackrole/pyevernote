#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
from optparse import OptionParser, OptionValueError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes

import settings


def shownote(args, file_name=None):
    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    note_guid = args[0]
    note  =  noteStore.getNote(note_guid, True, True, False, False)
    print "note_guid:",note.guid
    print "title:",note.title
    print "create_time:",note.created
    print "update_time:",note.updated
    print "notebook_guid:",note.notebookGuid
    content = note.content
    if file_name:
        with open(file_name, 'w') as f:
            f.write(note.content)
    else:
        print "========== content ========="
        print note.content


def parse_args():
    usage = "usage: %prog [options] note_guid"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="write the note content to file, need combine with -a", metavar="FILE")
    options, args = parser.parse_args()
    if len(args) < 1:
        raise OptionValueError("must give the note guid.")
    shownote(args, options.filename)


if __name__ == '__main__':
    # shownote()
    parse_args()
