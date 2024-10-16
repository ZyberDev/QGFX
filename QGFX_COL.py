def _unpack_color(r,g,b):
  if type(r)==Color:return r.unpack()
  if type(r) in [list,tuple]:r,g,b=r
  elif g==None:g,b=r,r
  return r,g,b

def _color(r,g,b):
  if type(r)==Color:return r.to_tuple()
  if type(r) in [list,tuple]:r,g,b=r
  elif g==None:g,b=r,r
  return round(r),round(g),round(b)

class Color:
  def __init__(self,r,g=None,b=None):
    r,g,b=_unpack_color(r,g,b)
    self.r=float(r)
    self.g=float(g)
    self.b=float(b)
  
  def from_8bit(r,g=None,b=None):
    r,g,b=_color(r,g,b)
    return Color(r/255,g/255,b/255)
  
  def __add__(self,other):
    other=Color(other)
    return Color(self.r+other.r,self.g+other.g,self.b+other.b)
  
  def __sub__(self,other):
    other=Color(other)
    return Color(self.r-other.r,self.g-other.g,self.b-other.b)
  
  def mul(self,other):
    other=Color(other)
    return Color(self.r*other.r,self.g*other.g,self.b*other.b)
  
  def div(self,other):
    other=Color(other)
    return Color(self.r/other.r,self.g/other.g,self.b/other.b)
  
  def lerp(self,other,t):
    other=Color(other)
    return self+(other-self).mul(t)
  
  def __repr__(self):
    return "Color"+str(self.to_tuple())
  
  def unpack(self):
    return self.r,self.g,self.b
  
  def to_tuple(self):
    return round(self.r*255),round(self.g*255),round(self.b*255)