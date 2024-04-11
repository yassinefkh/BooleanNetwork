import random

class BooleanNetworkVertex:
    def __init__(self, state, inputs, bool_func_index):
        self.state = state
        self.inputs = inputs
        self.bool_func_index = bool_func_index
