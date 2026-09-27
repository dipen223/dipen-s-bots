import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length=1
width =1
height=1
x=0
y=0
z=0
# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length,width,height])

for i in range(5):
    for j in range(5):
        length, width, height = 1, 1, 1
        k = height /2 
        for i in range(10):
            pyrosim.Send_Cube(name=f'Box{i}_{j}_{i}',pos=[i,j,k],size=[length,width,height])
            z += height / 2 + (height * 0.9) / 2
            length *= 0.9
            width *= 0.9
            height *= 0.9

   



pyrosim.End()