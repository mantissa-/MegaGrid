import bpy
import random
from random import randint

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.edge_split()

for i in range(6):
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_random(percent=20, seed=randint(0, 9999), action='SELECT')
    bpy.ops.mesh.select_random(percent=20, seed=randint(0, 9999), action='SELECT')
    bpy.ops.mesh.subdivide(smoothness=0)
    #bpy.ops.mesh.poke()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_split()

bpy.ops.object.editmode_toggle()