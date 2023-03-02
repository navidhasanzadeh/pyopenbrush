from openbrush import OpenBrush
import numpy as np
import time

      
ob = OpenBrush()

ob.new()
ob.viewOnlyToggle()
x = np.linspace(-2* np.pi ,2 * np.pi, 100)
step = 10
bias = 3
c = [0,1,0,0, 2,0,0, -3,0]
x_c = [bias+step, bias+step, bias+step,bias + 2 * step,bias + 2 * step,bias + 2 * step,bias + 3*step,bias + 3 *step,bias + 3* step]
x_c = x_c[::-1]

axis = [np.min(x_c)-2, np.max(x_c)+2]
axis_w = [0] * 2

y1 = np.sin(x)
y2 = 2 * np.sin(2 * x)
y3 = -3 * np.sin(4 * x)
y = y1 + 1 * y2 + 1* y3


# ob.brushSizeSet(0.1)
# ob.colorSetRGB([0.1, 0.2, 0.5])
ob.brushType("light")

ob.plot(x, y1, bias + step * 3, "red")
ob.plot(x, y2, bias + step * 2, "yellow")
ob.plot(x, y3, bias + step, "green")
ob.plot(x, y, bias , "white")

ob.plot(x=+12, y= np.array(c[0:3]), z=np.array(x_c[0:3])-3, c="red")
ob.plot(x=12, y=np.array(c[3:6]), z=np.array(x_c[3:6])-3, c="yellow")
ob.plot(x=+12, y=np.array(c[6:9]), z=np.array(x_c[6:9])-3, c="green")
ob.plot(x=-1* np.array(axis_w)+12, y=0, z=np.array(axis)-3 , c="cyan")

xx = -1* np.array(axis_w)+12
yy = 0
zz = np.array(axis)-3

ob.brushSizeSet(0.9)
ob.colorSetRGB("blue")
ob.drawPath([[np.min(x),np.min(y) ,bias], [np.min(x),np.max(y) ,bias], [np.max(x),np.max(y) ,bias], [np.max(x),np.min(y),bias],[np.min(x),np.min(y) ,bias],])
ob.colorSetRGB("cyan")
ob.drawPath([[np.min(xx),-6,np.min(zz)], [np.min(xx),-6, np.max(zz)], [np.max(xx),6,np.max(zz)], [np.max(xx),6, np.min(zz)],[np.min(xx),-6, np.min(zz)],])

# ob.drawPath([[np.min(x),np.min(y) ,bias + step], [np.min(x),np.max(y) ,bias + step], [np.max(x),np.max(y) ,bias + step], [np.max(x),np.min(y),bias + step],[np.min(x),np.min(y) ,bias + step],])

ob.userMoveTo([-18, -4, 3])

# ob.brushMoveTo([0,2, 10])
# ob.drawText("sin(x)")
# ob.plot(x, y1, 3 + 4, "red")
# ob.plot(x, y1, 3 + 4, "red")
# ob.plot(x, y1, 3 + 4, "red")
# ob.plot(x, y1, 3 + 4, "red")

# i = 0
# j = 0
# a = 1
# while True:
#     ob.strokeDelete(0)
#     ob.strokeDelete(0)
#     ob.strokeDelete(0)
#     ob.strokeDelete(0)
    
#     if i!=0:
#         ob.plot(x, y1, 3 + 4 * i * 0.1, "red")
#         ob.plot(x, y2, 3 + 8 * i * 0.1, "yellow")
#         ob.plot(x, y3, 3 + 12 * i * 0.1, "blue")
#     if i==0:
#         ob.plot(x, y, 3 + 0 * i * 0.1, "white")
#         time.sleep(2)
#     i = i + a
#     if abs(i)==20 or i == 0:
#         a *= -1
#     time.sleep(0.1)

# # x = np.linspace(-5* np.pi ,5 * np.pi, 500)
# y = np.sin(x) + 1
# z = np.cos(x)

# op.colorSetRGB([0.7, 0.2, 0.1])
# op.plot(x, y, z)

# x = np.linspace(-5* np.pi ,5 * np.pi, 500)
# y = np.sin(x) - 1 
# z = np.cos(x)

# op.colorSetRGB([0.6, 0, 0.6])
# op.plot(z, y, x)

# op.userMoveTo([0,3,10])


# op.viewOnlyToggle()