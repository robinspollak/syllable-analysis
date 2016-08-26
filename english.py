# -*- coding: utf-8 -*-   
test_words = [u'could', u'great', u'united', u'hotel', u'real', u'f', u'item', u'international', u'center', u'ebay']

def english_syllabify(word):
	vowels = u'aeiouy'
	'''
	counts number of syllables in an english word
	inspired by http://www.phonicsontheweb.com/syllables.php
	'''
	numVowels = 0
	afterVowel = False
	for char in word:
		if char in vowels:
			if not afterVowel: # don't count dipthongs
				numVowels += 1
				afterVowel = True
		else:
			afterVowel = False
	if (len(word) > 1 and word[-1] == "e"):
	   numVowels -= 1
	return numVowels



