#!/usr/bin/env python
#coding=utf-8

import sys
import unittest
import commands


# need to init the evernote data by hand for test
class TestListNotebooks(unittest.TestCase):
    """ test for list notebook """

    def test_list_notebooks(self):
        command_str = "python listnotebooks.py"
        # list the notebooks return status 0
        # the and notebook lists string
        (status, output) = commands.getstatusoutput(command_str)
        self.assertEqual(0, status)
        # assert the notebook list
        output_list = output.split('\n')
        self.assertTrue(len(output_list) >= 3)
