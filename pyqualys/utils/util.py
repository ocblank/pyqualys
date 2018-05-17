# -*- coding: utf-8 -*-
from lxml import etree


def verify_phone_number(number):
    pass


def verify_email_address(email):
    pass


def decode_xml(xml_str):
    response = xml_str.replace('encoding="UTF-8"', '')
    return etree.fromstring(response)
