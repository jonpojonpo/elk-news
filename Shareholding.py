#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Utils
import re
from decimal import Decimal


def Shareholding(article):
    total=''
    side=None
    pvs=None
    apvs=None
    gc=None
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
            if rowstring[0] == 'b':
                side = Utils.getSide(rowstring)
            if rowstring[0] == 'c':
                pvs = Utils.getPricesAndVolumes(rowstring)
            if rowstring[0] == 'd':
                apvs = Utils.getAggPVs(rowstring)
            #print(rowstring),
            #print ""
        #end of rows
        #print( "s=" +str(side))
        #print( "pvs=" + str(pvs))
        #print( "apvs=" + str(apvs))
        try:
            if len(apvs) > 0:
                gc = apvs[0][0] * apvs[0][1] * side
        except:
                try:
                    gc = pvs[0][0] * pvs[0][1] * side
                except:
                    gc = None
        print( "gc =" + str(gc) )
            
    #end of tables
    returndoc = { "investment" : str(gc) }
    return returndoc




