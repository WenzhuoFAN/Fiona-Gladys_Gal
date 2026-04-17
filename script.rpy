label start:

    show xinyi normal at stand_left
    "这是故事的开始。"

    x "今天也要一起去练习吗？"

    show sinuo normal at stand_right
    s "当然。"

    menu:
        "去":
            jump go_out
        "不去":
            jump stay_home

label go_out:

    x "那就出发吧。"
    s "嗯，走吧。"
    "你们一起去了练习室。"
    hide xinyi
    hide sinuo
    return

label stay_home:

    hide sinuo
    x "那今天就先在这里休息一下吧。"
    "你留在了教室里。"
    hide xinyi
    return
