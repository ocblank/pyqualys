# -*- coding: utf-8 -*-
import unittest
import pyqualys


class TestService(unittest.TestCase):
    def setUp(self):
        self.instance = None

    def test_services_instance(self):
        for service in self.instance.list_services():
            self.assertEqual(self.instance.service(service).__class__.__name__,
                             service.title()+"Service")
