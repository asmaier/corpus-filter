import csv
import re
import argparse
import pathlib

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

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Corpus filter - filters a corpus of sentences according to a white list of lemmas.")
	parser.add_argument("lemmas", type=str, help="Lemmas file - white list of lemmas as txt or csv file (single column)")
	parser.add_argument("input", type=str, help="Input file - list of sentences as txt or csv file (single column)")
	parser.add_argument("output", type=str, help="Output file - filtered list of sentences as txt file")
	args = parser.parse_args()
	
	LEMMAS = args.lemmas
	SENTENCES = args.input
	FILTERED = args.output

	stanza.download('ru')  # will take a while

	snlp = stanza.Pipeline(lang="ru")
	nlp = StanzaLanguage(snlp)

	lemmas = set()
	with open(LEMMAS, 'r') as infile:
		file_type = pathlib.Path(LEMMAS).suffix
		print("File type lemmas", file_type)
		if file_type == ".csv":
			reader = csv.reader(infile, delimiter=',', quotechar='"')
			for row in reader:
				lemmas.add(row[0])
		if file_type == ".txt":
			for row in infile:
				lemmas.add(row.strip())

	# print(lemmas)

	count = 0
	with open(SENTENCES, 'r') as infile:
		file_type = pathlib.Path(SENTENCES).suffix
		print("File type sentences", file_type)
		reader = None
		if file_type == ".csv":
			reader = csv.reader(infile, delimiter=',', quotechar='"')
			with open(FILTERED, "w") as outfile:
				for row in reader:
					sentence = row.strip()
					count+=1
					if has_only_lemmas(sentence,lemmas):
						outfile.write(sentence + "\n")
						outfile.flush()				
						print(count, sentence)

		if file_type == ".txt":
			reader = infile				
			with open(FILTERED, "w") as outfile:
				for row in reader:
					sentence = row.strip()
					count+=1
					if has_only_lemmas(sentence,lemmas):
						outfile.write(sentence + "\n")
						outfile.flush()				
						print(count, sentence) 
		
		

