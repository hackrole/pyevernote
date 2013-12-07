#!/usr/bin/env python
# encoding: utf-8

import settings
import sys
import time
from optparse import OptionParser, OptionError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def listnotes_options():
    parser = OptionParser()
    parser.add_option("-B", "--nbg", dest="nbg",
                      help="set the notebook guid to list",
                      metavar="NoteBookGuid")
    parser.add_option("-b", "--nbn", dest="nbn",
                      help="set the notebook name to list, cover the --nbg")
    parser.add_option("-T", "--tg", dest="tg",
                      help="set the tag guid to list",
                      metavar="TagGuid")
    parser.add_option("-t", "--tn", dest="tn",
                      help="set the tag name to list, cover the --tn",
                      metavar="TagName")
    # parser.add_option('-p', "--page", dest="page", default=1, type="int",
    #                   help="set the page to list, default  1",
    #                   metavar="Page")
    # parser.add_option("-s", "-pagesize", dest="page_size", default=20, type="int",
    #                   help="set the page size, default 20",
    #                   metavar="PageSize")
    return parser.parse_args()

def check_options(options):
    if not (options.nbg or options.nbn or options.tg or options.tn):
        raise OptionError("must give an contidion, use -h for detail")

def get_note_filter(options):
    if options.nbn:
        pass

def listnotes():
    # the option parser
    (options, args) = listnotes_options()
    check_options(options)

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
