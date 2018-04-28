import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize, imshow
import tensorflow as tf

def init():
    json_file = open('model_json.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    #load weights
    loaded_model.load_weights("model_og.h5")
    print("loaded from the disk")

    #compile
    loaded_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

    graph = tf.get_default_graph()

    return loaded_model, graph
