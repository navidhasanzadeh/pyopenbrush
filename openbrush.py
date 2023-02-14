import requests
import os
import platform

class OpenBrush:
    def __init__(self, ip="localhost:40074", mode = "monoscopic",
                 ob_host_ip="192.168.165.48"):
        self.ip = ip
        self.setMode(mode, ob_host_ip)
        
    def __list_to_str__(self, li):
        li = list(li)
        l_str = f'{{{", ".join(map(str, li))}}}'.replace("{","")\
            .replace("}","").replace(" ", "").replace("(", "[")\
                .replace(")", "]")
        return l_str

    def sendcom(self, values: dict):
      r = requests.get("http://{}/api/v1".format(self.ip), params=values)
      return r
  
    def setMode(self, mode: str, ob_host_ip="192.168.165.48"):
        if platform.system()=='Linux':
            if mode.lower() == "monoscopic":
                os.system("unset OB_HOST")
            if mode.lower() == "headset":
                os.system("export OB_HOST={}".format(ob_host_ip))
        
    def new(self):
        self.sendcom({"new":""})
        
    def drawText(self, text: str):
        self.sendcom({"draw.text":text})
        
    def drawPaths(self, points: list):
        points_str = self.__list_to_str__(points)
        self.sendcom({"draw.paths": points_str})

    def drawPath(self, points: list):
        points_str = self.__list_to_str__(points)
        self.sendcom({"draw.path": points_str})
    
    def colorSetRGB(self, values: list):   
        values_str = self.__list_to_str__(values)
        self.sendcom({"color.set.rgb": values_str})
    
    def brushType(self, brush_type: str):
        self.sendcom({"brush.type": brush_type})

    def brushSizeSet(self, brush_size: float):
        self.sendcom({"brush.size.set": brush_size})
    
    def userMoveTo(self, point: list):
        values_str = self.__list_to_str__(point)
        self.sendcom({"user.move.to": values_str})

    def userMoveBy(self, point: list):
        values_str = self.__list_to_str__(point)
        self.sendcom({"user.move.by": values_str})

    # def plot(self, x=None, y=None, z=None):
    #     if x is None:            
    #         x = list(range(len(y)))
    #     if z is None:
    #         z = [0] * len(y)
    #     zipped = zip(x, y, z)
    #     zipped_list = list(zipped)
    #     xyz = self.__list_to_str__([zipped_list])
    #     self.drawPaths([xyz])
    # def viewOnlyToggle(self):
    #     self.sendcom({"viewonly.toggle": ""})
        
                    