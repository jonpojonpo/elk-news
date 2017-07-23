#!/usr/bin/env python
# --- coding:utf-8 ---

import Utils
import re
import json


def Shareholding(article):
    table_data =[[cell.text for cell in row("td")] for row in article("tr")]
    print json.dumps(dict(table_data))

