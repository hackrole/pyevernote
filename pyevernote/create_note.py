#!/usr/bin/env python
#coding=utf-8

import settings
from optparse import OptionParser, OptionValueError
from evernote.api.client import EvernoteClient
from evernote.edam.noteStore import ttypes


def create_note():
    # get the opt parser
    usage = "usage: %prog <-t title> <-T tag1>.. <-n notebookguid>  file"
    parser = OptionParser(usage=usage)
    parser.add_option("-n", "--title", dest="note_title",
                          help="set the note title", metavar="TITLE")
    # TODO: options list
    parser.add_option("-t", "--tag", dest="note_tags",
                      help="set the note tag", metavar="TAGS")
    parser.add_option("-b", "--notebook", dest="notebook_guid",
                      help="set the notebook", metavar="notebook_guid")
    options, args = parser.parse_args()

    if len(args) < 1:
        raise OptionValueError("must give the filename to create the note")

    if options.note_title
        title = options.note_title
    elif title:
        # parser the file content #+TITLE
        pass
    else:
        pass # the filename without after

    if options.note_tags:
        tags = options.note_tags
    elif tags:
        pass # parser the file #TAGS

    if options.notebook_guid:
        notebook_guid = options.notebook_guid
    else:
        pass # parser the file for notebook_guid or title

    if note notebook_guid:
        warning("not give the notebook, use the default notebook!")

    note = ttypes.Note()
    note.title = title
    note.content = open(filename).read()
    note.notebookGuid = notebook_guid
    note.resources = [resources]
    note.tagNames = [tagname]
    try:
        create_note = noteStore.createNote(note)
    except EDAMNotFoundException,e:
        print "notebook %s not found" % (notbook)
    print "======= create note from file %s success =========" % (filename,)
    print create_note.guid
