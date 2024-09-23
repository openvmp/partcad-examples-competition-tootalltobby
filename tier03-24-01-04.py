import math
import cadquery as cq

# Create Cylinder 1
cylinder1 = cq.Workplane("XY").cylinder(32, 20)

# Create Cylinder 2
cylinder2 = cq.Workplane("XY").cylinder(32, 20).translate((98, 0, 0))

# Create Rectangular Block
rect_block = cq.Workplane("XY").box(98, 16, 32).translate((49, 0, 16))

# Union Operation
main_body = cylinder1.union(cylinder2).union(rect_block)

# Create Cylinder 3
cylinder3 = cq.Workplane("XY").cylinder(32, 7)

# Create Cylinder 4
cylinder4 = cq.Workplane("XY").cylinder(32, 7).translate((98, 0, 0))

# Create Rectangular Block 2
rect_block2 = cq.Workplane("XY").box(98, 14, 32).translate((49, 0, 16))

# Difference Operation for U-Shape Cutout
cutout = cylinder3.union(cylinder4).union(rect_block2)
main_body = main_body.cut(cutout)

# Create Cylinder 5
cylinder5 = cq.Workplane("XY").cylinder(32, 4)

# Create Cylinder 6
cylinder6 = cq.Workplane("XY").cylinder(32, 4).translate((98, 0, 0))

# Difference Operation for Holes
holes = cylinder5.union(cylinder6)
final_part = main_body.cut(holes)

show_object(final_part)