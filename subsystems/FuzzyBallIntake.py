import commands2
import rev

import Constants


class FuzzyBallIntakeSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.rollerMotor = rev.SparkMax(
            Constants.ROLLEYARM_MOTOR_ID, rev.SparkBase.MotorType.kBrushless
        )

        self.rollerMotor.setCANTimeout(250)
 
        self.sparkConfig = rev.SparkMaxConfig()

        self.sparkConfig.voltageCompensation(Constants.ROLLEYARM_MOTOR_VCOMP)
        self.sparkConfig.smartCurrentLimit(
            Constants.ROLLEYARM_MOTOR_CURRENT_LIMIT
        )
        self.rollerMotor.configure(
            self.sparkConfig,
            rev.SparkBase.ResetMode.kResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters,
        )

    def runRoller(self, forward: float, reverse: float) -> None:
        self.rollerMotor.set(forward - reverse)