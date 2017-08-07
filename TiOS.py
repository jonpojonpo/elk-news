#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Utils
import re
from decimal import Decimal


def TiOS(article):
    fulltext =''
    for s in article.stripped_strings:
        fulltext += s
    print(fulltext)
            
    #end of tables
    returndoc = { "TiOS" : "" }
    return returndoc




