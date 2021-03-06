import tensorflow.compat.v1.keras.backend as K
import tensorflow
import tensorflow.keras.backend

class TensorGradient(object):
    def __init__(self, model):
        # See https://stackoverflow.com/questions/54566337/how-to-get-gradient-values-using-tensorflow.keras-backend-gradients
        #self.gradients = K.gradients(model.output, model.input)
        #self.sess = K.get_session()
        self.model = model

    def __call__(self, x):

        if len(x.shape) != 2:
            x = x.reshape(1, x.shape[0])
        x = tensorflow.Variable(x, dtype=tensorflow.float32)
        # See https://stackoverflow.com/a/59147703
        with tensorflow.GradientTape() as tape:
            predictions = self.model(x)
        evaluated_gradients = tape.gradient(predictions, x)

        return tensorflow.keras.backend.eval(evaluated_gradients)
