import math

class Vector():
    def __init__(self,value,angle,unit='N'):
        self.value = value
        self.angle = angle
        self.Value = (value,angle)
        self.unit = unit
    def cut(self,cita=0):
        return (self.value * math.cos(math.radians(self.angle-cita)),0),(self.value * math.sin(math.radians(self.angle-cita)),90)
    def plus(self,F2):
        FRx=self.cut()[0][0]+F2.cut()[0][0]
        FRy=self.cut()[1][0]+F2.cut()[1][0]
        FRvalue=math.sqrt(FRx**2+FRy**2)
        FRangle=math.degrees(math.atan(FRy/FRx))
        if FRx*FRy<0:
            return Vector(FRvalue,-FRangle)
        else:
            return Vector(FRvalue, FRangle)
    def minus(self,F2):
        FRx=self.cut()[0][0]-F2.cut()[0][0]
        FRy=self.cut()[1][0]-F2.cut()[1][0]
        FRvalue=math.sqrt(FRx**2+FRy**2)
        FRangle=math.degrees(math.atan(FRy/FRx))
        if FRx*FRy<0:
            return Vector(FRvalue,-FRangle)
        else:
            return Vector(FRvalue, FRangle)
    def multiply(self,F2):
        FRvalue=self.value*F2.value
        FRangle=self.angle+F2.angle
        return Vector(FRvalue,FRangle)
    def divide(self,F2):
        FRvalue=self.value/F2.value
        FRangle=self.angle-F2.angle
        return Vector(FRvalue,FRangle)
    def __str__(self):
        return str(self.Value)

class Scalar():
    def __init__(self,value,unit='m'):
        self.value = value
        self.unit = unit
    def plus(self,v2):
        VR=self.value + v2.value
        return Scalar(VR)
    def minus(self,v2):
        VR=self.value - v2.value
        return Scalar(VR)
    def multiply(self,v2):
        VR=self.value * v2.value
        return Scalar(VR)
    def divide(self,v2):
        VR=self.value / v2.value
        return Scalar(VR)
    def __str__(self):
        return str(self.value)

class object():
    """
    A class to represent a physical object with mass, position, velocity, and acceleration.

    Attributes
    ----------
    mass : float
        The mass of the object.
    position : list
        The position of the object in a 2D space [x, y].
    velocity : Scalar
        The velocity of the object.
    acceleration : Scalar
        The acceleration of the object.

    Methods
    -------
    __str__():
        Returns a string representation of the object.
    xmove(time):
        Updates the x-coordinate of the object's position based on time.
    ymove(time):
        Updates the y-coordinate of the object's position based on time.
    move(time):
        Updates the position and velocity of the object based on time.
    run(time, precision=0.01):
        Simulates the object's movement over a given time with a specified precision.
    fake(time):
        Returns the estimated position of the object after a given time without updating the actual position.
    addforce(force):
        Adds a force to the object and updates its acceleration.
    addvelocity(velocity):
        Adds a velocity to the object and updates its velocity.
    addacceleration(acceleration):
        Adds an acceleration to the object and updates its acceleration.
    setposition(position):
        Sets the position of the object.
    """
    def __init__(self,mass,position,velocity,acceleration):
        self.mass = mass
        self.position = list(position)
        self.velocity = velocity
        self.acceleration = acceleration
    def __str__(self):
        return 'Mass: '+str(self.mass)+'\nPosition: '+str(self.position)+'\nVelocity: '+str(self.velocity)+'\nAcceleration: '+str(self.acceleration)
    def xmove(self,time):
        self.position[0] = self.position[0].plus(Scalar(0.5*self.acceleration.cut()[0].value*time**2+self.velocity.cut()[0].value*time))
        return self.position
    def ymove(self,time):
        self.position[1] = self.position[1].plus(Scalar(0.5*self.acceleration.cut()[1].value*time**2+self.velocity.cut()[1].value*time))
        return self.position
    def move(self,time):
        self.xmove(time)
        self.ymove(time)
        self.velocity = self.velocity.plus(self.acceleration.multiply(Scalar(time)))
        return self.position
    def run(self,time,precision=0.01):
        t = 0
        while t<time:
            self.move(precision)
            t += precision
        return self.position
    def fake(self,time):
        return (self.position[0].plus(self.velocity.cut()[0].multiply(Scalar(time))),self.position[1].plus(self.velocity.cut()[1].multiply(Scalar(time))))
    def addforce(self,force):
        self.acceleration = self.acceleration.plus(force.divide(Scalar(self.mass)))
        return self.acceleration
    def addvelocity(self,velocity):
        self.velocity = self.velocity.plus(velocity)
        return self.velocity
    def addacceleration(self,acceleration):
        self.acceleration = self.acceleration.plus(acceleration)
        return self.acceleration
    def setposition(self,position):
        self.position = list(position)
        return self.position

# Features to be added:
# class sense():
#     def __init__(self,groundtype='empty'):
#         self.groundtype = groundtype