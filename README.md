# CS 61A Coursework · Fall 2026

UC Berkeley **CS 61A（Structure and Interpretation of Computer Programs）** 的个人学习仓库，用来记录 Homework、Lab 和 Project 的代码实现与解题笔记。[Fall 2026 课程主页](https://cs61a.org/fa26/)

## 收录进度

| 类别 | 内容 |
| --- | --- |
| Homework（课后作业） | 待收录 |
| Lab（实验练习） | 待收录 |
| Project（课程项目） | [Cats：计算机辅助打字软件](projects/cats/)，实现中 |

## Cats

打字测试项目，涵盖文本筛选、打字速度与准确率统计，以及基于编辑距离的拼写纠错。[官方题目](https://cs61a.org/fa26/projects/cats/)

- **已有实现**　按主题筛选段落、计算打字准确率与每分钟词数、自动纠错和递归计算编辑距离。
- **待完成**　多人模式的进度上报、逐词计时与最快单词统计，以及额外挑战 `memo_diff` 和 `final_diff`。
- **文件入口**　[代码实现](projects/cats/cats.py) · [中文题目](projects/cats/计算机辅助打字软件（CATS）.md)

在仓库根目录运行以下命令，启动单人打字测试。Ubuntu 上可用 `python3` 代替 `python`。

```bash
cd projects/cats
python cats.py -t
```
