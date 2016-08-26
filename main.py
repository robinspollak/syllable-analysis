# -*- coding: utf-8 -*-   
import codecs

from english import english_syllabify
from spanish import *

englishWords = open('english-words.txt')
englishSyllableDict = {}

for line in englishWords:
	word = unicode(line.strip())
	numSyllables = english_syllabify(word)
	if numSyllables in englishSyllableDict:
		englishSyllableDict[numSyllables] += 1
	else:
		englishSyllableDict[numSyllables] = 1

print englishSyllableDict
del englishSyllableDict[0]
print 'Total number counted: %d' % (sum(englishSyllableDict.values()))

spanishWords = codecs.open("spanish-words.txt", "r", "utf-8")
spanishSyllableDict = {}

for line in spanishWords:
	word = unicode(line.strip().lower())
	numSyllables = len(spanish_syllabify(word))
	if numSyllables in spanishSyllableDict:
		spanishSyllableDict[numSyllables] += 1
	else:
		spanishSyllableDict[numSyllables] = 1

print spanishSyllableDict
del spanishSyllableDict[0]
print 'Total number counted: %d' % (sum(spanishSyllableDict.values()))



