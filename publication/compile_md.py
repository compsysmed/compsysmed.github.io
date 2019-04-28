#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import bibtexparser
import re

with open(sys.argv[1], 'r') as bibf:
    bibdb = bibtexparser.load(bibf)

entries = bibdb.get_entry_list()[0]
if 'year' in entries:
    y = entries['year']
else:
    y = '1900'
if 'month' in entries:
    mdict = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
             'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    if entries['month'] in mdict:
        m = mdict[entries['month']]
    else:
        m = m
else:
    m = '01'
if 'day' in entries:
    d = entries['day']
else:
    d = '01'
with open(sys.argv[2], 'w') as mdf:
    mdf.write('+++\n')
    mdf.write('title = "%s"\n'%re.sub('[{}]','',entries['title']))
    mdf.write('date = %s-%s-%s\n'%(y,m,d))
    authors = ['%s'%a.rstrip() for a in entries['author'].split(' and ')]
    authors = ['%s %s'%(a.split(', ')[1], a.split(', ')[0]) for a in authors]
    authstr = 'authors = ["%s"]\n'%'", "'.join(authors)
    mdf.write(authstr)
    mdf.write('publication_types = ["2"]\n')
    mdf.write('selected = false\n')
    mdf.write('publication = "*%s*"\n'%entries['journal'])
    mdf.write('doi = "%s"\n'%entries['doi'])
    mdf.write('pmid = "%s"\n'%entries['pmid'])
    mdf.write('+++\n')

