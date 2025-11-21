from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow will be even better."
blob = TextBlob(text)

print(blob.correct())
print(blob.sentences)
print(blob.tags)

print(blob.words)

print(blob.noun_phrases)

print(blob.sentiment)