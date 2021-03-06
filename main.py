# -*- coding: utf-8 -*-   
import codecs

from english import english_syllabify
from spanish import *

englishWords = open('english-words.txt')
englishSyllableDict = {}

for line in englishWords:
	word = unicode(line.strip())
	numSyllables = english_syllabify(word)
	if numSyllables > 0:
		if numSyllables in englishSyllableDict:
			englishSyllableDict[numSyllables] += 1
		else:
			englishSyllableDict[numSyllables] = 1

print englishSyllableDict
totalEnglishWords = sum(englishSyllableDict.values())
print 'Total number of words with >0 syllables counted %d' % totalEnglishWords

spanishWords = codecs.open("spanish-words.txt", "r", "utf-8")
spanishSyllableDict = {}

for line in spanishWords:
	totalSpanishWords = sum(spanishSyllableDict.values())
	if totalSpanishWords >= totalEnglishWords:
		break
	word = unicode(line.strip().lower())
	numSyllables = len(spanish_syllabify(word))
	if numSyllables > 0:
		if numSyllables in spanishSyllableDict:
			spanishSyllableDict[numSyllables] += 1
		else:
			spanishSyllableDict[numSyllables] = 1

print spanishSyllableDict
print 'Total number of words with >0 syllables counted: %d' % (totalSpanishWords)



