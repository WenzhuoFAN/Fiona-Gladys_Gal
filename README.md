# FionaGladysGal

## Current Layout

```text
FionaGladysGal/
+-- README.md
+-- options.rpy
+-- gui.rpy
+-- screens.rpy
+-- core/
|   +-- characters.rpy
|   +-- images.rpy
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
|   +-- cg/
|   +-- ui/
|   `-- characters/
`-- audio/
    +-- bgm/
    +-- se/
    `-- voice/
```

## Layer Rules

- `options.rpy`, `gui.rpy`, `screens.rpy`: only system and UI settings.
- `core/`: only reusable definitions such as characters, images, transforms, variables, audio aliases.
- `story/start.rpy`: only the project entry label and top-level flow handoff.
- `story/prologue/` and `story/chapter1/`: only chapter content and scene jumps.
- `story/routes/` and `story/endings/`: only branching and ending flow.

## 层级说明

- `options.rpy`、`gui.rpy`、`screens.rpy`：只负责系统配置、界面样式和通用 UI。
- `core/`：只放可复用的底层定义，比如角色、立绘声明、通用变换、变量、音频别名。
- `story/start.rpy`：只作为主入口，负责把流程交给序章或主线起点。
- `story/prologue/` 和 `story/chapter1/`：只写剧情内容、演出、选择和章节之间的跳转。
- `story/routes/` 和 `story/endings/`：只处理分线、收束和结局，不反向承担底层定义工作。

## Naming Rules

- Labels: `pro_00_intro`, `ch1_01_old_stage`, `route_xinyi`, `ending_true`
- Variables: `aff_xinyi`, `aff_sinuo`, `flag_prologue_cleared`
- Images: `image xinyi normal`, `image sinuo normal`
- Audio aliases: `audio.bgm_prologue`, `audio.se_stage_door`

## Collaboration Notes

- New character definitions go into `core/characters.rpy`.
- New standing CG and expressions go into `core/images.rpy`.
- Shared transforms and animation helpers go into `core/transforms.rpy`.
- Common flags and route variables go into `core/variables.rpy`.
- Plot writing should continue from `story/prologue/` and `story/chapter1/`.
- Shared repeated scenes should be extracted into `core/common_events.rpy`.

## Suggested Next Steps

1. Fill in the real prologue beats in `story/prologue/`.
2. Replace placeholder narration in `story/chapter1/` with the reunion draft.
3. Add background images under `images/bg/` and register them in `core/images.rpy`.
4. Add BGM and SFX aliases in `core/audio.rpy`.
5. Decide where the common route ends and where `route_xinyi` / `route_sinuo` begin.
