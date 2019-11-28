import nltk

# bigram example
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
print(list(nltk.bigrams(sent)))