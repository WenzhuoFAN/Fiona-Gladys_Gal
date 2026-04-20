# CG registrations.
#
# Folder rule:
#   images/cg/<arc>/<event_name>.<ext>
#   images/cg/routes/<route>/<event_name>.<ext>
#
# Image name rule:
#   image cg <arc>_<event_name> = "<path>"
#   image cg route_<route>_<event_name> = "<path>"
#
# Arc guide:
#   prologue
#   chapter1
#   endings
#   routes/xinyi
#   routes/sinuo
#
# Recommended formats:
#   webp/jpg for full-screen CG
#   png/webp when transparency is needed
#
# Examples:
# image cg prologue_rooftop_promise = "images/cg/prologue/rooftop_promise.webp"
# image cg chapter1_first_reunion = "images/cg/chapter1/first_reunion.webp"
# image cg route_xinyi_backstage_confession = "images/cg/routes/xinyi/backstage_confession.webp"
#
# Script usage:
#   scene cg prologue_rooftop_promise with dissolve
#   scene cg chapter1_first_reunion with fade
