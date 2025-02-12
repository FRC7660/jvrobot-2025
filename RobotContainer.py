import commands2
import commands2.button

import Constants
from subsystems.FuzzyBallIntake import FuzzyBallIntakeSubsystem
from subsystems.AutomaticPneumatics import AutomaticPneumatics
from subsystems.CANDriveSubsystem import CANDriveSubsystem
from subsystems.CANRollerSubsystem import CANRollerSubsystem

from commands.DriveCommand import DriveCommand
from commands.RollerCommand import RollerCommand
from commands.AutoCommand import AutoCommand
from commands.FuzzyBallIntake import FuzzyBallIntakeCommand
from commands.AutomaticPneumaticsCommand import AutomaticPneumaticsCommand


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
        self.fuzzyBallIntakeSubsystem = FuzzyBallIntakeSubsystem()
        self.automaticPneumatics = AutomaticPneumatics ()

        self.configureButtonBindings()

    def configureButtonBindings(self):
        self.driveSubsystem.setDefaultCommand(
            DriveCommand(
                lambda: -self.driverController.getLeftY(),
                lambda: -self.driverController.getRightX(),
                self.driveSubsystem,
            )
        )
     #   self.rollerSubsystem.setDefaultCommand(
        #    # RollerCommand(
        #         lambda: self.driverController.getRightTriggerAxis(),
        #         lambda: self.driverController.getLeftTriggerAxis(),
        #         self.rollerSubsystem,
        #     )
        # )
        self.driverController.a().whileTrue(
            RollerCommand(
            lambda: Constants.ROLLEY_THINGEY_EJECT_SPEED, 
            lambda: 0, 
            self.rollerSubsystem
            )
        )
        self.fuzzyBallIntakeSubsystem.setDefaultCommand(
            FuzzyBallIntakeCommand(
                lambda: self.driverController.getRightTriggerAxis(),
                lambda: self.driverController.getLeftTriggerAxis(),
                self.fuzzyBallIntakeSubsystem,
            )
        )
        self.automaticPneumatics.setDefaultCommand(
            AutomaticPneumaticsCommand(
                lambda: self.driverController.x(),
                self.automaticPneumatics
            )
        )


    def getAutonomousCommand(self) -> commands2.Command:
        return AutoCommand()
