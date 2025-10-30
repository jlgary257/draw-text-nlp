import tensorflow as tf
import keras
from keras.src.legacy.preprocessing.text import Tokenizer as Tokenizer

sentence = ['I am boy','I am tall']

tokenizer = Tokenizer(num_words=100)

tokenizer.fit_on_texts(sentence)

print(tokenizer.to_json())
print(sentence)