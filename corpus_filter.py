import csv
import re

import stanza
from spacy_stanza import StanzaLanguage


def has_only_lemmas(text, lemmas):
	clean_text = "".join(c for c in text if c.isalpha() or c == " ")
	clean_text_2 = " ".join(clean_text.split())

	doc = nlp(clean_text_2)

	for token in doc:
#       	print(token, token.lemma_)
        	if token.lemma_ not in lemmas:
                	return False
	
#	print(" ".join([token.lemma_ for token in doc]))
	return True


stanza.download('ru')  # will take a while

snlp = stanza.Pipeline(lang="ru")
nlp = StanzaLanguage(snlp)

lemmas = set()
with open('lemmas_russian.csv', 'r') as infile:
	reader = csv.reader(infile, delimiter=',', quotechar='"')
	for row in reader:
		lemmas.add(row[0])

count = 0
with open('sentences_russian.csv', 'r') as infile:
	reader = csv.reader(infile, delimiter=',', quotechar='"')
	with open("filtered_russian.csv", "w") as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='"')
		for row in reader:
			sentence = row[0]
			count+=1
			if has_only_lemmas(row[0],lemmas):
				writer.writerow([sentence])
				outfile.flush()				
				print(count, sentence) 
	

# text = "Андре́й Серге́евич Арша́вин (род. 29 мая 1981[4], Ленинград) — российский футболист, бывший капитан сборной России, заслуженный мастер спорта России (2008)."
# clean_text = "".join(c for c in text if c.isalpha() or c == " ")
# clean_text_2 = " ".join(clean_text.split())

# doc = nlp(clean_text_2)

# for token in doc:
#	print(token, token.lemma_)
#	if token.lemma_ not in lemmas:
#		print(token.lemma_)
#	# print(token, token.lemma, token.lemma_)
