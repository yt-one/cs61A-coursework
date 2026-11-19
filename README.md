# CS 61A Coursework · Fall 2026

UC Berkeley **CS 61A（Structure and Interpretation of Computer Programs）** 的个人学习仓库，用来记录 Homework、Lab 和 Project 的代码实现与解题笔记。[Fall 2026 课程主页](https://cs61a.org/fa26/)

## 收录进度

| 类别 | 内容 |
| --- | --- |
| Homework（课后作业） | [HW 04：Recursive Data](homeworks/hw04/) · [HW 05：List Mutation](homeworks/hw05/) |
| Lab（实验练习） | [Lab 04：Linked Lists](labs/lab04/) · [Lab 05：Trees](labs/lab05/) |
| Project（课程项目） | [Cats：计算机辅助打字软件](projects/cats/)，已完成 |

## Cats

打字测试项目，涵盖文本筛选、打字速度与准确率统计，以及基于编辑距离的拼写纠错。[官方题目](https://cs61a.org/fa26/projects/cats/)

- **已实现**　按主题筛选段落、计算打字准确率与每分钟词数、自动纠错、递归计算编辑距离、多人模式的进度上报与最快单词统计。
- **文件入口**　[代码实现](projects/cats/cats.py) · [中文题目](projects/cats/计算机辅助打字软件（CATS）.md)

在仓库根目录运行以下命令，启动单人打字测试。Ubuntu 上可用 `python3` 代替 `python`。

```bash
cd projects/cats
python cats.py -t
```

## Homework

- **HW 04 · Recursive Data**　链表与树的递归操作，以及基于递归数据结构的 Mobile 平衡判定。[代码](homeworks/hw04/hw04.py)
- **HW 05 · List Mutation**　嵌套列表的原地修改、可变列表与链表的互操作。[代码](homeworks/hw05/hw05.py)

## Lab

- **Lab 04 · Linked Lists**　链表的遍历、修改与构造。[代码](labs/lab04/lab04.py)
- **Lab 05 · Trees**　树的构造、遍历与叶子节点操作。[代码](labs/lab05/lab05.py)
