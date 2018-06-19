# -*- coding: utf-8 -*-
import re
import pyqualys

obj = pyqualys.QualysAPI(username="admin",
                         password="admin",
                         host="https://qualys.com/")

service = obj.service("vulnerability")

data = {'action': 'list'}
report_list = service.report.list_report(**data)
print(report_list)

data = {
        'report_title': 'pyqualys report',
        'action': 'launch',
        'report_type': 'Scan',
        'template_id': '134271',
        'output_format': 'pdf',
}
scan_report = service.report.scan_report(**data)
print(scan_report)
