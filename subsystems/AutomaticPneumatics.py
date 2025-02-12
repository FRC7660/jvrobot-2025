from wpilib import PneumaticsControlModule, PneumaticsModuleType, Solenoid
import Constants
import commands2


class AutomaticPneumatics(commands2.Subsystem):
    def __init__(self):
        self.pcm = PneumaticsControlModule(Constants.AUTOMATICPNEUMATICS_COMPRESSOR_ID)
        self.solenoid = Solenoid(
            PneumaticsModuleType.CTREPCM, Constants.AUTOMATICPNEUMATICS_SOLENOID_CHANNEL
            )
        self.pcm.enableCompressorAnalog(
            Constants.PRESSURE_LOW_VALUE, Constants.PRESSURE_HIGH_VALUE
        )
    def set_solenoid(self, state):
        self.solenoid.set(state)
         
    def toggle_solenoid(self):
        self.solenoid.toggle()