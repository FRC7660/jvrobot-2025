# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2

from subsystems.CANDriveSubsystem import CANDriveSubsystem


# Command class to drive the robot based on joystick inputs
class DriveCommand(commands2.Command):
    def __init__(
        self,
        leftSpeed: lambda leftSpeed: leftSpeed,
        rightSpeed: lambda rightSpeed: rightSpeed,
        driveSubsystem: CANDriveSubsystem,
    ) -> None:
        self.driveSubsystem = driveSubsystem
        self.leftSpeed = leftSpeed
        self.rightSpeed = rightSpeed
        self.addRequirements(self.driveSubsystem)
        super().__init__()

    def initialize(self) -> None:
        pass

    def apply_exponential_curve (self, value, exponent=2):
        raw_value = value**exponent if value >= 0 else -(abs(value) ** exponent)
        max_value = 1 ** exponent 
        scaled_output = raw_value / max_value
        return scaled_output

    def execute(self) -> None:
        self.driveSubsystem.tankDrive(
            self.leftSpeed,
            self.rightSpeed

        )

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False
