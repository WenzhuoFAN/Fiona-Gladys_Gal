# FionaGladysGal

## Current Layout / 当前结构

Current recommended project layout:

Ren'Py runtime files live under `game/`.

当前推荐的项目目录结构：

Ren'Py 的运行文件都放在 `game/` 下。

```text
FionaGladysGal/
+-- README.md
+-- game/
|   +-- options.rpy
|   +-- gui.rpy
|   +-- screens.rpy
|   +-- SourceHanSansLite.ttf
|   +-- core/
|   |   +-- characters.rpy
|   |   +-- images.rpy
|   |   +-- bg_images.rpy
|   |   +-- cg_images.rpy
|   |   +-- transforms.rpy
|   |   +-- variables.rpy
|   |   +-- audio.rpy
|   |   `-- common_events.rpy
|   +-- story/
|   |   +-- start.rpy
|   |   +-- prologue/
|   |   |   +-- 00_intro.rpy
|   |   |   +-- 01_practice_days.rpy
|   |   |   `-- 02_regret_night.rpy
|   |   +-- chapter1/
|   |   |   +-- cha1_00_reunion.rpy
|   |   |   +-- cha1_01_old_stage.rpy
|   |   |   `-- cha1_02_group_reconnect.rpy
|   |   +-- routes/
|   |   |   +-- common_route.rpy
|   |   |   +-- xinyi_route.rpy
|   |   |   `-- sinuo_route.rpy
|   |   `-- endings/
|   |       `-- true_end.rpy
|   +-- images/
|   |   +-- bg/
|   |   |   +-- school/
|   |   |   +-- city/
|   |   |   +-- stage/
|   |   |   +-- interior/
|   |   |   `-- special/
|   |   +-- cg/
|   |   |   +-- prologue/
|   |   |   +-- chapter1/
|   |   |   +-- routes/
|   |   |   |   +-- xinyi/
|   |   |   |   `-- sinuo/
|   |   |   `-- endings/
|   |   +-- ui/
|   |   `-- characters/
|   +-- audio/
|   |   +-- bgm/
|   |   +-- se/
|   |   `-- voice/
|   +-- libs/
|   `-- tl/
`-- System.Drawing.Drawing2D.GraphicsPath
```

## Layer Rules / 层级规则

English:

- `game/options.rpy`, `game/gui.rpy`, `game/screens.rpy`: only system and UI settings.
- `game/core/`: only reusable definitions such as characters, images, transforms, variables, and audio aliases.
- `game/core/images.rpy`: only standing character art and expression aliases.
- `game/core/bg_images.rpy`: only reusable background registrations and background naming templates.
- `game/core/cg_images.rpy`: only CG registrations and route/chapter CG naming templates.
- `game/story/start.rpy`: only the project entry label and top-level flow handoff.
- `game/story/prologue/` and `game/story/chapter1/`: only chapter content, scene logic, and jumps.
- `game/story/routes/` and `game/story/endings/`: only branching flow and endings.

中文：

- `game/options.rpy`、`game/gui.rpy`、`game/screens.rpy`：只负责系统配置、界面样式和通用 UI。
- `game/core/`：只放可复用的底层定义，比如角色、立绘声明、通用变换、变量和音频别名。
- `game/core/images.rpy`：只放人物立绘和表情差分声明。
- `game/core/bg_images.rpy`：只放背景图声明和背景命名模板。
- `game/core/cg_images.rpy`：只放 CG 声明和章节/路线 CG 命名模板。
- `game/story/start.rpy`：只作为主入口，负责把流程交给序章或主线起点。
- `game/story/prologue/` 和 `game/story/chapter1/`：只写章节剧情、场景演出和跳转逻辑。
- `game/story/routes/` 和 `game/story/endings/`：只处理分线推进和结局收束。

## Naming Rules / 命名规则

English:

- Labels: `pro_00_intro`, `cha1_00_reunion`, `route_xinyi`, `ending_true`
- Variables: `aff_xinyi`, `aff_sinuo`, `flag_prologue_cleared`
- Images: `image xinyi normal`, `image sinuo normal`
- Backgrounds: `image bg school_gate_day`, `image bg city_street_night_rain`
- CGs: `image cg prologue_rooftop_promise`, `image cg route_xinyi_backstage_confession`
- Chapter file prefix: `cha1_00_...`, `cha1_01_...`, `cha1_02_...`
- Audio aliases: `audio.bgm_prologue`, `audio.se_stage_door`

中文：

- 标签：`pro_00_intro`、`cha1_00_reunion`、`route_xinyi`、`ending_true`
- 变量：`aff_xinyi`、`aff_sinuo`、`flag_prologue_cleared`
- 图片：`image xinyi normal`、`image sinuo normal`
- 背景图：`image bg school_gate_day`、`image bg city_street_night_rain`
- CG：`image cg prologue_rooftop_promise`、`image cg route_xinyi_backstage_confession`
- 章节文件前缀：`cha1_00_...`、`cha1_01_...`、`cha1_02_...`
- 音频别名：`audio.bgm_prologue`、`audio.se_stage_door`

## Background And CG Rules / 背景图与 CG 规范

English:

- Background folders are grouped by reusable space, not by chapter.
- CG folders are grouped by chapter or route, because CG is usually tied to a one-off event.
- Background path rule: `game/images/bg/<category>/<location>_<time>[_weather][_mood].<ext>`
- Background image rule: `image bg <category>_<location>_<time>[_weather][_mood] = "images/bg/<category>/<location>_<time>[_weather][_mood].<ext>"`
- CG path rule: `game/images/cg/<arc>/<event_name>.<ext>` or `game/images/cg/routes/<route>/<event_name>.<ext>`
- CG image rule: `image cg <arc>_<event_name> = "images/cg/<arc>/<event_name>.<ext>"`
- Use `scene bg ...` for location/time changes.
- Use `scene cg ...` for full-screen event illustrations.
- Recommended formats:
  - backgrounds: `jpg` or `webp`
  - CG: `webp` or `jpg`
  - standing art with transparency: `png` or `webp`

中文：

- 背景图目录按“可复用地点”分，不按章节分。
- CG 目录按“章节/路线事件”分，因为 CG 通常是一次性关键画面。
- 背景图路径规则：`game/images/bg/<category>/<location>_<time>[_weather][_mood].<ext>`
- 背景图声明规则：`image bg <category>_<location>_<time>[_weather][_mood] = "images/bg/<category>/<location>_<time>[_weather][_mood].<ext>"`
- CG 路径规则：`game/images/cg/<arc>/<event_name>.<ext>` 或 `game/images/cg/routes/<route>/<event_name>.<ext>`
- CG 声明规则：`image cg <arc>_<event_name> = "images/cg/<arc>/<event_name>.<ext>"`
- 地点或时间变化时，用 `scene bg ...`
- 关键事件全屏插图时，用 `scene cg ...`
- 推荐格式：
  - 背景图：`jpg` 或 `webp`
  - CG：`webp` 或 `jpg`
  - 带透明的立绘/特效：`png` 或 `webp`

## Suggested Background Taxonomy / 建议的背景分类

English:

- `game/images/bg/school/`: gate, classroom, hallway, rooftop, practice room
- `game/images/bg/city/`: street, station, riverside, plaza
- `game/images/bg/stage/`: backstage, stage, rehearsal hall, auditorium
- `game/images/bg/interior/`: cafe, apartment, office, lounge
- `game/images/bg/special/`: memory, dream, filtered variants, stylized plates

中文：

- `game/images/bg/school/`：校门、教室、走廊、天台、练习室
- `game/images/bg/city/`：街道、车站、江边、广场
- `game/images/bg/stage/`：后台、舞台、排练厅、观众席
- `game/images/bg/interior/`：咖啡店、公寓、办公室、休息室
- `game/images/bg/special/`：回忆、梦境、滤镜版背景、特殊演出底图

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

- New character definitions go into `game/core/characters.rpy`.
- New standing art and expression declarations go into `game/core/images.rpy`.
- New reusable background declarations go into `game/core/bg_images.rpy`.
- New chapter/route CG declarations go into `game/core/cg_images.rpy`.
- Shared transforms and animation helpers go into `game/core/transforms.rpy`.
- Common flags and route variables go into `game/core/variables.rpy`.
- Plot writing should continue from `game/story/prologue/` and `game/story/chapter1/`.
- Shared repeated scenes should be extracted into `game/core/common_events.rpy`.

中文：

- 新角色定义写入 `game/core/characters.rpy`。
- 新立绘和表情差分声明写入 `game/core/images.rpy`。
- 新背景图声明写入 `game/core/bg_images.rpy`。
- 新章节/路线 CG 声明写入 `game/core/cg_images.rpy`。
- 通用站位、演出变换和动画辅助写入 `game/core/transforms.rpy`。
- 公共旗标、好感变量和路线变量写入 `game/core/variables.rpy`。
- 剧情正文继续在 `game/story/prologue/` 和 `game/story/chapter1/` 中推进。
- 多章节重复使用的公共片段应抽到 `game/core/common_events.rpy`。

## Suggested Next Steps / 建议的下一步

English:

1. Fill in the real prologue beats in `game/story/prologue/`.
2. Replace placeholder narration in `game/story/chapter1/` with the reunion draft.
3. Add reusable backgrounds under `game/images/bg/` and register them in `game/core/bg_images.rpy`.
4. Add event CG under `game/images/cg/` and register them in `game/core/cg_images.rpy`.
5. Add BGM and SFX aliases in `game/core/audio.rpy`.
6. Decide where the common route ends and where `route_xinyi` / `route_sinuo` begin.

中文：

1. 把 `game/story/prologue/` 里的占位内容替换成正式序章剧情。
2. 把 `game/story/chapter1/` 里的占位旁白替换成重逢章节草案。
3. 把可复用背景图放进 `game/images/bg/`，并在 `game/core/bg_images.rpy` 里统一注册。
4. 把事件 CG 放进 `game/images/cg/`，并在 `game/core/cg_images.rpy` 里统一注册。
5. 在 `game/core/audio.rpy` 里补全 BGM 和音效别名。
6. 明确共通线结束点，以及 `route_xinyi` / `route_sinuo` 的分流位置。
