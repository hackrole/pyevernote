#!/usr/bin/env python
# encoding: utf-8

import settings
from evernote.api.client import EvernoteClient


def showtags():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    tag_list = notestore.listTags()

    for tag in tag_list:
        print '=============='
        print tag.guid
        print tag.name
        print tag.parentGuid
        print tag.updateSequenceNum


if __name__ == '__main__':
    showtags()
