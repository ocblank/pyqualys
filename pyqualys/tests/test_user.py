# -*- coding: utf-8 -*-
import unittest
import pyqualys
from pyqualys.utils import util


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.__instance = pyqualys.QualysAPI(username="abc",
                                            password="abc@1",
                                            host="https://qualys.com/")
        cls.__service = cls.__instance.service("vulnerability")

    def test_add_user(self):
        new_user = {
            'first_name': 'Amit',
            'last_name': 'Ghadge',
            'title': 'My Title',
            'phone': '012345689',
            'fax': '022',
            'email': 'aghadge@company.com',
            'address1': 'Panchshil Tech Park',
            'address2': 'Shivaji Nagar',
            'city': 'Pune',
            'country': 'India',
            'state': 'Maharashtra',
            'zip_code': 411022,
            'external_id': 101,
            'send_email': 0,
            'user_role': 'unit_manager',
            'business_unit': 'aa',
            'ui_interface_style': 'navy_blue',
        }
        expected_output = r"(.*) user has been successfully created."
        response = self.__service.add_user(**new_user)
        self.assertRegex(response['data']['RETURN']['MESSAGE'],
                         expected_output)

    def test_edit_user(self):
        username = "quays_ag1"
        edit_user = {
            'login': username,
            'first_name': 'Amit',
            'last_name': 'Ghadge',
            'title': 'My Title is Scanner',
            'phone': '012345689',
            'fax': '022',
            'email': 'aghadge@company.com',
            'address1': 'Panchshil Tech Park',
            'address2': 'Shivaji Nagar',
            'city': 'Pune',
            'country': 'India',
            'state': 'Maharashtra',
            'zip_code': 411022,
            'external_id': 101
        }
        expected_output = r"{} user has been successfully updated."
        response = self.__service.edit_user(**edit_user)
        self.assertRegex(response['data']['RETURN']['MESSAGE'],
                         expected_output.format(username))

    def test_get_users(self):
        expected_output = 0
        response = self.__service.get_users()
        total_users = len(response['data']['USER_LIST'])
        self.assertNotEqual(total_users, expected_output)

    def test_delete_user(self):
        expected_output = ""
        pass

    def test_deactivate_user(self):
        username = "quays_ag1"
        expected_output = "{} user has been successfully deactivated."
        response = self.__service.deactivate_user(username=username)
        self.assertRegex(response['data']['RETURN']['MESSAGE'],
                         expected_output.format(username))

    def test_activate_user(self):
        username = "quays_ag1"
        expected_output = "{} user has been successfully activated."
        response = self.__service.activate_user(username=username)
        self.assertRegex(response['data']['RETURN']['MESSAGE'],
                         expected_output.format(username))
