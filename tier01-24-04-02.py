import math
import cadquery as cq

# Create Cylinder 1 (Main Body)
cylinder1 = cq.Workplane("XY").cylinder(0.875 * 25.4, 1.25 * 25.4 / 2)

# Create Cylinder 2 (Top Fillet)
cylinder2 = cq.Workplane("XY").cylinder(0.125 * 25.4, 1.5 * 25.4 / 2).translate((0, 0, 0.750 * 25.4))

# Union Cylinder 1 and Cylinder 2
combined_cylinders = cylinder1.union(cylinder2)

# Create Cone 1 (Bottom Taper) using a tapered extrusion
cone1 = (
    cq.Workplane("XY")
    .circle(1.25 * 25.4 / 2)
    .workplane(offset=-3.5 * 25.4)
    .circle(0.375 * 25.4 / 2)
    .loft()
)

# Union the Resulting Solid with Cone 1
combined_with_cone = combined_cylinders.union(cone1)

# Create Cylinder 3 (Hole)
cylinder3 = cq.Workplane("XY").cylinder(3.5 * 25.4, 0.5 * 25.4 / 2).rotate((0, 0, 0), (1, 0, 0), 90)

# Difference with Cylinder 3 (Hole)
final_part = combined_with_cone.cut(cylinder3)

show_object(final_part)