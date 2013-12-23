#!/usr/bin/env python
#coding=utf8

import mock
import unittest
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import ttypes


class ListNoteBookTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_notebooks_with_mock(self):
        TOKEN = 'S=s1:U=6a524:E=14621df994d:C=13eca2e6d4f:P=1cd:A=en-devtoken:V=2:H=70c0d7eb3ad2a17e7e5ed3e077eb7863'
        client = EvernoteClient(token=TOKEN)
        notestore = client.get_note_store()
        notestore.listNotebooks = mock.Mock(return_value={'time': 'hello world', 'thing': 'oevr'})
        print notestore.listNotebooks()

if __name__ == "__main__":
    unittest.main()
