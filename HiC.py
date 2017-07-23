#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Utils
import re
from decimal import Decimal


def HiC(article):
    holding=''
    holder=''
    holderUndef=True
    for table in article.findAll('tbody'):
        #print "Table!"
        for row in table.findAll('tr', recursive=False):
            #print "row!******************"
            rowstring=''
            for col in row.findAll('td'):
                for s in col.stripped_strings:
                    rowstring += s +' ' 
                rowstring.strip('\n')
                rowstring +=":"
            fields = rowstring.split(':')
            if rowstring.startswith('Resulting'):
                try:
                    holding = Utils.getDecimal(fields[3])
                except:
                    None
            if rowstring.startswith('Name') and holderUndef :
                    holder = fields[1]
                    holderUndef=False
            #if the form happens to be a non TR-1 do this
            if rowstring.startswith('3. Full name') and holderUndef :
                    holder = fields[1]
                    holderUndef=False
            if rowstring.startswith('7. Thresh') :
                    holding = Utils.getDecimal(fields[1])
            
    #end of tables
    gc=''
    returndoc = { "Holding" : str(holding), "Holder": str(holder) }
    return returndoc




