import re
import codec

#with open('Luis_Fonsi._Despacito_utf8.txt') as fh: sf = fh.read().lower()

#print sf

fh1 = codecs.open('Luis_Fonsi._Despacito_utf8.txt', encoding='utf-8')
sf1 = fh1.read().lower()

# In UTF-8 \u2026 is a series of three dots, like this: “…”
x1 = re.findall(u'\w{1,20}|[\.\u2026\,\!\:]', sf1, flags=re.UNICODE)

for w in x1: print w, '  ',
