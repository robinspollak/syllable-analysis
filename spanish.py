# -*- coding: utf-8 -*-    
strong_vowels = [u'a', u'e', u'o', u'á', u'à', u'ã', u'â', u'é', u'è', u'ó', u'ò', u'í', u'ú', u'ù']
weak_vowels = [u'i', u'u', u'y', u'ü']
vowels = strong_vowels + weak_vowels
single_consonants = [u'b', u'c', u'd', u'f', u'g', u'h', u'j', u'k', u'l', u'm', u'n', \
			  u'ñ', u'p', u'q', u'r', u'rr', u's', u't', u'v', u'w', u'x', u'y', u'z']
consonant_pairs = [u'bl', u'br', u'ch', u'cl', u'cr', u'dr', u'fl', u'fr', u'gl', u'gr', u'll', u'pl', u'pr', u'qu', u'rr', u'tr']
consonants = single_consonants + consonant_pairs
all_chars = strong_vowels + weak_vowels + consonants

test_list = [u'sábana', u'gato', u'casa', u'toalla', u'feo', u'iguana', u'reina', u'tío',
			 u'ciudad', u'creer', u'mano', u'oro', u'mesa', u'cuando', u'alcanzar', u'costa',
			 u'éxito', u'sombrillo', u'clave', u'trabajo', u'aplicar', u'frequente', u'hecho',
			 u'amarillo', u'carro', u'interrelacionado', u'enloquecer', u'merengue', u'atlántico']

def into_characters(word):
	character_list = []
	i = 0
	while i < len(word):
		if word[i] == 'h':
			i += 1
			continue
		if word[i:i+2] in consonant_pairs:
			character_list.append(word[i:i+2])
			i += 2
		elif word[i] in all_chars:
			if word[i] == u'x':
				character_list.append(u'k')
				character_list.append(u's')
			character_list.append(word[i])
			i += 1
		else:
			print word[i]
			raise Exception('Character %s not included in character list.' % (word[i])) 
	return character_list

def identify_syllable(character_list):
	'''
	accepts a list of characters, finds the first syllable
	and returns the syllable and the rest of the list
	'''
	first = character_list[0]
	second = character_list[1]
	third = character_list[2]
	rest = character_list[3::]
	if first in consonants:
		if (second in strong_vowels and third in weak_vowels) or\
		   (second in weak_vowels and third in strong_vowels):
		   	if len(rest) >= 1 and rest[0] in consonants and rest[1] in consonants:
				return (first + second + third + rest[0], rest[1::])
			else:
				return (first + second + third, rest)
		elif second in vowels:
			if rest and third in consonants and rest[0] in consonants:
				return (first + second + third, rest)
			else:
				return (first + second, [third] + rest)
		else:
			return (first, [second] + [third] + rest)
	else:
		if first in strong_vowels:
			if second in weak_vowels and third in consonants:
				return (first + second + third, rest)
			elif second in strong_vowels:
				return (first , [second] + [third] + rest)
			else:
				return (first + second, [third] + rest)			
		else:
			if second in vowels and third in consonants:
				return (first + second + third, rest)
			else:
				return (first + second, [third] + rest)

def spanish_syllabify(word):
	'''
	splits a spanish word into syllables
	reference: http://www.spanishdict.com/topics/show/116
	'''
	character_list = into_characters(word)
	syllables = []
	i = 0
	while len(character_list):
		if len(character_list) == 1 and character_list[0] in consonants:
			if len(syllables):
				syllables[-1] += character_list[0]
			else:
				syllables.append(character_list[0])
			break
		try:
			syllable, character_list = identify_syllable(character_list)
			syllables.append(syllable)
		except IndexError:
			syllables.append("".join(character_list))
			character_list = []
	return syllables