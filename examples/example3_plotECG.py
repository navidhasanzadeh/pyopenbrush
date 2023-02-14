from openbrush import OpenBrush
import numpy as np
from scipy.misc import electrocardiogram
import time

      
op = OpenBrush()

op.new()

ecg = electrocardiogram()

ecg = ecg[0:800:5] * 10

x = np.linspace(-0.5* len(ecg) ,0.5 * len(ecg), len(ecg))


op.brushSizeSet(0.5)
op.colorSetRGB([0.9, 0.1, 0.1])
op.plot(x, ecg)
op.userMoveTo([x[0],0,20])

time.sleep(2)

for t in range(len(ecg)):
    op.userMoveTo([x[t],0,20])
    time.sleep(0.1)
