import commands2
import Constants
import wpilib
from subsystems.AutomaticPneumatics import AutomaticPneumatics

class AutomaticPneumaticsCommand(commands2.Command):
    def __init__(
        self,
        button: lambda button: button,
        limit_switch: lambda limit_switch: limit_switch,
        pneumatics_subsystem: AutomaticPneumatics,
    ) -> None:
        self.button = button
        self.extend = False 
        self.button_previous = False 
        self.limit_switch = limit_switch
        self.timer = wpilib.Timer()
        self.pneumatics_subsystem = pneumatics_subsystem
        self.addRequirements(self.pneumatics_subsystem)
        super().__init__()

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        if self.button_previous == False and self.button().getAsBoolean() == True:
            self.pneumatics_subsystem.set_solenoid_0(self.extend)
            self.pneumatics_subsystem.set_solenoid_1(not self.extend)
            self.extend = not self.extend
            self.timer.reset()
        if self.extend == True and self.limit_switch() > Constants.HALF_WIT_SWITCH and self.timer() > 4.0:
            self.pneumatics_subsystem.set_solenoid_0(True)
            self.pneumatics_subsystem.set_solenoid_1(False)
            self.extend = False
        self.button_previous = self.button().getAsBoolean()

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False