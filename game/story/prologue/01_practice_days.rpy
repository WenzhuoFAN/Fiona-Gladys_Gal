label pro_01_practice_days:

    x "今天也要一起去练习吗？"
    s "当然。"

    menu:
        "陪心宜多练一会儿":
            $ aff_xinyi += 1
            "你们一起去了练习室。"

        "让思诺先回去休息":
            $ aff_sinuo += 1
            "你留在了教室里，天色慢慢暗了下来。"

    jump pro_02_regret_night
