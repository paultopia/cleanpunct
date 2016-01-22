# -*- coding: utf-8 -*-
drek = {u'“': '"', u'”': '"', u"’": "'", u"‘": "'", u'—': '-', u'−': '-', u'…': '...'}
def clean(text):
  for key in drek.keys():
    text = text.replace(key, drek[key])
  return text

def cleanFile(filename):
  import io
  with io.open(filename,'r',encoding='utf8') as t:
    text = t.read()
  newtext = clean(text)
  return newtext

def diskClean(filename):
  newtext = cleanFile(filename)
  filename = 'cleaned-' + filename
  with open(filename, 'w') as f:
    f.write(newtext)
  return filename

if __name__ == '__main__':
  import sys
  filename = sys.argv[1]
  diskClean(filename)
