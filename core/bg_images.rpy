# Background image registrations.
#
# Folder rule:
#   images/bg/<category>/<location>_<time>[_weather][_mood].<ext>
#
# Image name rule:
#   image bg <category>_<location>_<time>[_weather][_mood] = "<path>"
#
# Category guide:
#   school   - campus-era spaces and student-life locations.
#   city     - reunion-era outdoor public spaces.
#   stage    - rehearsal rooms, backstage, stage, and performance spaces.
#   interior - cafes, apartments, offices, lounges, and other indoor rooms.
#   special  - memory, dream, filtered, or one-off event backgrounds.
#
# Recommended formats:
#   jpg/webp for standard backgrounds
#   png/webp for backgrounds that need transparency or layered effects
#
# Examples:
# image bg school_gate_day = "images/bg/school/gate_day.jpg"
# image bg school_practice_room_evening = "images/bg/school/practice_room_evening.jpg"
# image bg city_street_night_rain = "images/bg/city/street_night_rain.jpg"
# image bg stage_backstage_dim = "images/bg/stage/backstage_dim.jpg"
#
# Script usage:
#   scene bg school_gate_day with fade
#   scene bg city_street_night_rain with dissolve

image bg school_hallway_day = "images/bg/school/hallway_day.png"
