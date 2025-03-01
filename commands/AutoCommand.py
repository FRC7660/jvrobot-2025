import Constants
import commands2
import wpilib
from subsystems.CANDriveSubsystem import CANDriveSubsystem
from subsystems.CANRollerSubsystem import CANRollerSubsystem


class AutoCommand(commands2.Command):
    def __init__(
        self,
        driveSubsystem: CANDriveSubsystem,
        rollerSubsystem: CANRollerSubsystem,
        autoChooser,
    ) -> None:
        self.driveSubsystem = driveSubsystem
        self.rollerSubsystem = rollerSubsystem
        self.autoChooser = autoChooser
        self.timer = wpilib.Timer()
        self.seconds = 7.9
        self.addRequirements(self.driveSubsystem)
        self.addRequirements(self.rollerSubsystem)
        super().__init__()

    def initialize(self) -> None:
        self.timer.restart()

    def routine1(self):
        if self.timer.get() < 1.6:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 2.8:
            self.driveSubsystem.arcadeDrive(0.0, -0.5)
        elif self.timer.get() < 3.7:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 4.9:
            self.driveSubsystem.arcadeDrive(0.0, -0.5)
        elif self.timer.get() < 5.7:
         self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 6.1:
            self.driveSubsystem.arcadeDrive(0.0, 0.0)
            self.rollerSubsystem.runRoller(Constants.ROLLEY_THINGEY_EJECT_SPEED, 0.0)
        elif self.timer.get() < 10.0:
            self.end(False)
    
    def routine2(self):
        if self.timer.get() < 1.6:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 2.8:
            self.driveSubsystem.arcadeDrive(0.0, 0.5)
        elif self.timer.get() < 3.7:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 4.9:
            self.driveSubsystem.arcadeDrive(0.0, 0.5)
        elif self.timer.get() < 5.7:
         self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 6.1:
            self.driveSubsystem.arcadeDrive(0.0, 0.0)
            self.rollerSubsystem.runRoller(Constants.ROLLEY_THINGEY_EJECT_SPEED, 0.0)
        elif self.timer.get() < 10.0:
            self.end(False)

    def routine3(self):
        if self.timer.get() < 2:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 2.7:
            self.end(False) 

    def routine4(self):
        if self.timer.get() < 3.5:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 6.3:
            self.driveSubsystem.arcadeDrive(0.0, 0.0)
            self.rollerSubsystem.runRoller(Constants.ROLLEY_THINGEY_EJECT_SPEED, 0.0)
        elif self.timer.get() < 8.0:
            self.end(False)
    
    def routine5(self):
        if self.timer.get() < 6.7:
            self.driveSubsystem.arcadeDrive(0.5, 0.0)
        elif self.timer.get() < 6.9:
            self.driveSubsystem.arcadeDrive(0.0, 0.0)
            self.rollerSubsystem.runRoller(Constants.ROLLEY_THINGEY_EJECT_SPEED, 0.0)
        elif self.timer.get() < 7.9:
            self.end(False)

    def execute(self) -> None:
        routine = self.autoChooser.getSelected()
        if routine == 1:
            self.routine1()
        elif routine == 2:
            self.routine2()
        elif routine == 3:
            self.routine3()
        elif routine == 4:
            self.routine4()
        elif routine == 5:
            self.routine5()
    def isFinished(self) -> bool:
        return self.timer.get() >= self.seconds

    def end(self, interrupted: bool) -> None:
        self.driveSubsystem.arcadeDrive(0.0, 0.0)
        self.rollerSubsystem.runRoller(0.0, 0.0)