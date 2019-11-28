import nltk
nltk.download('gutenberg') # for this example you need the gutenberg korpora
nltk.download('words') # for this example you need the words korpora

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

result = unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
print(result)