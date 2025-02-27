import commands2
import commands2.button
import Constants
from wpilib import RobotBase, AnalogInput
from wpilib.simulation import DriverStationSim
from cscore import CameraServer

from networktables import NetworkTables

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
        if RobotBase.isSimulation():
            DriverStationSim.setJoystickButtonCount(
                Constants.LEFT_CONTROLLER_PORT, 10
            )
            DriverStationSim.setJoystickAxisCount(Constants.LEFT_CONTROLLER_PORT, 10)
            DriverStationSim.notifyNewData()
            NetworkTables.initialize(server='localhost')
        else:
            NetworkTables.initialize(server='10.76.60.2')
        self.sd = NetworkTables.getTable('SmartDashboard')
        CameraServer.startAutomaticCapture()
        
        self.leftController = commands2.button.CommandJoystick(
            Constants.LEFT_CONTROLLER_PORT
        )
        self.rightController = commands2.button.CommandJoystick(
            Constants.RIGHT_CONTROLLER_PORT
        )
        self.codriverController = commands2.button.CommandXboxController(
            Constants.CODRIVER_CONTROLLER_PORT
        )
        self.driveSubsystem = CANDriveSubsystem()
        self.rollerSubsystem = CANRollerSubsystem()
        self.fuzzyBallIntakeSubsystem = FuzzyBallIntakeSubsystem()
        self.automaticPneumatics = AutomaticPneumatics ()
        self.automaticPneumatics.set_solenoid_0(True)
        self.automaticPneumatics.set_solenoid_1(False)

        # self.sd.putNumber('camera_server', CameraServer.is_alive())

        self.configureButtonBindings()

    def configureButtonBindings(self):
        self.driveSubsystem.setDefaultCommand(
            DriveCommand(
                lambda: -self.leftController.getRawAxis(1),
                lambda: -self.rightController.getRawAxis(1),
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
        self.leftTrigger = self.leftController.button(1)
        self.leftTrigger.whileTrue(
            RollerCommand(
            lambda: Constants.ROLLEY_THINGEY_EJECT_SPEED, 
            lambda: 0, 
            self.rollerSubsystem
            )
        ).whileFalse(
            RollerCommand(
                lambda: 0,
                lambda: 0,
                self.rollerSubsystem,
            )
        )
        self.rightThree = self.rightController.button(3)
        self.rightFour = self.rightController.button(4)
        self.fuzzyBallIntakeSubsystem.setDefaultCommand(
            FuzzyBallIntakeCommand(
                lambda: 0.5 if self.rightThree.getAsBoolean() else 0,
                lambda: 0.5 if self.rightFour.getAsBoolean() else 0,
                lambda: AnalogInput(0).getValue(),
                self.sd,
                self.fuzzyBallIntakeSubsystem,
            )
        )
        self.rightTrigger = self.rightController.button(1)
        self.automaticPneumatics.setDefaultCommand(
            AutomaticPneumaticsCommand(
                lambda: self.rightTrigger,
                lambda: AnalogInput(0).getValue(),
                self.automaticPneumatics
            )
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return AutoCommand(self.driveSubsystem, self.rollerSubsystem)