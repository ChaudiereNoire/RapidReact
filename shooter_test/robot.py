#!/usr/bin/env python3
"""
    This is a demo program showing how to run a couple of motors for a
    simple shooter.

    The last mod was just made to show how to introduce logging.  I only
    noticed the aged comments when I double checked the file on gihub.
"""

import logging
import rev
import time
import wpilib


class MyRobot(wpilib.TimedRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    leftChannel = 4
    rightChannel = 5

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    # Default shooter motor speed is 0
    shooterSpeed = 0

    def robotInit(self):
        """Robot initialization function"""
        self.leftMotor = rev.CANSparkMax(self.leftChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.rightMotor = rev.CANSparkMax(self.rightChannel, rev.CANSparkMax.MotorType.kBrushless)
        
        self.leftEncoder = self.leftMotor.getEncoder()
        self.rightEncoder = self.rightMotor.getEncoder()

        # invert the left side motors
        self.rightMotor.setInverted(True)

        # The shooter does not actually use a drive mechanism


        #self.drive = DifferentialDrive(
        #    self.leftMotor,
        #    self.rightMotor
        #)

        # self.drive.setExpiration(0.1)

        self.stick = wpilib.Joystick(self.joystickChannel)

    def teleopInit(self):
        self.leftMotor.set(self.shooterSpeed)
        self.rightMotor.set(self.shooterSpeed)

    def teleopPeriodic(self):

        # If the joystick button is pressed, run both motors at full speed
        try:
            if self.stick.getRawButton(1):
                self.shooterSpeed = self.stick.getRawAxis(3)
                stuff = "SHOOTER Time: {} Shooter Speed: {} Left Encoder: {} Right Encoder: {}".format(time.time(),
                         self.shooterSpeed, self.leftEncoder.getPosition(), self.rightEncoder.getPosition())
                self.logger.info(stuff)
            else:
                self.shooterSpeed = 0
        except:
            if not wpilib.DriverStation.isFMSAttached():
                raise

        self.leftMotor.set(self.shooterSpeed)
        self.rightMotor.set(self.shooterSpeed)

if __name__ == "__main__":
    wpilib.run(MyRobot)
