from random import uniform

class Neuron():
    def __init__(self, input_count: int, output_count: int, mask: str):
        if input_count <= 0 or output_count <= 0:
            raise ValueError(f"[init] Wrong connection count: {input_count}!")
        self.input_count = input_count
        self.output_count = output_count

        if mask not in ["relu", "tanh", "sigm"]:
            raise ValueError(f"chosen mask {mask} not known [relu, tanh, sigm]")
        self.mask = mask

        self.weights = [1 for x in range(self.input_count)]
        self.bias = 0

        
    def calculate(self, signal: float, connection_idx: int):
        try:
            return signal*self.weights[connection_idx] + self.bias
        except IndexError:
            print(f"[calc] Wrong connection index: {connection_idx}!")
        except Exception as e:
            print(f"[calc] Error: {e}")
    
    def randomize(self, mutation: float):
        self.weights = [x*(1+uniform(-mutation, mutation)) for x in self.weights]
        self.bias = self.bias*(1+uniform(-mutation, mutation)) + uniform(-mutation, mutation)

    def present(self):
        print(self.weights, self.bias, self.mask)

class Layer():
    def __init__(self, neuron_count: int, mask: str, input_count: int, output_count: int):
        self.neuron_count = neuron_count
        self.mask = mask

        self.neurons = []
        for i in range(self.neuron_count):
            neuron = Neuron(input_count, output_count, mask)
            self.neurons.append(neuron)
    
    def randomize(self, mutation: float):
        [x.randomize(mutation) for x in self.neurons]

    def present(self):
        print("Layer: ")
        [x.present() for x in self.neurons]
    



class Network():
    def __init__(self, input_count: int, output_count: int, hidden_struct: list):
        self.input_count = input_count
        self.output_count = output_count
        self.hidden_struct = hidden_struct

    def train(self):
        pass

def main():
    test = Layer(3, "relu", 4, 3)
    test.present()
    test.randomize(0.01)
    test.present()
    test.randomize(0.005)
    test.present()
    

if __name__ == "__main__":
    main()