from openbrush import OpenBrush
import numpy as np

      
op = OpenBrush()

op.new()

x = np.linspace(-5* np.pi ,5 * np.pi, 500)
y = np.sin(x)


op.brushSizeSet(0.1)
op.colorSetRGB([0.1, 0.2, 0.5])
op.brushType("light")
op.plot(x, y)


x = np.linspace(-5* np.pi ,5 * np.pi, 500)
y = np.sin(x) + 1
z = np.cos(x)

op.colorSetRGB([0.7, 0.2, 0.1])
op.plot(x, y, z)

x = np.linspace(-5* np.pi ,5 * np.pi, 500)
y = np.sin(x) - 1 
z = np.cos(x)

op.colorSetRGB([0.6, 0, 0.6])
op.plot(z, y, x)

op.userMoveTo([0,3,10])


# op.viewOnlyToggle()