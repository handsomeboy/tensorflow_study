import tensorflow as tfdef print_device_infomation():    a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')    b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')    c = a + b    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))    print(sess.run(c))'''add: (Add): /job:localhost/replica:0/task:0/cpu:0b: (Const): /job:localhost/replica:0/task:0/cpu:0a: (Const): /job:localhost/replica:0/task:0/cpu:0[ 2.  4.  6.]'''def set_device():    with tf.device("/cpu:0"):        a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')        b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')    with tf.device("/cpu:0"):        c = a + b    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))    print(sess.run(c))if __name__ == '__main__':    set_device()