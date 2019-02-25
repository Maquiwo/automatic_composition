from conductor import Conductor

class Tune:
    def __init__(self):
        self.conductor = Conductor()
    
    def play(self):
        return self.conductor.play()