# 完整公开示例索引

模板中的研究内容来自公开的 Segment Anything（SAM）与 Vision Transformer（ViT）论文。两组是独立的页型案例，不是需要按顺序讲述的一份论文报告。使用时保留组织关系，替换为用户材料；页数与章节由实际任务决定。

制作前先看 [全稿预览](previews/overview.jpg)，再打开本次所选页的完整预览。背景与问题发现的具体迁移步骤见 [构图说明](composition.md)。原生编辑对象、备注来源和第 9 页动画保存在 `../assets/whu-template.pptx`。

| 模板页 | 用途与完整预览 | 值得迁移的组织方式 | 动画 |
|---|---|---|---|
| 1 | [封面](previews/page-01.png) | 建筑与校标构图、标题层级；按实际汇报填写身份 | 无 |
| 2 | [目录](previews/page-02.png) | 条目对应实际章节；六项只是可编辑示例 | 无 |
| 3 | [场景背景与需求](previews/page-03.png) | 左侧场景与约束、中部纵向结果及三组能力、右侧应用，底部结论 | 无 |
| 4 | [从实例发现问题](previews/page-04.png) | 大幅案例、四色定位框与引线，对应右侧两行解释，归纳共同问题 | 无 |
| 5 | [从观察到设计](previews/page-05.png) | 整体到局部观察、困难区、补充案例与机制，合并两条设计思路 | 无 |
| 6 | [实验观察与取舍](previews/page-06.png) | 两行独立受控实验，各自连接趋势解释、条件和取舍 | 无 |
| 7 | [问题与证据](previews/page-07.png) | 两种评测的曲线对照，各有协议、观察和条件 | 无 |
| 8 | [输入表示](previews/page-08.png) | 图像样例、投影图、尺寸演算、符号与含义并置 | 无 |
| 9 | [完整架构](previews/page-09.png) | 总体结构与编码器细节、分步说明及局部对应 | 四次点击 |
| 10 | [内部计算](previews/page-10.png) | 放大模块、计算公式、运算作用和迁移方式 | 无 |
| 11 | [数据与协议](previews/page-11.png) | 两张原生表格、评测区别及比较条件 | 无 |
| 12 | [结果与成本](previews/page-12.png) | 完整相关任务对照、均值与标准差、成本及结果边界 | 无 |
| 13 | [模型扩展](previews/page-13.png) | 两种评测图、控制条件、趋势和解释范围 | 无 |
| 14 | [机制分析](previews/page-14.png) | 三幅互补证据各对应具体解释，并标明模型差异 | 无 |
| 15 | [定性案例](previews/page-15.png) | 同一输入与可视化逐行对应，观察与机制推断分开 | 无 |
| 16 | [研究总结](previews/page-16.png) | 方法、观察、证据和条件形成对应表 | 无 |
| 17 | [结束页](previews/page-17.png) | 延续封面品牌构图 | 无 |

[背景、问题定位与设计思路预览](previews/new-pages.jpg)。动画演示：[架构图点击状态](previews/method-animation.gif)。此动画用于理解局部结构，不扩展到背景、普通技术路线或表格。

## 公开素材来源

- Kirillov et al., *Segment Anything*, ICCV 2023，[论文 v1](https://arxiv.org/abs/2304.02643v1)。第 3 页图像取自 Figure 4，输入类型、模型能力及应用据 §1–3、§7；点/框/掩码符号是可编辑输入示意，约 50 ms 不包含图像编码。第 4 页使用 Figure 3，四组文字描述图中四列有效案例，不声称四项独立失败实验。第 5 页使用 Figures 3–4，整体图、裁切放大、局部输出分别标明，最小损失反传及质量评分据 §3。第 6 页使用 Figure 13 中/右，解释据 §7.6，是实验后观察，不伪称事前研究动机。原图内容保持真实，新增定位框、引线与文字均可编辑。
- Dosovitskiy et al., *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*, ICLR 2021，[论文 v2](https://arxiv.org/abs/2010.11929v2)。第 7 页使用 Figures 3–4；第 11 页据 §4.1 与 Table 1；第 12 页选取 Table 2 的三列模型并保留全部七项任务及计算成本；第 13–15 页分别使用 Figures 5、7、6。解释来自对应正文，表格保留原文数值与误差。
- 第 8–10 页的架构及局部图来自 [Google Research 官方架构图](https://github.com/google-research/vision_transformer/blob/main/vit_figure.png)，公式与定义见原论文 §3.1–3.2。第 8 页的 224 × 224 尺寸为明确标注的演算示例。
- 品牌资源位于 `../assets/whu/`。图像出处、裁切范围与使用方式也记录在相应幻灯片备注中。

公开示例只是制作参照，不能把示例论文的事实、结果或研究归属移入其他任务。新增可分发示例同样需要可追溯的公开来源。
