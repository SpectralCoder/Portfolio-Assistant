import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# import colorama 
# colorama.init()
# from colorama import Fore, Style, Back

import random
import pickle

with open(dir_path + '/' + 'intents.json') as file:
    data = json.load(file)


def chat(inp):
    # load trained model
    model = keras.models.load_model(dir_path + '/' +'chat_model')

    # load tokenizer object
    with open(dir_path + '/' +'tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open(dir_path + '/' +'label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    # print( "User: ", end="")

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            # print( "ChatBot:", np.random.choice(i['responses']))
            return np.random.choice(i['responses'])

    # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

# print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
# chat()
