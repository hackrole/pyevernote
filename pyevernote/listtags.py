#!/usr/bin/env python
# encoding: utf-8

import settings
from evernote.api.client import EvernoteClient
from utils import json_data_print_totable


def showtags():
    client = EvernoteClient(token=settings.TOKEN)
    notestore = client.get_note_store()

    tag_list = notestore.listTags()

    thead = ["tag_guid", "tag_name", "tag_parent_guid", "tag_updateSequenceNum"]
    data = [{'tag_guid': tag.guid, "tag_name": tag.name, "tag_parent_guid": tag.parentGuid,
             "tag_updateSequenceNum": tag.updateSequenceNum} for tag in tag_list]
    title = "tag_list"

    # print data
    json_data_print_totable(thead, data, title)


if __name__ == '__main__':
    showtags()
