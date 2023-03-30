import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('8-cat-66.h5')
classify = ['food/biological', 'brown glass', 'cardboard', 'green glass' ,'metal', 'paper', 'plastic', 'white glass']

def predict(img):
    pic = cv2.imread(img)
    pic = cv2.resize(pic, (30, 30))
    pic = np.reshape(pic, (-1, 30, 30, 3))
    return str(classify[model.predict([pic]).argmax()])








