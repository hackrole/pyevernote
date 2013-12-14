#!/usr/bin/env python
# encoding: utf-8

import settings
import sys
import time
from optparse import OptionParser, OptionError, OptParseError
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes
from utils import json_data_print_totable


def listnotes():
    # the option parser
    parser = OptionParser()
    parser.add_option("-b", "--nbn", dest="nbn",
                      help="set the notebook name to list, cover the --nbg",
                      metavar="notebook_name")
    parser.add_option("-t", "--tn", dest="tn", action="append",
                      help="set the tag name to list, cover the --tn",
                      metavar="tag_name")

    (options, args) = parser.parse_args()
    if not options.nbn and not options.tn:
        print "must set the notebook name or tagname, use -h for detail"
        sys.exit(-1)

    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    note_filter = ttypes.NoteFilter()
    # get the notebook guid if give the notebook name
    if options.nbn:
        notebooks = notestore.listNotebooks()
        for notebook in notebooks:
            if notebook.name.lower() == options.nbn.lower():
                nbg = notebook.guid
                note_filter.notebookGuid = nbg
                break
    # get the tags guid if give the tag list
    if options.tn:
        tags = notestore.listTags()
        tgs = []
        for tag in tags:
            if lower(tag.name) in options.tn:
                tgs.append(tag.guid)
        if tgs:
            note_filter.tagGuids = tgs

    note_collections_count = notestore.findNoteCounts(note_filter, True)
    try:
        note_count = sum(note_collections_count.notebookCounts.values())
    except Exception,e:
        print ">>> no notes found"
        sys.exit(-1)
    print ">>> find %s notes" % (note_count)

    # get the notes_list meta data
    note_result_spc = ttypes.NotesMetadataResultSpec(True, True, True,
                                                     True, True, False, True)
    note_list = notestore.findNotesMetadata(note_filter, 0, note_count,
                                            note_result_spc)

    # print the json data
    thead = ['guid', 'title', 'notebook_guid', 'tags_guid',
             'created', 'updated']
    note_list = [{'guid': note.guid, 'title': note.title,
                  'notebook_guid': note.notebookGuid,
                  'tags_guid': note.tagGuids,
                  'created': time.strftime("%Y-%m-%d", time.gmtime(note.created/1000)),
                  'updated': time.strftime("%Y-%m-%d", time.gmtime(note.updated/1000))}
                 for note in note_list.notes]
    title = "note list"
    json_data_print_totable(thead, note_list, title)


if __name__ == '__main__':
    listnotes()
