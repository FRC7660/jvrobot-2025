# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2
import wpilib
import wpilib.drive
from phoenix5 import WPI_TalonSRX, NeutralMode
import Constants
from wpilib import RobotBase

class CANDriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.leftLeader = WPI_TalonSRX(Constants.LEFT_LEADER_ID)  
        self.leftFollower = WPI_TalonSRX(Constants.LEFT_FOLLOWER_ID) 
        self.rightLeader = WPI_TalonSRX(Constants.RIGHT_LEADER_ID)  
        self.rightFollower = WPI_TalonSRX(Constants.RIGHT_FOLLOWER_ID) 

        self.leftLeader.configVoltageCompSaturation(12.0)
        self.leftFollower.configVoltageCompSaturation(12.0)
        self.rightLeader.configVoltageCompSaturation(12.0)
        self.rightFollower.configVoltageCompSaturation(12.0)

        self.leftLeader.setExpiration(9.9 * 10 ** 9)
        self.leftFollower.setExpiration(9.9 * 10 ** 9)
        self.rightLeader.setExpiration(9.9 * 10 ** 9)
        self.rightFollower.setExpiration(9.9 * 10 ** 9)

        if RobotBase.isSimulation():
            self.leftLeader.setSafetyEnabled(False)
            self.leftFollower.setSafetyEnabled(False)
            self.rightLeader.setSafetyEnabled(False)
            self.rightFollower.setSafetyEnabled(False)
        else:
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

    def tankDrive(self, leftSpeed: float, rightSpeed: float) -> None:
        self.drive.tankDrive(leftSpeed, rightSpeed, False)
