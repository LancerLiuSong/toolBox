import tensorflow as tf
print(tf.__version__)

hello = tf.constant('Hello from tensorflow!')
print(tf.Session().run(hello))