#Preprocessing steps for Open NMT

#imports

import tensorflow as tf


#Tokenization

#By default, Keras’ Tokenizer will trim out all the punctuations
en_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
en_tokenizer.fit_on_texts(#raw_data_name)

# raw English sentences converted to integer sequences
data_en = en_tokenizer.texts_to_sequences(raw_data_en)


