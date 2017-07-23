#!/usr/bin/env python
# -- coding: utf-8 --

import locale
import re
from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

#ambitious attempt to parse a whole transaction from string
def parseTransaction(x):
    y = 0
    try:
       tup = re.search(ur'(Sale|Purchase).*?([,\d]+).*?price.*?([£$€])(\d+(?:\.\d{2})?)', x).groups()
       if tup:
           if tup[0]== "Sale":
               side=0
           else:
               side=1
       vol=getvolume(tup[1])
       px=getprice(tup[3])
       gc=vol * px
       doc = {
               "vol" : vol,
               "px" : px,
               "gc" : gc
       }
    except:
        None
    return doc

def getVolume(x):
    y=0
    try:
        y = int(locale.atof(x))
    except:
        None
    return y

def getPrice(x):
    y =Decimal(0)
    try:
       #start off parsing as float but if major ccy symbol multiply 100
       y = locale.atof(x)
       tup = re.search(ur'([£$€])(\d+(?:\.\d+)?)', x).groups()
       if tup:
          y = tup[1] * 100
          return y
       else:
          tup = re.search(ur'(\d+(?:\.\d+)\s*p', x, re.IGNORECASE).groups()
          if tup:
              print(tup)
              y = Decimal(tup[0])
    except:
        None
    return y


def getDecimal(x):
    y = Decimal(0) 
    tup = re.search('([\.\d]+)', x).groups()
    if tup:
       y=Decimal(tup[0])
    return y

def getPrice2(x):
    y = Decimal(0)
    try:
        tup = re.search('([\.\d]+)', x).groups()
        if tup:
           y=Decimal(tup[0])
        if "£" in x:
           y *= 100
    except:
        None
    return y


def isPrice(x):
    if "£" in x:
        return True
    if "pence" in x:
        return True
    if "p" in x:
        return True
    return False

def isVolume(x):
    if "£" in x:
        return False
    if "pence" in x:
        return False 
    if "p" in x:
        return False
    tup = re.search('([\,\d]+)', x).groups()
    if tup:
        return True
    return False

def getSide(x):
    x.lower()
    print(x)
    if 'purchase' in x:
        return 1
    if 'aquisition' in x:
        return 1
    if 'sale' in x:
        return -1
    if 'disposal' in x:
        return -1
    if 'vesting' in x:
        return 1
    return 1

def getPricesAndVolumes(x):
    clean=[]
    for match in re.findall(u'(\d[\,\d\.]*).*?(\d[\.\d\,]*)', x):
        clean.append( (getDecimal(match[0]), getDecimal(match[1])) )
    return clean
    return x

def getAggPVs(x):
    clean=[]
    for match in re.findall(u'(\d[\,\d\.]*).*?(\d[\.\d\,]*)', x):
        clean.append( (getDecimal(match[0]), getDecimal(match[1])) )
    return clean
    return x
