from aqa.math import *
from varmain.primitiv import *
from varmain.custom import *
import math as m

@activate(Group="Gasket", 
          FirstPortEndtypes = "Undefined_ET", 
          TooltipShort="Gasket w/ Bolt", 
          TooltipLong="Gasket with Bolt",  
          LengthUnit="in", 
          Ports="2")

@group("MainDimensions")
@param(D1=LENGTH, TooltipShort="Gasket Outside Diameter", TooltipLong="Gasket Outside Diameter")
@param(D2=LENGTH, TooltipShort="Nominal Outside Diameter", TooltipLong="Nominal Outside Diameter")
@param(T=LENGTH, TooltipShort="Thickness of Gasket", TooltipLong="Thickness of Gasket")
@param(B=INT, TooltipShort="Number of Bolts", TooltipLong="Number of Bolts")
@param(BD=LENGTH, TooltipShort="Bolt Diameter", TooltipLong="Bolt Diameter")
@param(BL=LENGTH, TooltipShort="Bolt Length", TooltipLong="Bolt Length")
@param(BCD=LENGTH, TooltipShort="Bolt Circle Diameter", TooltipLong="Bolt Circle Diameter")


def GASKET_W_BOLT(s, D1=2, D2=1.315, T=0.0625, B=4, BD=0.5, BL=2.5, BCD=3.125984, **kw):
    
    #Bolt Split Angle
    start_angle = 0
    split_angle = 360/B

    GASKET = CYLINDER(s, R=D1/2, H=T, O=D2/2).rotateY(-90)

    for i in range(0, B):
       
        x = (BCD/2)*m.cos(m.radians(start_angle))
        y = (BCD/2)*m.sin(m.radians(start_angle))
        z = -(BL/2)+T
        BOLT = CYLINDER(s, R=BD/2, H=BL, O=0).translate((x, y, z)).rotateY(-90)
        
        start_angle = start_angle + split_angle
        
        GASKET.uniteWith(BOLT)
        BOLT.erase()
    
    s.setPoint((0, 0, 0), (1, 0, 0))
    s.setPoint((-T, 0, 0), (-1, 0, 0))


