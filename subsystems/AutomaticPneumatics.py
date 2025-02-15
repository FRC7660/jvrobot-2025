from wpilib import PneumaticsControlModule, PneumaticsModuleType, Solenoid
import Constants
import commands2


class AutomaticPneumatics(commands2.Subsystem):
    def __init__(self):
        self.pcm = PneumaticsControlModule(Constants.AUTOMATICPNEUMATICS_COMPRESSOR_ID)
        self.solenoid_0 = Solenoid(
            Constants.AUTOMATICPNEUMATICS_COMPRESSOR_ID,
            PneumaticsModuleType.CTREPCM,
            Constants.AUTOMATICPNEUMATICS_SOLENOID_CHANNEL,
            )
        self.solenoid_1 = Solenoid(
            Constants.AUTOMATICPNEUMATICS_COMPRESSOR_ID,
            PneumaticsModuleType.CTREPCM, 
            Constants.AUTOMATICPNEUMATICS_SOLENOID_CHANNEL_1,
            )
        self.pcm.enableCompressorAnalog(
            Constants.PRESSURE_LOW_VALUE, Constants.PRESSURE_HIGH_VALUE
        )
    def set_solenoid_0(self, state):
        self.solenoid_0.set(state)
    
    def set_solenoid_1(self, state):
        self.solenoid_1.set(state)
         
    def toggle_solenoid(self):
        self.solenoid0.toggle()