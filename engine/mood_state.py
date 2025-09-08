class MoodState:
    def __init__(self):
        self.stimulation = 0.3
        self.intensity = 0.5
        self.energy = 0.5
        self.curiosity = 0.4
        self.calmness = 0.5
        self.numbness = 0.1
        self.obsession = 0.2
        self.performance = 0.4
        self.withdrawal = 0.1
        self.control = 0.5
        self.attention = 0.4

    def clip(self):
        for attr in vars(self):
            setattr(self, attr, min(1.0, max(0.0, getattr(self, attr))))
