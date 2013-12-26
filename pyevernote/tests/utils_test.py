#!/usr/bin/env python
#coding=utf8

import sys
import os

PRO_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PRO_PATH)

import unittest
import mock
import utils
import settings
from evernote.api.client import Store
from evernote.edam.error import ttypes as error_ttypes


# TODO define new exception
class GetNoteStoreTestCase(unittest.TestCase):

    def test_get_notestore_with_correct_token(self):
        token = settings.TOKEN
        ns = utils.get_notestore(token=token)
        self.assertTrue(isinstance(ns, Store))
        self.assertEqual(ns.token, token)

    def test_get_notestore_with_error_token(self):
        token = "error token"
        with self.assertRaises(error_ttypes.EDAMUserException):
            ns = utils.get_notestore(token=token)


class ListNotebooksTestCase(unittest.TestCase):
    def setUp(self):
        # mock the notestore for data init
        self.ns = mock.MagicMock()
        self.ns.return_value = ''

    def test_list_notebooks(self):
        notebook_list, thead_list, title = listnotebooks(self.ns)
