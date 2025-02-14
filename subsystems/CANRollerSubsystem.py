# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.F

import commands2
from phoenix5 import WPI_VictorSPX, NeutralMode

import Constants


class CANRollerSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
  
        self.rolleyThingey = WPI_VictorSPX(Constants.ROLLEY_THINGEY_ID) 

        self.rolleyThingey.configVoltageCompSaturation(12.0)

        # self.rolleyThingey.setExpiration(0.250)

        self.rolleyThingey.setSafetyEnabled(True)

        self.rolleyThingey.enableVoltageCompensation(True)

        self.rolleyThingey.setNeutralMode(NeutralMode.Brake)

    # function to run the roller with joystick inputs
    def runRoller(self, forward: float, reverse: float) -> None:
        self.rolleyThingey.set(forward - reverse)
