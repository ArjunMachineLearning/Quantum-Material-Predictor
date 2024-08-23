import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_dim, output_dim):
    model = models.Sequential()
    model.add(layers.Dense(128, activation='relu', input_shape=(input_dim,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(output_dim, activation='linear'))
    model.compile(optimizer='adam', loss=custom_loss)
    return model

def custom_loss(y_true, y_pred):
    penalty = tf.reduce_mean(tf.square(tf.maximum(0.0, y_pred - y_true)))
    return tf.reduce_mean(tf.losses.mean_squared_error(y_true, y_pred) + penalty)
