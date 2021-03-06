"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  #line = re.sub(r'# (.*)', r'<h1>\1</h1>', line) #I dont know why this regex catches ## and ###... its screwing everything up
  #return line
  if line[:2] == "# ":
    line = "<h1>" + line[2:] + "</h1>"
  return line

def convertH2(line):
  if line[:3] == "## ":
    line = "<h2>" + line[3:] + "</h2>"
  return line

def convertH3(line):
  if line[:4] == "### ":
    line = "<h3>" + line[4:] + "</h3>"
  return line

bq = False
for line in fileinput.input():
  line = line.rstrip()
  if line[0] == '>' and not bq:
    bq = True
    print "<blockquote>"
    line = line[1:].lstrip()
  elif line[0] == '>' and bq:
    line = line[1:].lstrip()
  elif bq and not line[0] == '>':
    bq = False
    print "</blockquote>"
  if line[0] != '>' and line[0] != '#':
    line = convertStrong(line)
    line = convertEm(line)
    print '<p>' + line + '</p>',
  else:
    line = convertH1(line)
    line = convertH2(line)
    line = convertH3(line)
    print line
  
  

