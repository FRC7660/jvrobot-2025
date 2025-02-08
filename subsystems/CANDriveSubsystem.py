# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2
import wpilib
import wpilib.drive
from phoenix5 import WPI_VictorSPX, NeutralMode
import Constants

class CANDriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.leftLeader = WPI_VictorSPX(Constants.LEFT_LEADER_ID)  
        self.leftFollower = WPI_VictorSPX(Constants.LEFT_FOLLOWER_ID) 
        self.rightLeader = WPI_VictorSPX(Constants.RIGHT_LEADER_ID)  
        self.rightFollower = WPI_VictorSPX(Constants.RIGHT_FOLLOWER_ID) 

        self.leftLeader.configVoltageCompSaturation(12.0)
        self.leftFollower.configVoltageCompSaturation(12.0)
        self.rightLeader.configVoltageCompSaturation(12.0)
        self.rightFollower.configVoltageCompSaturation(12.0)

        self.leftLeader.setExpiration(0.250)
        self.leftFollower.setExpiration(0.250)
        self.rightLeader.setExpiration(0.250)
        self.rightFollower.setExpiration(0.250)

        self.leftLeader.setSafetyEnabled(True)
        self.leftFollower.setSafetyEnabled(True)
        self.rightLeader.setSafetyEnabled(True)
        self.rightFollower.setSafetyEnabled(True)

        self.leftLeader.enableVoltageCompensation(True)
        self.leftFollower.enableVoltageCompensation(True)
        self.rightLeader.enableVoltageCompensation(True)
        self.rightFollower.enableVoltageCompensation(True)

        self.rightLeader.setInverted(True)
        self.rightFollower.setInverted(True)

        self.leftFollower.follow(self.leftLeader)
        self.rightFollower.follow(self.rightLeader)

        self.leftLeader.setNeutralMode(NeutralMode.Brake)
        self.leftFollower.setNeutralMode(NeutralMode.Brake)
        self.rightLeader.setNeutralMode(NeutralMode.Brake)
        self.rightFollower.setNeutralMode(NeutralMode.Brake)

        self.drive = wpilib.drive.DifferentialDrive(self.leftLeader, self.rightLeader)
        
    def arcadeDrive(self, xSpeed: float, zRotation: float) -> None:
        self.drive.arcadeDrive(xSpeed, zRotation)
