# -*- coding: utf-8 -*-
import unittest
import pyqualys


class TestService(unittest.TestCase):
    def setUp(self):
        self.instance = pyqualys.QualysAPI(username="abc",
                                           password="abc@1",
                                           host="https://qualys.com/")

    def test_list_service(self):
        self.assertEqual(self.instance.list_services(), ["vulnerability"])
