import math
import cadquery as cq

main_cylinder = cq.Workplane("XY").cylinder(55, 25)

inner_hollow_cylinder = cq.Workplane("XY").cylinder(42, 21)
main_cylinder = main_cylinder.cut(inner_hollow_cylinder)

top_elliptical_cap = (
    cq.Workplane("XY")
    .ellipse(10, 4)
    .workplane(offset=4)
    .ellipse(10, 4)
    .loft(combine=True)
    .translate((0, 0, 55))
)
main_cylinder = main_cylinder.union(top_elliptical_cap)

handle = (
    cq.Workplane("YZ")
    .ellipse(20, 8)
    .workplane(offset=6)
    .ellipse(20, 8)
    .loft(combine=True)
    .translate((25, 0, 37))
)
main_cylinder = main_cylinder.union(handle)

hole_in_handle = cq.Workplane("YZ").cylinder(5, 12).translate((25, 0, 37))
main_cylinder = main_cylinder.cut(hole_in_handle)

# Removed the draft_angle section as it was causing errors and seems unnecessary
# draft_angle = (
#     cq.Workplane("XY")
#     .cylinder(42, 21)
#     .workplane(offset=42)
#     .cylinder(42, 21)
#     .loft(combine=True)
# )
# main_cylinder = main_cylinder.cut(draft_angle)

show_object(main_cylinder)