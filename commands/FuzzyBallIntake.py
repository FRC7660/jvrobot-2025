import commands2

from subsystems.FuzzyBallIntake import FuzzyBallIntakeSubsystem


class FuzzyBallIntakeCommand(commands2.Command):
    def __init__(
        self,
        forward: lambda forward: forward,
        reverse: lambda reverse: reverse,
        fuzzyBallIntakeSubsystem: FuzzyBallIntakeSubsystem,
    ) -> None:
        self.fuzzyBallIntakeSubsystem = fuzzyBallIntakeSubsystem
        self.forward = forward
        self.reverse = reverse
        self.addRequirements(fuzzyBallIntakeSubsystem)
        super().__init__()

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        self.fuzzyBallIntakeSubsystem.runRoller(self.forward(), self.reverse())

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False