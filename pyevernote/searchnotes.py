#!/usr/bin/env python
#coding=utf-8

import settings
from optparse import OptionParser, OptionValueError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


def search_notes():
    # TODO: more search options
    usage = "usage: %prog <-p page> <-l limit> words"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--page", dest="page",
                      help="give the note list page", metavar="Page")
    parser.add_option("-l", "--limit", dest="limit",
                      help="give the page limit", metavar="Limit")
    options, args = parser.parse_args()
    if len(args) != 1:
        raise OptionParser("only support one word search, give \"\" for space")
    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    words = args[0]
    note_filter = ttypes.NoteFilter(words=words)
    page = options.page if not options.page else 1
    limit = options.limit if not options.limit else 20

    note_meta_list = noteStore.findNotesMetadata(note_filter, )










