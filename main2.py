import numpy as np
import math


class Dler:
    def __init__(self, eksen, derece, mesafe):
        self.eksen  = eksen  
        self.derece = derece 
        self.mesafe = mesafe 
        #self.nokta  = nokta  
        #self.adj    = adj
        
    def Td(self):
        T = np.array([])        
        for i in range(len(self.derece)):
            self.derece[i] = np.where(self.derece[i] < 0, 360+self.derece[i], self.derece[i])    
            if self.eksen[i] == "y":
                T = np.append(T, np.array(
                        [[math.cos(math.radians(self.derece[i])), 0, math.sin(math.radians(self.derece[i])), self.mesafe[i][0]],
                        [0, 1, 0, self.mesafe[i][1]],
                        [-math.sin(math.radians(self.derece[i])), 0, math.cos(math.radians(self.derece[i])), self.mesafe[i][2]],
                        [0, 0, 0, 1]]
                    ))
            if self.eksen[i] == "z":
                T = np.append(T, np.array(
                        [[math.cos(math.radians(self.derece[i])), -math.sin(math.radians(self.derece[i])), 0, self.mesafe[i][0]],
                        [math.sin(math.radians(self.derece[i])), math.cos(math.radians(self.derece[i])), 0, self.mesafe[i][1]],
                        [0, 0, 1, self.mesafe[i][2]],
                        [0, 0, 0, 1]]
                    ))
            if self.eksen[i] == "x":
                T = np.append(T, np.array(
                        [[1, 0, 0, self.mesafe[i][0]],
                        [0, math.cos(math.radians(self.derece[i])), -math.sin(math.radians(self.derece[i])), self.mesafe[i][1]],
                        [0, math.sin(math.radians(self.derece[i])), math.cos(math.radians(self.derece[i])), self.mesafe[i][2]],
                        [0, 0, 0, 1]]
                    ))

        T = T.reshape([len(self.derece), 4, 4])
        for n in range(len(self.derece)):
            for m in range(4):
                for k in range(4):
                    if T[n,m,k] == math.cos(math.radians(90)):
                        T[n,m,k] = 0

        T = np.where((T < 0) & (T > -0.001) , 0, T)                 
                        
        return T, len(self.derece)


    def Dt(self):
        
        
        Tbitti = np.matmul( # bu saga dogru tersten
            self.Td()[0][self.Td()[1] - 2], # [0][2]
            self.Td()[0][self.Td()[1] - 1]  # [0][3]
            )
        
        if self.Td()[1] > 2:  
            for i in range(self.Td()[1] - 3, -1, -1):
                Tbitti = np.matmul(  # bu saga dogru tersten
                    self.Td()[0][i],
                    Tbitti
                    )
            return Tbitti
    
    def spePoints(self, nokta, **adj):
        nokta = np.array(np.append(nokta, 1))
        nokta = nokta.reshape(4, 1)
        #print(adj["adj"])
        if adj['adj'] == 0:
            return np.matmul(self.Dt(), nokta)
        elif adj['adj'] == 1:
            return np.matmul(np.linalg.inv(self.Dt()), nokta)


a = Dler(
                ["x", "x", "z", "x", "y"],              # sirasiyla eksenlerde (will rotate which around the axis in order )
                [0, 90, 90, -60, 20],                   # bu kadar derece donsun (how much should rotate)
                [[50, 10, 10], [0, 0, -10], [-50, 20, 10], [0, -10, 40], [10, -40, -5]] # her donme sonrasi yapmasi gerek hareket (movement origin to origin)
            )

#b = a.Td() # donusum matrisleri
#b = a.Dt()  # bu matrislerin toplam carpimi
b = a.spePoints([10, 20, 30], adj = 0) # 1 : global noktanin lokaldaki yeri
                                       # 2 : lokaldeki noktanin globaldaki yeri             
print(b)
