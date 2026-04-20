# FionaGladysGal

## Current Layout / 当前结构

Current recommended project layout:

当前推荐的项目目录结构：

```text
FionaGladysGal/
+-- README.md
+-- options.rpy
+-- gui.rpy
+-- screens.rpy
+-- core/
|   +-- characters.rpy
|   +-- images.rpy
|   +-- bg_images.rpy
|   +-- cg_images.rpy
|   +-- transforms.rpy
|   +-- variables.rpy
|   +-- audio.rpy
|   `-- common_events.rpy
+-- story/
|   +-- start.rpy
|   +-- prologue/
|   |   +-- 00_intro.rpy
|   |   +-- 01_practice_days.rpy
|   |   `-- 02_regret_night.rpy
|   +-- chapter1/
|   |   +-- 00_reunion.rpy
|   |   +-- 01_old_stage.rpy
|   |   `-- 02_group_reconnect.rpy
|   +-- routes/
|   |   +-- common_route.rpy
|   |   +-- xinyi_route.rpy
|   |   `-- sinuo_route.rpy
|   `-- endings/
|       `-- true_end.rpy
+-- images/
|   +-- bg/
|   |   +-- school/
|   |   +-- city/
|   |   +-- stage/
|   |   +-- interior/
|   |   `-- special/
|   +-- cg/
|   |   +-- prologue/
|   |   +-- chapter1/
|   |   +-- routes/
|   |   |   +-- xinyi/
|   |   |   `-- sinuo/
|   |   `-- endings/
|   +-- ui/
|   `-- characters/
`-- audio/
    +-- bgm/
    +-- se/
    `-- voice/
```

## Layer Rules / 层级规则

English:

- `options.rpy`, `gui.rpy`, `screens.rpy`: only system and UI settings.
- `core/`: only reusable definitions such as characters, images, transforms, variables, and audio aliases.
- `core/images.rpy`: only standing character art and expression aliases.
- `core/bg_images.rpy`: only reusable background registrations and background naming templates.
- `core/cg_images.rpy`: only CG registrations and route/chapter CG naming templates.
- `story/start.rpy`: only the project entry label and top-level flow handoff.
- `story/prologue/` and `story/chapter1/`: only chapter content, scene logic, and jumps.
- `story/routes/` and `story/endings/`: only branching flow and endings.

中文：

- `options.rpy`、`gui.rpy`、`screens.rpy`：只负责系统配置、界面样式和通用 UI。
- `core/`：只放可复用的底层定义，比如角色、立绘声明、通用变换、变量和音频别名。
- `core/images.rpy`：只放人物立绘和表情差分声明。
- `core/bg_images.rpy`：只放背景图声明和背景命名模板。
- `core/cg_images.rpy`：只放 CG 声明和章节/路线 CG 命名模板。
- `story/start.rpy`：只作为主入口，负责把流程交给序章或主线起点。
- `story/prologue/` 和 `story/chapter1/`：只写章节剧情、场景演出和跳转逻辑。
- `story/routes/` 和 `story/endings/`：只处理分线推进和结局收束。

## Naming Rules / 命名规则

English:

- Labels: `pro_00_intro`, `ch1_01_old_stage`, `route_xinyi`, `ending_true`
- Variables: `aff_xinyi`, `aff_sinuo`, `flag_prologue_cleared`
- Images: `image xinyi normal`, `image sinuo normal`
- Backgrounds: `image bg school_gate_day`, `image bg city_street_night_rain`
- CGs: `image cg prologue_rooftop_promise`, `image cg route_xinyi_backstage_confession`
- Audio aliases: `audio.bgm_prologue`, `audio.se_stage_door`

中文：

- 标签：`pro_00_intro`、`ch1_01_old_stage`、`route_xinyi`、`ending_true`
- 变量：`aff_xinyi`、`aff_sinuo`、`flag_prologue_cleared`
- 图片：`image xinyi normal`、`image sinuo normal`
- 背景图：`image bg school_gate_day`、`image bg city_street_night_rain`
- CG：`image cg prologue_rooftop_promise`、`image cg route_xinyi_backstage_confession`
- 音频别名：`audio.bgm_prologue`、`audio.se_stage_door`

## Background And CG Rules / 背景图与 CG 规范

English:

- Background folders are grouped by reusable space, not by chapter.
- CG folders are grouped by chapter or route, because CG is usually tied to a one-off event.
- Background path rule: `images/bg/<category>/<location>_<time>[_weather][_mood].<ext>`
- Background image rule: `image bg <category>_<location>_<time>[_weather][_mood] = "<path>"`
- CG path rule: `images/cg/<arc>/<event_name>.<ext>` or `images/cg/routes/<route>/<event_name>.<ext>`
- CG image rule: `image cg <arc>_<event_name> = "<path>"`
- Use `scene bg ...` for location/time changes.
- Use `scene cg ...` for full-screen event illustrations.
- Recommended formats:
  - backgrounds: `jpg` or `webp`
  - CG: `webp` or `jpg`
  - standing art with transparency: `png` or `webp`

