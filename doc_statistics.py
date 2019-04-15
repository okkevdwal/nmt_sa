


"# Sentences:" len(doc)

"Vocabulary:" len(set(doc))

wordcounts = []
with open(filepath) as f:
    text = f.read()
    sentences = text.split('.')
    for sentence in sentences:
        words = sentence.split(' ')
        wordcounts.append(len(words))

sentences = len(sentences)
words = words
average_wordcount = sum(wordcounts)/len(wordcounts)