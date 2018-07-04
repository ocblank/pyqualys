# -*- coding: utf-8 -*-
import pyqualys

qualys = pyqualys.QualysAPI(username="abc",
                            password="abc",
                            host="https://qualys.com/")

service = qualys.service("vulnerability")
# Get response in json format, default is xml
service.FORMAT = "json"

# Start Scan
scan = service.scanner.start_scan(scan_title="MyLinuxScanTest", ip="10.114.26.122",
                                  iscanner_name="AGScanner",
                                  option_title="Initial Options")
print("Start Scan", scan.text)