#QUICK GRAPHICS LIBRARY
from QGFX_COL import Color,_color
import sys

_ESC=chr(27)

def _grcmd(t,*args,l=None):
  l=() if l==None else tuple(l)
  l=args+l+tuple([t])
  sys.stdout.write(_ESC+"["+";".join(map(str,l))+"G")

def _deg(x):
  return round(x*10)

def _points(p):
  if type(p[0]) in [tuple,list]:
    return map(round,[p[i//2][i%2] for i in range(len(p)*2)])
  else:
    return map(round,p)

def flush():
  print(end="")

def cls():
  sys.stdout.write(_ESC+"[2J")

def clear():
  cls()
  set_color(255,255,255)
  fill_rect(0,220,320,20)

def set_color(r,g=None,b=None):
  r,g,b=_color(r,g,b)
  _grcmd(0,r,g,b)

def set_pen(size,style):
  _grcmd(1,style,size)

def set_pixel(x,y,r,g=None,b=None):
  r,g,b=_color(r,g,b)
  _grcmd(2,round(x),round(y),r,g,b)

def draw_arc(x,y,w,h,start,extent):
  _grcmd(3,round(x),round(y),round(w),round(h),_deg(start),_deg(extent))

def draw_line(x0,y0,x1,y1):
  _grcmd(4,round(x0),round(y0),round(x1),round(y1))

def draw_poly_line(p):
  _grcmd(5,l=_points(p))

def draw_rect(x,y,w,h):
  _grcmd(6,round(x),round(y),round(w),round(h))

def fill_arc(x,y,w,h,start,extent):
  _grcmd(7,round(x),round(y),round(w),round(h),_deg(start),_deg(extent))

def fill_polygon(p):
  _grcmd(8,l=_points(p))

def fill_rect(x,y,w,h):
  _grcmd(9,round(x),round(y),round(w),round(h))

def draw_string(x,y,s):
  _grcmd(10,round(x),round(y))
  sys.stdout.write(s)
  _grcmd(11)

def draw_image(img,x,y):
  _grcmd(12,round(x),round(y))
  sys.stdout.write(img)
  _grcmd(13)

def push_image(x,y,w,h):
  _grcmd(14,round(x),round(y),round(w),round(h))

def pop_image():
  _grcmd(15)

def get_pixel(x,y):
  _grcmd(16,round(x),round(y))
  return list(map(int,sys.stdin.readline().split(",")))

def cursor(mode):
  _grcmd(17,mode)

def draw_circle(x,y,r):
  draw_arc(x-r,y-r,r*2,r*2,0,360)

def fill_circle(x,y,r):
  fill_arc(x-r,y-r,r*2,r*2,0,360)
