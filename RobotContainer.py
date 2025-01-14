# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2
import commands2.button

import Constants
from subsystems.CANDriveSubsystem import CANDriveSubsystem
from subsystems.CANRollerSubsystem import CANRollerSubsystem

from commands.DriveCommand import DriveCommand
from commands.RollerCommand import RollerCommand
from commands.AutoCommand import AutoCommand


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self.driverController = commands2.button.CommandXboxController(
            Constants.DRIVER_CONTROLLER_PORT
        )
        self.operatorController = commands2.button.CommandXboxController(
            Constants.OPERATOR_CONTROLLER_PORT
        )
        self.driveSubsystem = CANDriveSubsystem()
        self.rollerSubsystem = CANRollerSubsystem()

        self.configureButtonBindings()

    # function to bind commands to buttons on the operator and driver controllers.
    def configureButtonBindings(self):
        self.driveSubsystem.setDefaultCommand(
            DriveCommand(
                lambda: -self.driverController.getLeftY(),
                lambda: -self.driverController.getRightX(),
                self.driveSubsystem,
            )
        )
        self.rollerSubsystem.setDefaultCommand(
            RollerCommand(
                lambda: self.operatorController.getRightTriggerAxis(),
                lambda: self.operatorController.getLeftTriggerAxis(),
                self.rollerSubsystem,
            )
        )
        self.operatorController.a().whileTrue(
            RollerCommand(
            lambda: Constants.ROLLER_MOTOR_EJECT_SPEED, 
            lambda: 0, 
            self.rollerSubsystem)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return AutoCommand()
