import Constants
import commands2
import wpilib
from subsystems.CANDriveSubsystem import CANDriveSubsystem
from subsystems.CANRollerSubsystem import CANRollerSubsystem


class AutoCommand(commands2.Command):
    def __init__(self, driveSubsystem: CANDriveSubsystem, rollerSubsystem: CANRollerSubsystem) -> None:
        self.driveSubsystem = driveSubsystem
        self.rollerSubsystem = rollerSubsystem
        self.timer = wpilib.Timer()
        self.seconds = 1.7
        self.addRequirements(self.driveSubsystem)
        self.addRequirements(self.rollerSubsystem)
        super().__init__()

    def initialize(self) -> None:
        self.timer.restart()
        
    
    def execute(self) -> None:
        if self.timer.get() < 0.3:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 0.6:
            self.driveSubsystem.arcadeDrive(0.0, 0.5)
        elif self.timer.get() < 0.9:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 1.2:
            self.driveSubsystem.arcadeDrive(0.0, 0.0)
            self.rollerSubsystem.runRoller(Constants.ROLLEY_THINGEY_EJECT_SPEED, 0.0)

    def isFinished(self) -> bool:
        return self.timer.get() >= self.seconds

    def end(self, interrupted: bool) -> None:
        self.driveSubsystem.arcadeDrive(0.0, 0.0)
        self.rollerSubsystem.runRoller(0.0, 0.0)

