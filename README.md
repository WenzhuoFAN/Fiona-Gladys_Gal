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

## Layer Rules / 层级规则

English:

- `options.rpy`, `gui.rpy`, `screens.rpy`: only system and UI settings.
- `core/`: only reusable definitions such as characters, images, transforms, variables, and audio aliases.
- `story/start.rpy`: only the project entry label and top-level flow handoff.
- `story/prologue/` and `story/chapter1/`: only chapter content, scene logic, and jumps.
- `story/routes/` and `story/endings/`: only branching flow and endings.

中文：

- `options.rpy`、`gui.rpy`、`screens.rpy`：只负责系统配置、界面样式和通用 UI。
- `core/`：只放可复用的底层定义，比如角色、立绘声明、通用变换、变量和音频别名。
- `story/start.rpy`：只作为主入口，负责把流程交给序章或主线起点。
- `story/prologue/` 和 `story/chapter1/`：只写章节剧情、场景演出和跳转逻辑。
- `story/routes/` 和 `story/endings/`：只处理分线推进和结局收束。

## Naming Rules / 命名规则

English:

- Labels: `pro_00_intro`, `ch1_01_old_stage`, `route_xinyi`, `ending_true`
- Variables: `aff_xinyi`, `aff_sinuo`, `flag_prologue_cleared`
- Images: `image xinyi normal`, `image sinuo normal`
- Audio aliases: `audio.bgm_prologue`, `audio.se_stage_door`

中文：

- 标签：`pro_00_intro`、`ch1_01_old_stage`、`route_xinyi`、`ending_true`
- 变量：`aff_xinyi`、`aff_sinuo`、`flag_prologue_cleared`
- 图片：`image xinyi normal`、`image sinuo normal`
- 音频别名：`audio.bgm_prologue`、`audio.se_stage_door`

## Collaboration Notes / 协作说明

English:

- New character definitions go into `core/characters.rpy`.
- New standing CG, expressions, and image declarations go into `core/images.rpy`.
- Shared transforms and animation helpers go into `core/transforms.rpy`.
- Common flags and route variables go into `core/variables.rpy`.
- Plot writing should continue from `story/prologue/` and `story/chapter1/`.
- Shared repeated scenes should be extracted into `core/common_events.rpy`.

中文：

- 新角色定义写入 `core/characters.rpy`。
- 新立绘、表情差分和图片声明写入 `core/images.rpy`。
- 通用站位、演出变换和动画辅助写入 `core/transforms.rpy`。
- 公共旗标、好感变量和路线变量写入 `core/variables.rpy`。
- 剧情正文继续在 `story/prologue/` 和 `story/chapter1/` 中推进。
- 多章节重复使用的公共片段应抽到 `core/common_events.rpy`。

## Suggested Next Steps / 建议的下一步

English:

1. Fill in the real prologue beats in `story/prologue/`.
2. Replace placeholder narration in `story/chapter1/` with the reunion draft.
3. Add background images under `images/bg/` and register them in `core/images.rpy`.
4. Add BGM and SFX aliases in `core/audio.rpy`.
5. Decide where the common route ends and where `route_xinyi` / `route_sinuo` begin.

中文：

1. 把 `story/prologue/` 里的占位内容替换成正式序章剧情。
2. 把 `story/chapter1/` 里的占位旁白替换成重逢章节草案。
3. 把背景图放进 `images/bg/`，并在 `core/images.rpy` 里统一注册。
4. 在 `core/audio.rpy` 里补全 BGM 和音效别名。
5. 明确共通线结束点，以及 `route_xinyi` / `route_sinuo` 的分流位置。
