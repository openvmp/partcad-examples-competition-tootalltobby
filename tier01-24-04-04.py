import cadquery as cq
import math

main_cuboid = cq.Workplane("XY").box(10.0, 0.75, 1.0, centered=(True, True, True))

cylindrical_ends = (
    cq.Workplane("XY")
    .moveTo(-5.0, 0)
    .circle(0.75)
    .extrude(0.75)
    .union(
        cq.Workplane("XY")
        .moveTo(5.0, 0)
        .circle(0.75)
        .extrude(0.75)
    )
)

combined_shape = main_cuboid.union(cylindrical_ends)

# Reduce the fillet radius to ensure it can be applied successfully
combined_shape = combined_shape.edges("|Z").fillet(0.3)

central_arch = (
    cq.Workplane("XZ")
    .center(0, 0.5)
    .circle(18.0)
    .extrude(0.75)
)

final_shape = combined_shape.cut(central_arch)

final_shape = final_shape.edges("<Z").fillet(0.1875)

show_object(final_shape)