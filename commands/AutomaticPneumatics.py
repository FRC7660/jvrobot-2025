import commands2

class Pneumatics(commands2.CommandBase):
    def __init__(self, pneumatics_subsystem):
        super().__init__()
        self.pneumatics_subsystem = pneumatics_subsystem
        self.addRequirements([self.pneumatics_subsystem])
    def execute(self):
        self.pneumatics_subsystem.set_solenoid(not self.pneumatics_subsystem.solenoid.get())