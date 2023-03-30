import tensorflow as tf
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split



def main():
    images, labels = load_data('dataset')
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=0.5
    )

    model = make_model()

    model.fit(x_train, y_train, epochs=50)

    model.evaluate(x_test,  y_test, verbose=2)


    model.save("modelX.h5")



def make_model():
    model = tf.keras.Sequential()

    model.add(tf.keras.layers.Conv2D(512, (3, 3), activation="relu", input_shape=((30, 30, 3))))
    model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(256, (3, 3), activation="relu"))
    model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2)))



    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(128, activation="relu"))


    model.add(tf.keras.layers.Dropout(0.3))

    # Output Layer
    model.add(tf.keras.layers.Dense(8, activation="softmax"))

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

def load_data(data_dir):

    images = []
    labels = []

    categories = os.listdir(data_dir)
    for label in categories:
        pictures = os.listdir(os.path.join(data_dir, label))
        for pic in pictures:
            img = cv2.imread(os.path.join(data_dir, label, pic))
            resized_img = cv2.resize(img, (30, 30))
            images.append(resized_img)
            labels.append(int(label))
        

    return (images, labels)


if __name__ == "__main__":
    main()