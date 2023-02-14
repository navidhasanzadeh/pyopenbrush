from openbrush import OpenBrush
      
op = OpenBrush()

op.new()

op.setMode("monoscopic")

op.colorSetRGB([0.1, 0.8, 0.1])

op.brushSizeSet(0.9)

op.drawText("Navid Hasanzadeh")

op.drawPaths([[[0,0,0],[1,0,0],[1,1,0]],[[0,0,-1],[-1,0,-1],[-1,1,-1]]
              , [[0,0,-1],[-0,0,-1],[-1,2,-2]]])

op.colorSetRGB([0.1, 0., 0.1])

op.userMoveTo([0,0,0])

op.drawPath([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])

op.brushType("light")
