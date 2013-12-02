#!/usr/bin/env python
#coding=utf-8

import settings
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes
from evernote.edam.error import ttypes as error_ttypes


def delete_note():
    usage = "usage: %prog note_guid"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if len(args) != 1:
        raise OptionParser("must give the note_guid.")

    client = EvernoteClient(token=settings.TOKEN)
    noteStore = client.get_note_store()

    note_guid = args[0]
    try:
        noteStore.deleteNote(note_guid)
    except error_ttypes.EDAMNotFoundException,e:
        print "note for guid %s not found" % (note_guid,)
    except error_ttypes.EDAMUserException,e:
        print "note for guid %s is already delete" % (note_guid,)
    except error_ttypes.EDAMUserException,e:
        print "you have no permission to delete the note(guid:)" % (note_guid,)
    print "note(guid: %s) has been move to trash" % (note_guid,)
