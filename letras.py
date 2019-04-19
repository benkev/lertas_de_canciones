import re
import codecs
import numpy as np, matplotlib.pyplot as plt

#with open('Luis_Fonsi._Despacito_utf8.txt') as fh: sf = fh.read().lower()

#print sf

#with codecs.open('Luis_Fonsi._Despacito_utf8.txt', encoding='utf-8') as fh1:
with codecs.open('Don_Quixote.iso-8859-1.txt', encoding='iso-8859-1') as fh1:
	letra = fh1.read().lower()
#
# Ellipsis ("..."but a single symbol): \u2026  
# EM DASH (long dash, "tiret") \u2014
# Upside-down "?": \u00bf
# Upside-down "!": \u00a1
# Left single quotation mark:  \u2018
# Right single quotation mark: \u2019
# Left double quotation mark:  \u201c
# Right double quotation mark: \u201d
#

#
# Create list of words and punctuation marks
#
lst = re.findall(u'\w{1,20}|[\.\u2026\,\!\u00a1\?\u00bf\:\;\-\u2014]' \
				 u'\"\u201c\u201d\'\u2018\u2019',
				 letra, flags=re.UNICODE)

word_freq = {}

for word in lst:
	# print word, '  ',
	cnt = word_freq.get(word, 0)     # cnt = freq[word] if word in freq, else 0
	word_freq[word] = cnt + 1

words = word_freq.keys() 
wf_desc = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

for word, freq in wf_desc:
    print '%10s\t %4d' % (word, freq)	



#
# Ellipsis ("...", but a single symbol): \u2026  
# EM DASH (long dash, "tiret") \u2014
# Upside-down "?": \u00bf
# Upside-down "!": \u00a1
# Left single quotation mark:  \u2018
# Right single quotation mark: \u2019
# Left double quotation mark:  \u201c
# Right double quotation mark: \u201d
#

#
# Create list of words and punctuation marks
#
lst = re.findall(u'\w{1,20}|[\.\u2026\,\!\u00a1\?\u00bf\:\;\-\u2014]' \
				 u'\"\u201c\u201d\'\u2018\u2019',
				 letra, flags=re.UNICODE)

word_freq = {}

for word in lst:
	# print word, '  ',
	cnt = word_freq.get(word, 0)     # cnt = freq[word] if word in freq, else 0
	word_freq[word] = cnt + 1

words = word_freq.keys() 
wf_des = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

wfreqs = np.array(map(lambda x: x[1], wf_des), dtype=np.int)

# for word, freq in wf_des[:100]:
#     print '%10s\t %4d' % (word, freq)	

plt.plot(wfreqs[:1000], lw=2); plt.grid(1)


dword_freq = {}

nw = len(lst)
for iw in xrange(nw):
	dwkey = lst[iw-1] + ' ' + lst[iw]  # Two adjacent words
	cnt = dword_freq.get(dwkey, 0)
	dword_freq[dwkey] = cnt + 1
	
dwords = dword_freq.keys() 
dwf_des = sorted(dword_freq.items(), key=lambda x: x[1], reverse=True)

dwfreqs = np.array(map(lambda x: x[1], dwf_des), dtype=np.int)

for dword, freq in dwf_des[:1000]:
    print '%4d %10s' % (freq, dword)	

plt.figure()
plt.plot(dwfreqs[:1000], lw=2); plt.grid(1)


