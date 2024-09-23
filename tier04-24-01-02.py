import cadquery as cq
import math

main_body = (
    cq.Workplane("XY")
    .box(118, 54, 42)
    .edges("|X and >Y")
    .fillet(6)
)

cutout = cq.Workplane("XY").box(99, 16, 38).translate((0, 0, 20))

large_hole = (
    cq.Workplane("XY")
    .circle(55 / 2)
    .extrude(54)
    .translate((-27.5 - 55 / 2, 0, 27))
)

small_hole = (
    cq.Workplane("XY")
    .circle(30 / 2)
    .extrude(54)
    .translate((-27.5 + 55 / 2, 0, 27))
)

chamfer_cut = (
    cq.Workplane("XY")
    .box(22, 16, 42)  # Increased depth to cut through the side wall
    .translate((51, 0, 0))  # Adjusted Z to align with the bottom face
    .rotateAboutCenter((0, 0, 1), 60)
)

# Create fillets on the front face
for i in [-1, 1]:
    main_body = (
        main_body.faces(">X")
        .workplane()
        .moveTo(59, i * 27)
        .circle(6)
        .extrude(-6)
    )

final_part = (
    main_body.cut(cutout)
    .cut(large_hole)
    .cut(small_hole)
    .cut(chamfer_cut)
)

show_object(final_part)