import math
import cadquery as cq

# Step 1: Create the Main Body
main_body = cq.Workplane("XY").box(10.0, 1.0, 1.0)

# Step 2: Create the Arch Cutout
arch_cutout = cq.Workplane("XY").cylinder(1.0, 18.0).translate((0, 0, 0.5))
main_body = main_body.cut(arch_cutout)

# Step 3: Create the Side Cutouts
side_cutout1 = cq.Workplane("XY").box(2.5, 1.0, 1.0).translate((-3.75, 0, 0.5))
side_cutout2 = cq.Workplane("XY").box(2.5, 1.0, 1.0).translate((3.75, 0, 0.5))
main_body = main_body.cut(side_cutout1).cut(side_cutout2)

# Step 4: Create the Rounded Ends
rounded_end1 = cq.Workplane("XY").cylinder(1.0, 0.75).translate((-5.0, 0, 0.5))
rounded_end2 = cq.Workplane("XY").cylinder(1.0, 0.75).translate((5.0, 0, 0.5))
main_body = main_body.union(rounded_end1).union(rounded_end2)

# Step 5: Apply Fillets with a reduced radius
main_body = main_body.edges().fillet(0.1)

show_object(main_body)