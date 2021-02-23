# corpus-filter
This tool allows to filter a corpus of sentences by a list of lemmas.
Such a tool can be very useful to generate a text limited to only
specific lemmas/vocabulary, e.g. you can filter for sentences
with only the 1000 most common words/lemmas. This can be used
for writing books teaching a language to beginners or kids 
(or presidents) with limited vocabulary.    

At the moment the tool only supports the russian language.
 
We are making use of [stanza](https://stanfordnlp.github.io/stanza/) 
package (formerly known as StandfordNLP).
The russian lemmatizer of this package however is only a wrapper around
[pymorph2](https://github.com/kmike/pymorphy2).

See also:
- https://guitton.co/posts/spacy-stanza-russian-swedish/
- https://stackoverflow.com/a/60741103/179014

# Installation

    pipenv install
    pipenv shell

# Usage
    usage: corpus_filter.py [-h] lemmas input output

    Corpus filter - filters a corpus of sentences according to a white list of
    lemmas.

    positional arguments:
      lemmas      Lemmas file - white list of lemmas as txt or csv file (single
                  column)
      input       Input file - list of sentences as txt or csv file (single
                  column)
      output      Output file - filtered list of sentences as txt file

    optional arguments:
      -h, --help  show this help message and exit

# Example

    python corpus_filter.py lemmas_russian.txt sentences_russian.txt output.txt

