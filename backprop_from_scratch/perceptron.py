import numpy as np
from eval import sigmoid

class Perceptron():
    """ Initializes a Perceptron.
        Passed to MLP.
        Methods:
            -   _forward_step     Calculates activation.
            -   _update           Updates neurons params.
    """


    def __init__(self, input_units, learning_rate = 1, activ_func = sigmoid):
        """ ## Parameters:
        
            -   input_units = input layer width
            -   learning_rate = param update rhythm
            -   activ_func = activation function
        """

        self.weights = np.random.randn(input_units) # assign random values to weights
        self.bias = np.random.randn(1)              # and bias on initialisation
        self.drive = np.nan
        self.alpha = learning_rate
        self.activation = activ_func
    


    def _forward_step(self, inputs):
        """ Calculates activation.
            
            ## Parameters:

            inputs = activations from earlier layer neurons
        """
        print(inputs)
        print(self.weights)
        self.drive = np.dot(inputs, self.weights) + self.bias
        return self.activation(self.drive)



    def _update(self, delta):
        """ Updates neurons params.

            ## Parameters:

            delta = error signal
        """

        # gradient calc
        gradient = delta * self.weights
        # param update
        self.weights -=  self.alpha * gradient
        self.bias -= self.alpha * delta