#!/usr/bin/env python3
"""
    This is a demo program showing how to use Mecanum control with the
    MecanumDrive class.

    Since the team has decided to build a wedge, this code is going to
    have to be modified to use only three motors.

    The theory for such a design can be found at 
                    https://www.mdpi.com/2073-8994/11/10/1268 

"""

import wpilib
import rev
from wpilib.drive import KilloughDrive


class MyRobot(wpilib.TimedRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    leftChannel = 1
    rightChannel = 2
    rearChannel = 3

    # Channels on the roboRIO that run the shooter
    rightShooterChannel = 4
    leftShooterChannel = 5

    # Channels on the roboRIO to be used for the intake
    intakeChannel = 6

    # Channels on the roboRIO to be used for the lift
    liftChannel = 7

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        """Robot initialization function"""
        self.leftMotor  = rev.CANSparkMax(self.leftChannel,  rev.CANSparkMax.MotorType.kBrushless)
        self.rightMotor = rev.CANSparkMax(self.rightChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.rearMotor  = rev.CANSparkMax(self.rearChannel,  rev.CANSparkMax.MotorType.kBrushless)

        self.rightShooterMotor = rev.CANSparkMax(self.rightShooterChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.leftShooterMotor =  rev.CANSparkMax(self.leftShooterChannel, rev.CANSparkMax.MotorType.kBrushless)

        # invert the left side motors
        self.leftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rightMotor.setInverted(True)
        self.rearMotor.setInverted(True)

        self.drive = KilloughDrive(
            self.leftMotor,
            self.rightMotor,
            self.rearMotor,
        )

        self.drive.setExpiration(0.1)

        self.stick = wpilib.Joystick(self.joystickChannel)

    def teleopInit(self):
        self.drive.setSafetyEnabled(True)

    def teleopPeriodic(self):

        """Place code here that does things as a result of operator
        actions"""

        try:
            if self.stick.getTrigger():
                print("Trigger Pressed")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(1):
                print("Button 1 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(2):
                print("Button 2 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(3):
                print("Button 3 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(4):
                print("Button 4 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(5):
                print("Button 5 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(6):
                print("Button 6 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(7):
                print("Button 7 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(8):
                print("Button 8 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(9):
                print("Button 9 Pressed.")
        except:
            if not self.isFmsAttached():
                raise
        try:
            if self.stick.getRawButton(10):
                print("Button 10 Pressed.")
        except:
            if not self.isFmsAttached():
                raise

        """Runs the motors with Killough drive."""
        # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
        # This sample does not use field-oriented drive, so the gyro input is set to zero.
        try:
            self.drive.driveCartesian(
                self.stick.getX(), self.stick.getY(), self.stick.getZ(), 0
            )
        except:
            if not self.isFmsAttached():
                raise


if __name__ == "__main__":
    wpilib.run(MyRobot)
