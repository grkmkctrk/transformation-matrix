## transformation-matrix

There are two algorithms forward and backward kinematic.

>>Forward kinematics find the location of end of the robot arm in global coordinate plane.
In this algorithm givens are length of the robot arms and degree of between robot arms.

>>Backward kinematics find the degree of between the robot arms for reach the target point.       
In this algorithm givens are length of the robot arms and location of end of the robot arm.
This project is calculate the transformation matrix that you need when you use these algorithms.  





a = Dler(
                ["x", "x", "z", "x", "y"],                                              
                [0, 90, 90, -60, 20],                                                   
                [[50, 10, 10], [0, 0, -10], [-50, 20, 10], [0, -10, 40], [10, -40, -5]] 
            )
sirasiyla eksenlerde (will rotate which around the axis in order )
bu kadar derece donsun (how much should rotate)
her donme sonrasi yapmasi gerek hareket (movement origin to origin)

b = a.Td()                                
b = a.Dt()                                
b = a.spePoints([10, 20, 30], adj = 0)     
                                           
donusum matrisleri (transformation matrices that progam used)
bu matrislerin toplam carpimi (mutiplication of the matrices starting the rigth side)
1 : global noktanin lokaldaki yeri (write 1 to find global location in local plane)
0 : lokaldeki noktanin globaldaki yeri (write 0 to find local location in global plane)





