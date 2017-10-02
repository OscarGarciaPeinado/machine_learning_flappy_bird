# coding: utf-8

import tensorflow as tf


class Perceptron:
    num_input = 2
    n_hidden_layer_1 = 6
    num_classes = 2
    weights = {
        'h1': tf.Variable(tf.random_normal([num_input, n_hidden_layer_1])),
        'out': tf.Variable(tf.random_normal([n_hidden_layer_1, num_classes]))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([n_hidden_layer_1])),
        'out': tf.Variable(tf.random_normal([num_classes]))
    }

    X = tf.placeholder("float", [None, num_input])

    def __init__(self):
        self.logits = self.neural_net(self.X)

    def neural_net(self, x):
        layer_1 = tf.add(tf.matmul(x, self.weights['h1']), self.biases['b1'])
        out_layer = tf.matmul(layer_1, self.weights['out']) + self.biases['out']
        return out_layer

    def predict(self, distance_x, distance_y):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

        return tf.nn.softmax(self.logits)
