# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2
import wpilib
import wpilib.drive
import rev

import Constants


class CANDriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        # spark max motor controllers in brushed mode
        self.leftLeader = rev.SparkMax(
            Constants.LEFT_LEADER_ID, rev.SparkBase.MotorType.kBrushed
        )
        self.leftFollower = rev.SparkMax(
            Constants.LEFT_FOLLOWER_ID, rev.SparkBase.MotorType.kBrushed
        )
        self.rightLeader = rev.SparkMax(
            Constants.RIGHT_LEADER_ID, rev.SparkBase.MotorType.kBrushed
        )
        self.rightFollower = rev.SparkMax(
            Constants.RIGHT_FOLLOWER_ID, rev.SparkBase.MotorType.kBrushed
        )

        # this is the differential drive instance which allows us to control
        # the drive with joysticks
        self.drive = wpilib.drive.DifferentialDrive(
            self.leftLeader, self.rightLeader
        )

        # set can timeouts. This program only sets parameters on startup and
        # doesn't get any parameters so a long timeout is acceptable. Programs
        # which set or get parameters during runtime likely want a timeout
        # closer or equal to the default.
        self.leftLeader.setCANTimeout(250)
        self.rightLeader.setCANTimeout(250)
        self.leftFollower.setCANTimeout(250)
        self.rightFollower.setCANTimeout(250)

        self.sparkConfig = rev.SparkMaxConfig()

        # enable voltage compensation. This makes the performance more consistent
        # at different levels of battery charge at the cost of some peak performance
        # with a fully charged battery
        self.sparkConfig.voltageCompensation(12.0)

        # set current limit. This helps prevent tripping breakers
        self.sparkConfig.smartCurrentLimit(Constants.DRIVE_MOTOR_CURRENT_LIMIT)

        # set to follow leader and then use to configure corresponding follower
        self.sparkConfig.follow(self.leftLeader)
        self.leftFollower.configure(
            self.sparkConfig,
            rev.SparkBase.ResetMode.kResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters,
        )
        self.sparkConfig.follow(self.rightLeader)
        self.rightFollower.configure(
            self.sparkConfig,
            rev.SparkBase.ResetMode.kResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters,
        )

        # disable following and use to configure leader. Invert before configuring
        # left side so that postive values drive both sides forward
        self.sparkConfig.disableFollowerMode()
        self.rightLeader.configure(
            self.sparkConfig,
            rev.SparkBase.ResetMode.kResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters,
        )
        self.sparkConfig.inverted(True)
        self.leftLeader.configure(
            self.sparkConfig,
            rev.SparkBase.ResetMode.kResetSafeParameters,
            rev.SparkBase.PersistMode.kPersistParameters,
        )

    # function to drive with joystick inputs
    def arcadeDrive(self, xSpeed: float, zRotation: float) -> None:
        self.drive.arcadeDrive(xSpeed, zRotation)
