# -*- coding: utf-8 -*-
import io, sys
filename = sys.argv[1]
drek = {u'“': '"', u'”': '"', u"’": "'", u"‘": "'", u'—': '-', u'−': '-'}
with io.open(filename,'r',encoding='utf8') as t:
  text = t.read()
for key in drek.keys():
  text = text.replace(key, drek[key])
filename = 'cleaned-' + filename
with open(filename, 'w') as f:
    f.write(text)
