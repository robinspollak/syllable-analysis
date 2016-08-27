# Anaylsis on Number of Syllables in Frequently Used Words: Comparing English and Spanish
This project explores the proportion of words in English and Spanish that have different numbers of syllables.
It uses the 20,000 most frequently used words in the two languages ([English](https://github.com/first20hours/google-10000-english/blob/master/20k.txt) and [Spanish](https://es.wiktionary.org/wiki/Ap%C3%A9ndice:Palabras_m%C3%A1s_frecuentes_del_espa%C3%B1ol) respectively).
It uses algorithms based on linguistic rules provided for [English](http://www.phonicsontheweb.com/syllables.php) and [Spanish](http://www.spanishdict.com/topics/show/116) and the findings
are published on [Medium](https://medium.com/@RobinPollak/syllabification-is-a-fun-word-does-english-use-more-one-syllable-words-than-spanish-f1c28bed98d).

Code relevant to the splitting of words in the two languages are located in [english.py](https://github.com/robinspollak/syllable-analysis/blob/master/english.py) and [spanish.py](https://github.com/robinspollak/syllable-analysis/blob/master/spanish.py). The ingestion of the lists of words and the counting of syllables occurs in [main.py](https://github.com/robinspollak/syllable-analysis/blob/master/main.py).

Questions and comments can be directed to [robin@pollak.io](mailto:robin@pollak.io) and improvements to the syllabification algorithms are greatly appreciated and can be opened as pull requests. 
