import cadquery as cq
import paramak 
import os 
import numpy as np

# geometry
# class ExtrudeCircleShape(distance, radius, extrusion_start_offset=0.0, rotation_angle=360, extrude_both=True, color=(0.984, 0.603, 0.6), name='extrudecircleshape', **kwargs)
for i in range(1,100):
    radius = 5
    length = i # np.random.randint(1,100)
    my_shape = paramak.ExtrudeCircleShape(points=[(50,0)], radius=radius, distance=length)
    my_shape.export_stp('geometry/stp_files/'+str(i)+'.stp')
    my_shape.export_2d_image('geometry/png_files/'+str(i)+'.png')
    my_shape.export_html_3d('geometry/html_files/'+str(i)+'.html')

