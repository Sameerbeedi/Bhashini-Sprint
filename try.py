import tensorflow as tf
from tensorflow import keras
model = tf.keras.models.load_model("emotion_recognition\model_v1_0.68_0.74.h5")
model.summary()