中文：

- 背景图目录按“可复用地点”分，不按章节分。
- CG 目录按“章节/路线事件”分，因为 CG 通常是一次性关键画面。
- 背景图路径规则：`images/bg/<category>/<location>_<time>[_weather][_mood].<ext>`
- 背景图声明规则：`image bg <category>_<location>_<time>[_weather][_mood] = "<path>"`
- CG 路径规则：`images/cg/<arc>/<event_name>.<ext>` 或 `images/cg/routes/<route>/<event_name>.<ext>`
- CG 声明规则：`image cg <arc>_<event_name> = "<path>"`
- 地点或时间变化时，用 `scene bg ...`
- 关键事件全屏插图时，用 `scene cg ...`
- 推荐格式：
  - 背景图：`jpg` 或 `webp`
  - CG：`webp` 或 `jpg`
  - 带透明的立绘/特效：`png` 或 `webp`

## Suggested Background Taxonomy / 建议的背景分类

English:

- `images/bg/school/`: gate, classroom, hallway, rooftop, practice room
- `images/bg/city/`: street, station, riverside, plaza
- `images/bg/stage/`: backstage, stage, rehearsal hall, auditorium
- `images/bg/interior/`: cafe, apartment, office, lounge
- `images/bg/special/`: memory, dream, filtered variants, stylized plates

中文：

- `images/bg/school/`：校门、教室、走廊、天台、练习室
- `images/bg/city/`：街道、车站、江边、广场
- `images/bg/stage/`：后台、舞台、排练厅、观众席
- `images/bg/interior/`：咖啡店、公寓、办公室、休息室
- `images/bg/special/`：回忆、梦境、滤镜版背景、特殊演出底图

## Script Examples / 剧本示例

```renpy
scene bg school_gate_day with fade
show xinyi normal at left
show sinuo normal at right

x "今天也要一起练习吗？"

scene bg stage_backstage_dim with dissolve
s "我们已经走到这里了。"

scene cg chapter1_first_reunion with fade
```

## Collaboration Notes / 协作说明

English:

- New character definitions go into `core/characters.rpy`.
- New standing art and expression declarations go into `core/images.rpy`.
- New reusable background declarations go into `core/bg_images.rpy`.
- New chapter/route CG declarations go into `core/cg_images.rpy`.
- Shared transforms and animation helpers go into `core/transforms.rpy`.
- Common flags and route variables go into `core/variables.rpy`.
- Plot writing should continue from `story/prologue/` and `story/chapter1/`.
- Shared repeated scenes should be extracted into `core/common_events.rpy`.

中文：

- 新角色定义写入 `core/characters.rpy`。
- 新立绘和表情差分声明写入 `core/images.rpy`。
- 新背景图声明写入 `core/bg_images.rpy`。
- 新章节/路线 CG 声明写入 `core/cg_images.rpy`。
- 通用站位、演出变换和动画辅助写入 `core/transforms.rpy`。
- 公共旗标、好感变量和路线变量写入 `core/variables.rpy`。
- 剧情正文继续在 `story/prologue/` 和 `story/chapter1/` 中推进。
- 多章节重复使用的公共片段应抽到 `core/common_events.rpy`。

## Suggested Next Steps / 建议的下一步

English:

1. Fill in the real prologue beats in `story/prologue/`.
2. Replace placeholder narration in `story/chapter1/` with the reunion draft.
3. Add reusable backgrounds under `images/bg/` and register them in `core/bg_images.rpy`.
4. Add event CG under `images/cg/` and register them in `core/cg_images.rpy`.
5. Add BGM and SFX aliases in `core/audio.rpy`.
6. Decide where the common route ends and where `route_xinyi` / `route_sinuo` begin.

中文：

1. 把 `story/prologue/` 里的占位内容替换成正式序章剧情。
2. 把 `story/chapter1/` 里的占位旁白替换成重逢章节草案。
3. 把可复用背景图放进 `images/bg/`，并在 `core/bg_images.rpy` 里统一注册。
4. 把事件 CG 放进 `images/cg/`，并在 `core/cg_images.rpy` 里统一注册。
5. 在 `core/audio.rpy` 里补全 BGM 和音效别名。
6. 明确共通线结束点，以及 `route_xinyi` / `route_sinuo` 的分流位置。
