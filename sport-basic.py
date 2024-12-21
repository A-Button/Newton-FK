import math

class F():
    def __init__(self,value,angle):
        self.value = value
        self.angle = angle
        self.Value = (value,angle)
    def cut(self,cita=0):
        return (self.value * math.cos(math.radians(self.angle-cita)),0),(self.value * math.sin(math.radians(self.angle-cita)),90)
    def plus(self,F2):
        FRx=self.cut()[0][0]+F2.cut()[0][0]
        FRy=self.cut()[1][0]+F2.cut()[1][0]
        FRvalue=math.sqrt(FRx**2+FRy**2)
        FRangle=math.degrees(math.atan(FRy/FRx))
        if FRx*FRy<0:
            return F(FRvalue,-FRangle)
        else:
            return F(FRvalue, FRangle)
    def minus(self,F2):
        FRx=self.cut()[0][0]-F2.cut()[0][0]
        FRy=self.cut()[1][0]-F2.cut()[1][0]
        FRvalue=math.sqrt(FRx**2+FRy**2)
        FRangle=math.degrees(math.atan(FRy/FRx))
        if FRx*FRy<0:
            return F(FRvalue,-FRangle)
        else:
            return F(FRvalue, FRangle)
    def multiply(self,F2):
        FRvalue=self.value*F2.value
        FRangle=self.angle+F2.angle
        return F(FRvalue,FRangle)
    def divide(self,F2):
        FRvalue=self.value/F2.value
        FRangle=self.angle-F2.angle
        return F(FRvalue,FRangle)
    def __str__(self):
        return str(self.Value)

class v():
    def __init__(self,value,angle):
        self.value = value
        self.angle = angle
        self.Value = (value,angle)
    def plus(self,v2):
        VRx=self.value * math.cos(math.radians(self.angle))+v2.value * math.cos(math.radians(v2.angle))
        VRy=self.value * math.sin(math.radians(self.angle))+v2.value * math.sin(math.radians(v2.angle))
        VRvalue=math.sqrt(VRx**2+VRy**2)
        VRangle=math.degrees(math.atan(VRy/VRx))
        if VRx*VRy<0:
            return v(VRvalue,-VRangle)
        else:
            return v(VRvalue, VRangle)
    def minus(self,v2):
        VRx=self.value * math.cos(math.radians(self.angle))-v2.value * math.cos(math.radians(v2.angle))
        VRy=self.value * math.sin(math.radians(self.angle))-v2.value * math.sin(math.radians(v2.angle))
        VRvalue=math.sqrt(VRx**2+VRy**2)
        VRangle=math.degrees(math.atan(VRy/VRx))
        if VRx*VRy<0:
            return v(VRvalue,-VRangle)
        else:
            return v(VRvalue, VRangle)
    def multiply(self,v2):
        VRvalue=self.value*v2.value
        VRangle=self.angle+v2.angle
        return v(VRvalue,VRangle)
    def divide(self,v2):
        VRvalue=self.value/v2.value
        VRangle=self.angle-v2.angle
        return v(VRvalue,VRangle)
    def __str__(self):
        return str(self.Value)

class a():
    def __init__(self,value,angle):
        self.value = value
        self.angle = angle
        self.Value = (value,angle)
    def plus(self,a2):
        ARx=self.value * math.cos(math.radians(self.angle))+a2.value * math.cos(math.radians(a2.angle))
        ARy=self.value * math.sin(math.radians(self.angle))+a2.value * math.sin(math.radians(a2.angle))
        ARvalue=math.sqrt(ARx**2+ARy**2)
        ARangle=math.degrees(math.atan(ARy/ARx))
        if ARx*ARy<0:
            return a(ARvalue,-ARangle)
        else:
            return a(ARvalue, ARangle)
    def minus(self,a2):
        ARx=self.value * math.cos(math.radians(self.angle))-a2.value * math.cos(math.radians(a2.angle))
        ARy=self.value * math.sin(math.radians(self.angle))-a2.value * math.sin(math.radians(a2.angle))
        ARvalue=math.sqrt(ARx**2+ARy**2)
        ARangle=math.degrees(math.atan(ARy/ARx))
        if ARx*ARy<0:
            return a(ARvalue,-ARangle)
        else:
            return a(ARvalue, ARangle)
    def multiply(self,a2):
        ARvalue=self.value*a2.value
        ARangle=self.angle+a2.angle
        return a(ARvalue,ARangle)
    def divide(self,a2):
        ARvalue=self.value/a2.value
        ARangle=self.angle-a2.angle
        return a(ARvalue,ARangle)
    def __str__(self):
        return str(self.Value)

class x():
    def __init__(self,value,angle):
        self.value = value
        self.angle = angle
        self.Value = (value,angle)
    def plus(self,x2):
        XRx=self.value * math.cos(math.radians(self.angle))+x2.value * math.cos(math.radians(x2.angle))
        XRy=self.value * math.sin(math.radians(self.angle))+x2.value * math.sin(math.radians(x2.angle))
        SRvalue=math.sqrt(XRx**2+XRy**2)
        SRangle=math.degrees(math.atan(XRy/XRx))
        if XRx*XRy<0:
            return x(SRvalue,-SRangle)
        else:
            return x(SRvalue, SRangle)
    def minus(self,x2):
        XRx=self.value * math.cos(math.radians(self.angle))-x2.value * math.cos(math.radians(x2.angle))
        XRy=self.value * math.sin(math.radians(self.angle))-x2.value * math.sin(math.radians(x2.angle))
        SRvalue=math.sqrt(XRx**2+XRy**2)
        SRangle=math.degrees(math.atan(XRy/XRx))
        if XRx*XRy<0:
            return x(SRvalue,-SRangle)
        else:
            return x(SRvalue, SRangle)
    def multiply(self,x2):
        SRvalue=self.value*x2.value
        SRangle=self.angle+x2.angle
        return x(SRvalue,SRangle)
    def divide(self,x2):
        SRvalue=self.value/x2.value
        SRangle=self.angle-x2.angle
        return x(SRvalue,SRangle)
    def __str__(self):
        return str(self.Value)

# Example
F1=F(3,90)
F2=F(4,0)
print(F1.plus(F2))
print(F1.minus(F2))