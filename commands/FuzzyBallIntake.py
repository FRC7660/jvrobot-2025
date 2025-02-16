import commands2
import Constants

from subsystems.FuzzyBallIntake import FuzzyBallIntakeSubsystem


class FuzzyBallIntakeCommand(commands2.Command):
    def __init__(
        self,
        forward: lambda forward: forward,
        reverse: lambda reverse: reverse,
        limit_switch: lambda limit_switch: limit_switch,
        smart_dashboard,
        fuzzyBallIntakeSubsystem: FuzzyBallIntakeSubsystem,
    ) -> None:
        self.fuzzyBallIntakeSubsystem = fuzzyBallIntakeSubsystem
        self.forward = forward
        self.reverse = reverse
        self.limit_switch = limit_switch
        self.smart_dashboard = smart_dashboard
        self.addRequirements(fuzzyBallIntakeSubsystem)
        super().__init__()

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        self.smart_dashboard.putNumber('limit_switch', self.limit_switch())
        self.smart_dashboard.putNumber('intake_forward', self.forward())
        self.smart_dashboard.putNumber('intake_reverse', self.reverse())
        
        if self.limit_switch() > Constants.HALF_WIT_SWITCH:
            self.fuzzyBallIntakeSubsystem.runRoller(self.forward(), 0.0)
        else:
            self.fuzzyBallIntakeSubsystem.runRoller(self.forward(), self.reverse())

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False