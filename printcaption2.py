# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:32:52 2020

@author: Johannah
"""

#”max_length” value would need to be changed for different dataset
#image file input is near the bottom, change file name accordingly 

from pickle import load
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.models import load_model

# extract features from each photo in the directory
def extract_features(filename):
        # load the model and remove final layer (for classifying)
        model = VGG16()
        model.layers.pop()
        model = Model(inputs=model.inputs, outputs=model.layers[-1].output)
        # load the photo
        image = load_img(filename, target_size=(224, 224))
        image = img_to_array(image)   # convert the image pixels to a numpy array
        image = img_to_array(image)
        # reshape data for the model
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        # prepare the image for the VGG model
        image = preprocess_input(image)
        # get features
        feature = model.predict(image, verbose=0)
        return feature

# map an integer to a word
def word_for_id(integer, tokenizer):
   for word, index in tokenizer.word_index.items():
                if index == integer:
                        return word
                        return None

# generate a description for an image
def generate_desc(model, tokenizer, photo, max_length):
        #add token to start the generation 
        in_text = 'startseq'
        # iterate over length of the sequence
        for i in range(max_length):
                # integer encode input sequence
                sequence = tokenizer.texts_to_sequences([in_text])[0]
                # pad input
                sequence = pad_sequences([sequence], maxlen=max_length)
                # predict next word
                yhat = model.predict([photo,sequence], verbose=0)
                # convert probability to integer
                yhat = argmax(yhat)
                # map integer to word
                word = word_for_id(yhat, tokenizer)
                # stop if we cannot map the word
                if word is None:
                    break
                # append as input for generating the next word
                in_text += ' ' + word
                # stop if end of the sequence
                if word == 'endseq':
                    break
                return in_text # load the tokenizer

tokenizer = load(open('tokenizer.pkl', 'rb'))
# the max sequence length (from training)
max_length = 34
# load the model
model = load_model('model-ep002-loss4.262-val_loss4.184.h5')
# load and prepare the photograph
photo = extract_features('example_image10.jpg')
#generate and print description for new image
description = generate_desc(model, tokenizer, photo, max_length)
print(description)
