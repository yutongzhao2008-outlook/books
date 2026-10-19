# Karpathy 四种解释格式 PROMPT 模板

来源：`karpathy.jfif`（Andrej Karpathy, "Four Steps to Understand Anything with AI"）
用法：把 `{{TOPIC}}` 替换为你要理解的主题，然后把整段发给 AI。

## 核心思路

同一个主题，用四种方式理解：**文字 → 图 → 交互网页 → 动画视频**。

## 1. 简化语言（Plain Language）

```
Explain {{TOPIC}} using ASD-STE100.
```

- ASD-STE100 是为航空维护制定的受控英语，规则严格，文字清晰易读。
- 如果觉得太生硬，改用：

```
Explain {{TOPIC}} at about 80% of ASD-STE100 strictness.
```

## 2. 图示（Diagram）

适合看清结构、关系与流程。

```
Explain {{TOPIC}} with a clear diagram.
```

## 3. 交互式 HTML（Interactive HTML）

适合探索示例、拖动滑块、观看动画。

```
Build an interactive HTML explainer for {{TOPIC}}.
```

进阶写法：

```
Turn the explanation of {{TOPIC}} into an interactive webpage. Include examples, sliders and animations.
```

## 4. 讲解视频（Explainer Video）

适合用动态展示“概念如何一步步变化”。

```
Create a 3b1b-style video explainer on {{TOPIC}}.
```

## 选择格式

| 格式 | 适合场景 | 结果 |
|---|---|---|
| 简化语言 | 减少术语 | 清晰的解释 |
| 图示 | 看清关系 | 可视化结构 |
| HTML | 探索示例 | 交互式学习 |
| 视频 | 跟随变化 | 通过动态建立直觉 |

> 原文结尾：Code is abundant. Ask for custom apps and videos built around what you want to learn.
> 选择最适合你大脑理解的格式。
