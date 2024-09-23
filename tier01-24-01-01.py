import cadquery as cq
import math

cuboid1 = cq.Workplane("XY").box(65, 30, 15)
cuboid2 = cq.Workplane("XY").box(30, 30, 62).translate((15, 0, 38.5))
cylinder = cq.Workplane("XY").cylinder(15, 14.5).rotate((0, 0, 0), (0, 1, 0), 90).translate((65, 15, 7.5))

combined_cuboids = cuboid1.union(cuboid2)
filleted_end = combined_cuboids.edges("|Z and >X").fillet(14.5)

show_object(filleted_end)