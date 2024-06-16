import csv
from collections import Counter
import argparse
import pathlib

import stanza
from spacy_stanza import StanzaLanguage


def contains_only_lemmas(tokens, lemmas):
	for token in tokens:
		if token.lemma_ not in lemmas:
			return False
	return True


def extract_tokens(text):
	clean_text = "".join(c for c in text if c.isalpha() or c == " ")
	clean_text_2 = " ".join(clean_text.split())
	doc = nlp(clean_text_2)
	return doc


def get_lines(file, file_type):
	lines = []
	if file_type == ".csv":
		reader = csv.reader(file, delimiter=',', quotechar='"')
		for row in reader:
			lines.append(row[0].strip())
	if file_type == ".txt":
		for row in file:
			lines.append(row.strip())
	return lines


def main(args):
	LEMMAS = args.lemmas
	SENTENCES = args.input
	FILTERED = args.output

	lemmas = set()
	with open(LEMMAS, 'r') as infile:
		file_type = pathlib.Path(LEMMAS).suffix
		print("File type lemmas", file_type)
		for line in get_lines(infile, file_type):
			lemmas.add(line)
	# print(lemmas)

	count = 0
	used_lemmas = Counter()
	with open(SENTENCES, 'r') as infile:
		file_type = pathlib.Path(SENTENCES).suffix
		print("File type sentences", file_type)

		with open(FILTERED, "w") as outfile:
			for line in get_lines(infile, file_type):
				sentence = line
				count += 1
				tokens = extract_tokens(sentence)

				if contains_only_lemmas(tokens, lemmas):
					outfile.write(sentence + "\n")
					outfile.flush()
					print(count, sentence)

					for token in tokens:
						used_lemmas[token.lemma_] += 1

	with open("used_lemmas.log", "w") as statfile:
		for lemma in sorted(used_lemmas):
			statfile.write(lemma + " " + str(used_lemmas[lemma]) + "\n")

	with open("unused_lemmas.log", "w") as statfile:
		for lemma in lemmas:
			if lemma not in used_lemmas:
				statfile.write(lemma + "\n")


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Corpus filter - filters a corpus of sentences according to a white list of lemmas.")
	parser.add_argument("lemmas", type=str, help="Lemmas file - white list of lemmas as txt or csv file (single column)")
	parser.add_argument("input", type=str, help="Input file - list of sentences as txt or csv file (single column)")
	parser.add_argument("output", type=str, help="Output file - filtered list of sentences as txt file")
	args = parser.parse_args()

	stanza.download('ru')  # will take a while
	snlp = stanza.Pipeline(lang="ru")
	nlp = StanzaLanguage(snlp)

	main(args)


