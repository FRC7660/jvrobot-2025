import commands2
import Constants

from networktables import NetworkTables
from subsystems.FuzzyBallIntake import FuzzyBallIntakeSubsystem


class FuzzyBallIntakeCommand(commands2.Command):
    def __init__(
        self,
        forward: lambda forward: forward,
        reverse: lambda reverse: reverse,
        limit_switch: lambda limit_switch: limit_switch,
        fuzzyBallIntakeSubsystem: FuzzyBallIntakeSubsystem,
    ) -> None:
        self.fuzzyBallIntakeSubsystem = fuzzyBallIntakeSubsystem
        self.forward = forward
        self.reverse = reverse
        self.limit_switch = limit_switch
        self.addRequirements(fuzzyBallIntakeSubsystem)
        NetworkTables.initialize(server='10.76.60.2')
        self.sd = NetworkTables.getTable('SmartDashboard')
        super().__init__()

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        if self.limit_switch() > Constants.HALF_WIT_SWITCH:
            self.fuzzyBallIntakeSubsystem.runRoller(self.forward(), 0.0)
        else:
            self.fuzzyBallIntakeSubsystem.runRoller(self.forward(), self.reverse())

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False