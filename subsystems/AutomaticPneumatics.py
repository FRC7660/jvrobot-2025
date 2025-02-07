from wpilib import PneumaticsControlModule, Solenoid
class PneumaticsSubsystem:
    def __init__(self, pcm_module, solenoid_channel):
        self.pcm = PneumaticsControlModule(pcm_module)
        self.solenoid = Solenoid(self.pcm, solenoid_channel)
    def set_solenoid(self, state):
        self.solenoid.set(state)