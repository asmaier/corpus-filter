import argparse


def extract_words(text):
    clean_text = "".join(c for c in text if c.isalpha() or c == " ")
    return clean_text.split()


def main(args):

    LENGTH = args.length
    SENTENCES = args.input
    FILTERED = args.output

    with open(SENTENCES, 'r') as infile:
        with open(FILTERED, "w") as outfile:
            for line in infile:
                sentence = line
                words = extract_words(sentence)
                number_of_words = len(words)

                if number_of_words and number_of_words <= LENGTH:
                    outfile.write(sentence)
                    outfile.flush()
                    print(number_of_words, sentence.strip())


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Sentence filter - filters a list of sentences according to length")
    parser.add_argument("length", type=int, help="Maximum length of sentences in number of words")
    parser.add_argument("input", type=str, help="Input file - list of sentences as txt or csv file (single column)")
    parser.add_argument("output", type=str, help="Output file - filtered list of sentences as txt file")
    args = parser.parse_args()

    main(args)
