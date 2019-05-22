from keras import backend as K


class TensorGradient(object):
    def __init__(self, model):
        # See https://stackoverflow.com/questions/54566337/how-to-get-gradient-values-using-keras-backend-gradients
        self.gradients = K.gradients(model.output, model.input)
        self.sess = K.get_session()
        self.model = model

    def __call__(self, x):

        if len(x.shape) != 2:
            x = x.reshape(1, x.shape[0])
        # See https://stackoverflow.com/questions/54566337/how-to-get-gradient-values-using-keras-backend-gradients
        evaluated_gradients = self.sess.run(self.gradients[0], feed_dict={self.model.input: x})

        return evaluated_gradients