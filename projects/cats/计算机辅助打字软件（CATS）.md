# 计算机辅助打字软件（CATS）

- **截止时间：** 10 月 2 日星期五晚上 11:59
- **阶段检查截止时间：** 9 月 28 日星期一晚上 11:59
- **分值：** 20 分
- **下载：** [cats.zip](https://cs61a.org/fa26/projects/cats/cats.zip)

要获得本项目的成绩，你必须完成每一道题，然后参加一次关于你所写解答的简短验收面谈。你可以使用 Preceptor 进行面谈，也可以在 Office Hours 期间由课程工作人员对你进行面谈。如果面谈无法正常进行，仍请按时提交可运行的代码，或在截止日期前申请延期。

**在作业截止日期（包括任何已获批准的延期）之后的 3 个工作日内，工作人员会安排线下验收。** 如果验收时间距离原始截止日期超过 3 个工作日，工作人员可能会要求通过 Flextensions 确认你的延期截止日期。

你需要提交一个 Provenance 提交包，其中包含你使用 VS Code 的记录，包括与 Preceptor 的交互记录。本作业不得使用 Preceptor 以外的 AI 工具。

> 程序员梦想着  
> 抽象、递归，  
> 以及飞快地打字。

## 重要提交说明

要获得完整分数：

- 在 **9 月 28 日星期一** 前提交已完成阶段 1 和阶段 2 的版本，占 1 分。
- 在 **10 月 2 日星期五** 前提交完整项目。

请尽量按照题目顺序完成，并在推进过程中运行每道题的测试，因为后面某些题目的实现会依赖前面的题目。

你可以与一名搭档共同完成本项目。

如果你在 **10 月 1 日星期四** 前提交整个项目，可以获得 1 分奖励分。项目截止日期和阶段检查截止日期可以申请延期，但提前提交截止日期不能延期；除非你是 DSP 学生，并且获得了作业延期方面的合理便利安排。

## 简介

在本项目中，你将编写一个测量打字速度的程序。此外，你还将实现打字自动更正功能：用户输入一个单词后，该功能会尝试更正其拼写。

本项目的灵感来自 [TypeRacer](https://play.typeracer.com/)。

## 最终成品

你可以在 [cats.cs61a.org](https://cats.cs61a.org/) 上体验课程工作人员提供的项目解答，现在就可以试一试。

完成本项目后，你将亲自实现其中很大一部分功能，包括多人模式！

## 下载初始文件

首先，以 [ZIP 压缩包](https://cs61a.org/fa26/projects/cats/cats.zip) 的形式下载全部项目代码。以下是解压后会看到的文件。本项目中，你只需要修改 [`cats.py`](https://cs61a.org/fa26/projects/cats/cats.py.html)。

- [`cats.py`](https://cs61a.org/fa26/projects/cats/cats.py.html)：打字测试的逻辑。
- [`utils.py`](https://cs61a.org/fa26/projects/cats/utils.py.html)：用于操作文件和字符串的工具函数。
- [`ucb.py`](https://cs61a.org/fa26/projects/cats/ucb.py.html)：CS 61A 项目使用的工具函数。
- [`data/sample_passages.txt`](https://cs61a.org/fa26/projects/cats/data/sample_passages.txt.html)：供用户输入的文本示例。这些内容是从不同主题的维基百科文章中抓取而来的。
- [`data/common_words.txt`](https://cs61a.org/fa26/projects/cats/data/common_words.txt.html)：按出现频率排序的常见英语单词。
- [`data/words.txt`](https://cs61a.org/fa26/projects/cats/data/words.txt.html)：更多按出现频率排序的英语单词。
- [`data/final_diff_words.txt`](https://cs61a.org/fa26/projects/cats/data/final_diff_words.txt.html)：更多英语单词！
- `data/testcases.out`：可选 Final Diff 扩展的测试用例。
- [`cats_gui.py`](https://cs61a.org/fa26/projects/cats/cats_gui.py.html)：基于 Web 的图形用户界面（GUI）所使用的 Web 服务器。
- `gui_files`：图形用户界面所需的文件目录。
- `tests`：pytest-grader 测试套件。
- [`score.py`](https://cs61a.org/fa26/projects/cats/score.py.html)：可选 Final Diff 扩展的一部分。

你可能还会看到上面未列出的其他文件，它们是测试运行器及部分 GUI 正常工作所必需的。**除了 `cats.py`，请不要修改任何其他文件。**

## 计分说明

本项目共 20 分：

- 19 分用于评估正确性。
- 1 分用于奖励在阶段检查截止日期前提交阶段 1 和阶段 2。

## 入门视频

[这些视频](https://www.youtube.com/playlist?list=PLAgL9fR__tSs)可能为你完成本作业中的编程问题提供一些方向。

观看这些视频时，你需要登录自己的 `berkeley.edu` 邮箱。

# 阶段 1：打字

**提醒：** 整个项目中，我们只修改 `cats.py` 中的函数。

## 问题 1（1 分）

实现 `pick`。该函数用于选择用户在打字测试中需要输入的文章。

它接受三个参数：

- `passages`：候选文章组成的列表，列表元素为字符串。
- `select`：一个函数，用于评估一篇文章。如果文章符合特定条件，则返回 `True`，否则返回 `False`。
- `k`：一个非负整数，表示在所有符合条件的文章中，目标文章的索引。

`pick` 函数返回 `passages` 中第 `k` 个使 `select` 函数返回 `True` 的文章。

如果不存在这样的文章，即 `k` 大于或等于符合条件的文章数量，则 `pick` 返回空字符串。

**提示：** 不需要关心 `select` 函数的具体实现。只需假设它接受一篇文章作为输入，并返回 `True` 或 `False`。

**提醒：** 索引从 0 开始。如果 `k` 为 0，则需要选择第一篇符合条件的文章。

```bash
python3 -m pytest -k q01 --unlock
```

解锁示例：

```python
>>> from cats import pick
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> pick(ps, s, 0)  # 记得给字符串加上引号（''）！
______
>>> pick(ps, s, 1)
______
>>> pick(ps, s, 2)
______
```

```bash
python3 -m pytest -k q01
```

## 问题 2（1 分）

实现 `about` 函数。它接受一个名为 `keywords` 的单词列表，并返回一个函数。

返回的函数在接受一篇文章后，会检查该文章是否包含 `keywords` 中的任意单词。如果文章中出现了关键词列表中的任意单词，则返回 `True`，否则返回 `False`。

实现 `about` 后，就可以把它返回的函数作为 `pick` 的 `select` 参数。这样便能根据文章是否包含传给 `about` 的关键词列表中的任意单词来筛选文章。在继续开发打字测试时，这一功能会很有用。

为了确保比较准确，你需要：

1. 忽略大小写，将大写字母和小写字母视为等价。
2. 忽略文章中的标点符号。
3. 只检查是否与 `keywords` 列表中的单词完全匹配，而不是检查子字符串。例如，文章中的 `"dogs"` 不应与关键词中的 `"dog"` 匹配。

**提示：** 使用 `utils.py` 中的 `split`、`lower` 和 `remove_punctuation` 函数。

```bash
python3 -m pytest -k q02 --unlock
```

解锁示例：

```python
>>> from cats import about
>>> from cats import pick
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A passage about cats.')
______
>>> dogs('A passage about dogs.')
______
>>> dogs('Release the Hounds!')
______
>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
______
>>> dogs('Do gs and ho unds don\'t count')
______
>>> dogs("AdogsPassage")
______
```

```bash
python3 -m pytest -k q02
```

## 问题 3（2 分）

实现 `accuracy`。它接受用户输入的文章 `typed` 和原始文章 `source`，返回 `typed` 中与 `source` 对应单词完全匹配的单词百分比。

大小写和标点符号也必须匹配。“对应”是指 `typed` 中的每个单词必须与 `source` 中相匹配的单词处于相同位置。换句话说，`typed` 的第一个单词必须匹配 `source` 的第一个单词，第二个单词必须匹配第二个单词，依此类推。

在这里，**单词**是由空白字符与其他单词分隔开的任意字符序列。因此，应将 `"dog;"` 这样的序列视为一个单词。

在实际打字测试中，`typed` 表示玩家已经输入的内容，`source` 表示玩家尝试复现的文章。

- 如果 `typed` 比 `source` 长，那么 `typed` 中那些在 `source` 里没有对应单词的多余单词全部算作**错误**。
- 如果 `typed` 比 `source` 短，并且到目前为止 `typed` 中的所有单词都与 `source` 对应，则准确率为 `100.0`。
- 如果 `typed` 和 `source` 都为空，则准确率为 `100.0`。
- 如果 `typed` 为空而 `source` 非空，则准确率为 `0.0`。
- 如果 `typed` 非空而 `source` 为空，则准确率为 `0.0`。

```bash
python3 -m pytest -k q03 --unlock
```

解锁示例：

```python
>>> from cats import accuracy
>>> accuracy("12345", "12345")  # 应返回 100.0，而不是整数 100！
______
>>> accuracy("a b c", "a b c")
______
>>> accuracy("a  b  c  d", "b  a  c  d")
______
>>> accuracy("a b", "c d e")
______
>>> accuracy("Cat", "cat")  # 该函数区分大小写
______
>>> accuracy("a b c d", "a d")
______
>>> accuracy("abc", " ")
______
>>> accuracy("a b \tc", "a b c")  # 制表符本身不计为单词
______
>>> accuracy("abc", "")
______
>>> accuracy("", "abc")
______
>>> accuracy("a b c d", "b c d")
______
>>> accuracy("cats.", "cats")  # 标点符号也计入比较
______
>>> accuracy("", "")  # 返回 100.0
______
```

```bash
python3 -m pytest -k q03
```

## 问题 4（1 分）

实现 `wpm`，根据字符串 `typed` 和以**秒**为单位的已用时间 `elapsed`，计算**每分钟单词数**，即一种打字速度的度量。

尽管名为“每分钟单词数”，它并不是根据实际输入的单词数量计算的，而是根据每 5 个字符组成一组的数量计算，从而避免打字测试受到单词长度差异的影响。

每分钟单词数的计算公式为：将输入的字符总数（包括空格）除以 5（平均单词长度），再将结果除以以**分钟**为单位的已用时间。

例如，字符串 `"I am glad!"` 包含 10 个字符，不包括引号。计算时将输入单词数视为 2，因为 `10 / 5 = 2`。如果某人在 30 秒，即半分钟内输入了该字符串，其打字速度就是每分钟 4 个单词。

```bash
python3 -m pytest -k q04 --unlock
```

解锁示例：

```python
>>> from cats import wpm
>>> wpm("12345", 3)  # 注意：wpm 返回浮点数，即带小数点的数
______
>>> wpm("a b c", 20)
______
>>> wpm("", 10)
______
```

```bash
python3 -m pytest -k q04
```

**现在可以测试你的打字速度了！**

你可以使用命令行，针对特定主题的文章测试打字速度。例如，下面的命令会加载关于猫或小猫的文章。如果感兴趣，可以查看 `run_typing_test` 函数的实现；该函数已经为你定义好了。

```bash
python3 cats.py -t cats kittens
```

你也可以使用以下命令体验基于 Web 的图形用户界面：

```bash
python3 cats_gui.py
```

关闭浏览器中的标签页后，可能还需要在终端中按 `Ctrl+C` 或 `Cmd+C` 才能退出 GUI。

# 阶段 2：自动更正

在基于 Web 的 GUI 中，有一个“Enable Auto-Correct”（启用自动更正）选项，但它目前没有任何作用。接下来要实现自动拼写错误更正。

每当用户按下空格键时，如果其最后输入的单词与词典中的任何单词都不匹配，但与某个单词很接近，就使用这个相近的单词替换用户输入的内容。

## 问题 5（2 分）

实现 `autocorrect`。它接受 `typed_word`、`word_list`、`diff_function` 和 `limit`。

`autocorrect` 的目标是：根据 `diff_function` 的判断，返回 `word_list` 中与给定 `typed_word` 最接近的单词。

具体来说，`autocorrect` 执行以下操作：

- 如果 `typed_word` 已包含在 `word_list` 中，则直接返回该单词。
- 否则，返回 `word_list` 中与 `typed_word` 差异最小的单词。这里的差异是 `diff_function` 返回的数值。
- 但是，如果 `typed_word` 与 `word_list` 中所有单词的最小差异仍然大于 `limit`，则返回 `typed_word` 本身。换句话说，`limit` 设置了一个最大阈值，规定拼写错误严重到什么程度时仍可以进行更正。

假设 `typed_word` 和 `word_list` 中的所有元素均为小写，且不含标点符号。

**重要：** 如果 `word_list` 中有多个字符串与 `typed_word` 的差异并列最小，`autocorrect` 应返回在 `word_list` 中出现最早，即索引最小的字符串。

差异函数接受三个参数：

1. `typed_word`。
2. 原始单词，在这里是 `word_list` 中的某个单词。
3. `limit`。

差异函数输出一个数字，表示两个字符串之间的差异程度。

下面是一个差异函数示例，它计算 `1 + limit` 与两个输入字符串长度差之间的较小值：

```python
>>> def length_diff(w1, w2, limit):
...     return min(limit + 1, abs(len(w2) - len(w1)))
>>> length_diff('mellow', 'cello', 10)
1
>>> length_diff('hippo', 'hippopotamus', 5)
6
```

**注意：** 为了简洁，一些解锁测试在定义 lambda 函数时使用了三元运算符。三元运算符是 `if` 语句的单行形式。

例如，在一个测试中，差异函数定义为：

```python
first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
```

如果 `w1` 和 `w2` 的首字符不同，该 lambda 函数返回 1，否则返回 0。

**注意：** 如果希望选用一行实现，可以尝试使用 `max` 或 `min`，并传入可选的 `key` 参数。`key` 接受一个单参数函数。例如，`max([-7, 2, -1], key=abs)` 会返回 `-7`，因为 `abs(-7)` 大于 `abs(2)` 和 `abs(-1)`。

```bash
python3 -m pytest -k q05 --unlock
```

解锁示例：

```python
>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
______
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
______
>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
______
>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
______
>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
______
>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
______
>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
______
```

```bash
python3 -m pytest -k q05
```

## 问题 6（3 分）

实现 `furry_fixes`，它是一个可以传给 `autocorrect` 的 `diff_function` 参数的差异函数。

该函数接受两个字符串，返回为了将 `typed` 单词转换为 `source` 单词，最少需要修改的字符数量。如果两个字符串长度不同，还需要将长度差计入修改总数。

例如：

```python
>>> big_limit = 10
>>> furry_fixes("nice", "rice", big_limit)  # 替换：n -> r
1
>>> furry_fixes("range", "rungs", big_limit)  # 替换：a -> u，e -> s
2
>>> furry_fixes("pill", "pillage", big_limit)  # 不需要替换，长度差为 3
3
>>> furry_fixes("goodbye", "good", big_limit)  # 不需要替换，长度差为 3
3
>>> furry_fixes("roses", "arose", big_limit)  # 替换：r -> a，o -> r，s -> o，e -> s，s -> e
5
>>> furry_fixes("rose", "hello", big_limit)  # 替换：r -> h，o -> e，s -> l，e -> l，长度差为 1
5
```

**重要：** 实现中不得使用 `while`、`for` 或列表推导式。请使用递归。

如果需要修改的字符数大于 `limit`，`furry_fixes` 应返回任意一个大于 `limit` 的数，并尽量减少为此所需的计算量。

为什么要有 `limit`？根据问题 5，`autocorrect` 会拒绝任何与 `typed` 单词的差异大于 `limit` 的 `source` 单词。差异比 `limit` 大 1 还是大 100 并不重要，`autocorrect` 都会同样拒绝它。

因此，一旦确定差异已经超过 `limit`，就应当停止递归调用以节省时间，即使最终返回的差异值不再精确。

下面两次 `furry_fixes` 调用所需的求值时间应当大致相同：

```python
>>> limit = 4
>>> furry_fixes("roses", "arose", limit) > limit
True
>>> furry_fixes("rosesabcdefghijklm", "arosenopqrstuvwxyz", limit) > limit
True
```

为了确保你确实通过在达到 `limit` 后停止递归节省了时间，自动评分器会包含一项测试，根据函数调用次数衡量解答的性能。如果未通过该测试，请考虑增加一个与 `limit` 有关的基本情况。

**提示：** 解决本题需要不止一个基本情况。

### 字符串切片

字符串是字符序列，字母、数字和标点符号都属于字符。字符串的切片是另一个字符串，其中包含原字符串的一部分字符。

例如：

```python
>>> a = 'strap'
>>> a[0]
's'
>>> a[1:]
'trap'
>>> a[2:]
'rap'
>>> a[1:][1:]
'rap'
```

```bash
python3 -m pytest -k q06 --unlock
```

解锁示例：

```python
>>> from cats import furry_fixes, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> furry_fixes("car", "cad", big_limit)
______
>>> furry_fixes("this", "that", big_limit)
______
>>> furry_fixes("one", "two", big_limit)
______
>>> furry_fixes("from", "form", big_limit)
______
>>> furry_fixes("awe", "awesome", big_limit)
______
>>> furry_fixes("awful", "awesome", big_limit)
______
>>> furry_fixes("awful", "awesome", 3) > 3
______
>>> furry_fixes("awful", "awesome", 4) > 4
______
>>> furry_fixes("awful", "awesome", 5) > 5
______
```

```bash
python3 -m pytest -k q06
```

尝试在 GUI 中启用自动更正。它能让你打得更快吗？更正结果准确吗？

## 问题 7（3 分）

实现 `minimum_mewtations`，这是一个可用于 `autocorrect` 的更高级差异函数。它返回将 `typed` 单词转换为 `source` 单词所需的**最少**编辑操作次数。

共有三种编辑操作：

| 操作 | 示例 |
|---|---|
| 向 `typed` 中添加一个字母 | 向 `"itten"` 添加 `"k"`，得到 `"kitten"` |
| 从 `typed` 中删除一个字母 | 从 `"scat"` 中删除 `"s"`，得到 `"cat"` |
| 将 `typed` 中的一个字母替换为另一个字母 | 将 `"zaguar"` 中的 `"z"` 替换为 `"j"`，得到 `"jaguar"` |

每次编辑操作都会使两个单词之间的差异增加 1。

```python
>>> big_limit = 10
>>> minimum_mewtations("cats", "scat", big_limit)  # cats -> scats -> scat
2
>>> minimum_mewtations("purng", "purring", big_limit)  # purng -> purrng -> purring
2
>>> minimum_mewtations("ckiteus", "kittens", big_limit)  # ckiteus -> kiteus -> kitteus -> kittens
3
```

`cats.py` 中已经提供了一个实现模板。你可以随意修改该模板，也可以将其完全删除。

**提示：** `minimum_mewtations` 中的某个递归调用会与 `furry_fixes` 类似。不过，由于 `minimum_mewtations` 考虑三种特定的编辑操作——添加、删除和替换，因此还需要其他递归调用来处理这些情况。

如果所需的编辑次数大于 `limit`，`minimum_mewtations` 应返回任意一个大于 `limit` 的数，例如 `limit + 1`，并应在达到限制后停止递归调用以节省时间。

下面两次 `minimum_mewtations` 调用所需的求值时间应当大致相同：

```python
>>> limit = 2
>>> minimum_mewtations("ckiteus", "kittens", limit) > limit
True
>>> minimum_mewtations("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
True
```

为了确保代码在达到 `limit` 后停止递归调用，自动评分器会包含一项测试，根据函数调用次数衡量解答的性能。

**重要：** 在实现 `minimum_mewtations` 时，不应使用任何辅助函数，否则自动评分测试可能失败。

**重要：** 准备测试实现时，请记得删除下面这行代码：

```python
assert False, 'Remove this line'
```

```bash
python3 -m pytest -k q07 --unlock
```

解锁示例：

```python
>>> from cats import minimum_mewtations, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> minimum_mewtations("wind", "wind", big_limit)
______
>>> minimum_mewtations("wird", "wiry", big_limit)
______
>>> minimum_mewtations("wird", "bird", big_limit)
______
>>> minimum_mewtations("wird", "wires", big_limit)
______
>>> minimum_mewtations("wird", "bwird", big_limit)
______
>>> minimum_mewtations("speling", "spellings", big_limit)
______
>>> minimum_mewtations("hash", "ash", big_limit)
______
>>> minimum_mewtations("ash", "hash", big_limit)
______
>>> minimum_mewtations("roses", "arose", big_limit)  # roses -> aroses -> arose
______
>>> minimum_mewtations("tesng", "testing", big_limit)  # tesng -> testng -> testing
______
>>> minimum_mewtations("rlogcul", "logical", big_limit)  # rlogcul -> logcul -> logicul -> logical
______
>>> minimum_mewtations("", "", big_limit)  # 空字符串变为空字符串不需要编辑
______
```

```bash
python3 -m pytest -k q07
```

再次启用自动更正并输入。这次的更正结果是否更加准确？

```bash
python3 cats_gui.py
```

## 可选：Final Diff 扩展（0 分）

你可以选择设计自己的差异函数 `final_diff`。下面是一些让更正更加准确的方向：

- 考虑哪些添加和删除操作比其他操作更可能发生。例如，如果某个字母连续出现两次，那么不小心漏掉其中一个字母的可能性会更高。
- 将两个相邻字母交换位置视为一次修改，而不是两次。
- 尝试纳入常见的拼写错误。
- 键盘上彼此相邻的字母更容易被相互替换。

你还可以通过修改 `cats.py` 中变量 `FINAL_DIFF_LIMIT` 的值，设置希望差异函数使用的限制。

运行以下命令，可以检查 `final_diff` 在提供的常见拼写错误数据集上的成功率：

```bash
python3 score.py
```

如果不知道从哪里开始，可以尝试把 `furry_fixes` 和 `minimum_mewtations` 的代码复制粘贴到 `final_diff` 中并运行评分。观察它们修正了哪些拼写错误、没有修正哪些拼写错误，可能会给你带来一些想法。

## 阶段检查提交

检查是否已完成阶段 1 和阶段 2 中的所有问题：

```bash
python3 -m pytest --score
```

运行 pytest 时，你仍会看到一些测试处于锁定状态，因为尚未完成整个项目。只要正确完成到目前为止的所有问题，就可以获得阶段检查的全部分数。

确认满意后，提交阶段检查：

1. 在 VS Code 命令面板中运行 `Provenance: Prepare Submission Bundle`。
2. 将生成的 ZIP 文件上传至 Gradescope 上的 **Cats Checkpoint** 作业。

请务必在 **9 月 28 日星期一** 的阶段检查截止日期前提交。

如需回顾如何使用 Provenance 创建并提交 ZIP 文件，请参考 Lab 00。

每位搭档都必须提交由自己亲自输入的项目版本。

# 阶段 3：多人模式

和朋友一起打字会更有趣！现在你将实现多人功能。

在自己的计算机上运行 `cats_gui.py` 后，它会连接到位于 `cats.cs61a.org` 的课程服务器，并寻找另一位玩家进行比赛。

与朋友比赛时，会有 5 个不同的程序同时运行：

1. **你的 GUI**：在 Web 浏览器中处理所有文本着色和显示。
2. **你的 `cats_gui.py`**：一个 Web 服务器，使用你在 `cats.py` 中编写的代码与 GUI 通信。
3. **对手的 `cats_gui.py`**。
4. **对手的 GUI**。
5. **CS 61A 多人服务器**：负责匹配玩家并传递消息。

当你输入时，GUI 会将你已输入的内容上传到自己的 `cats_gui.py` 服务器。该服务器计算你的进度并返回进度更新。

该服务器还会向 CS 61A 多人服务器上传进度更新，使对手的 GUI 也能显示你的进度。

与此同时，你的 GUI 会不断向 `cats_gui.py` 请求对手的进度更新，以保持显示内容为最新状态；`cats_gui.py` 再从多人服务器获取这些信息。

每位玩家都有一个 `id` 编号，服务器使用该编号跟踪打字进度。

## 问题 8（2 分）

实现 `report_progress`。每当用户输入完一个单词时，都会调用该函数。

它接受：

- `typed`：用户目前已经输入的单词列表。
- `source`：原始文本中的单词列表。
- `user_id`：用户 ID。
- `upload`：用于向多人服务器上传进度报告的函数。

`typed` 中的单词数量永远不会超过 `source`。

你的进度是一个比值：从开头到第一个错误单词之前，你已经正确输入的 `source` 单词数量，除以 `source` 的单词总数。

例如，下面的进度为 `0.25`：

```python
report_progress(["Hello", "ths", "is"], ["Hello", "this", "is", "wrong"], ...)
```

`report_progress` 函数应当：

1. 调用 `upload` 函数，向多人服务器上传一条消息。传入的字典包含两个键：`'id'` 和 `'progress'`。
   - `'id'` 应设置为用户的 `user_id`。
   - `'progress'` 应保存按照上述定义计算出的用户进度。
2. 返回计算出的用户进度。

**提示：** 下面的字典展示了 `upload` 函数可能收到的一种输入。它表示 `user_id` 为 4、`progress` 为 0.6 的玩家。

```python
{'id': 4, 'progress': 0.6}
```

```bash
python3 -m pytest -k q08 --unlock
```

解锁示例：

```python
>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> typed = ['I', 'have', 'begun']
>>> source = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
______
>>> report_progress(typed, source, 1, print_progress)  # 使用报告调用 print_progress
______
______
>>> report_progress(['I', 'begun'], source, 2, print_progress)
______
______
>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], source, 3, print_progress)
______
______
```

```bash
python3 -m pytest -k q08
```

## 问题 9（1 分）

实现 `time_per_word`。它接受两个参数：

- `words`：玩家正在输入的单词列表。
- `player_timestamps`：由列表组成的列表。每个内部列表包含时间戳，表示对应玩家完成输入 `words` 中各个单词的时间。

该函数应返回一个具有以下结构的字典：

- `'words'`：玩家正在输入的单词列表。
- `'times'`：由列表组成的列表 `times`，保存每位玩家输入每个单词所花费的时长。

具体来说，`times[i][j]` 应表示玩家 `i` 输入 `words[j]` 所花费的时间。

该时长等于玩家完成输入 `words[j]` 的时间，减去完成输入 `words[j-1]` 的时间。对于 `words[0]`，则等于玩家完成输入 `words[0]` 的时间减去玩家开始输入的时间。

参数 `player_timestamps` 中的时间戳是**累计且始终递增的**，而 `times` 中的值是**每位玩家相邻时间戳之间的差值**。

例如，如果：

```python
player_timestamps = [[1, 3, 5], [2, 5, 6]]
```

那么：

```python
times = [[2, 2], [3, 1]]
```

第一位玩家在时间点 1、3、5 完成各个单词，第二位玩家在时间点 2、5、6 完成各个单词。因此，第一位玩家的时间差为 `(3-1)`、`(5-3)`，第二位玩家的时间差为 `(5-2)`、`(6-5)`。

`player_timestamps` 中每个内部列表的第一个值表示对应玩家的初始开始时间。

```bash
python3 -m pytest -k q09 --unlock
```

解锁示例：

```python
>>> from cats import *
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> words_and_times = time_per_word(words, p)
>>> words, times = words_and_times['words'], words_and_times['times']
>>> words
______
>>> times
______
>>> p = [[0, 2, 3], [2, 4, 7]]
>>> words_and_times = time_per_word(['hello', 'world'], p)
>>> words, times = words_and_times['words'], words_and_times['times']
>>> words
______
>>> words[1]
______
>>> times
______
>>> times[0][1]
______
```

```bash
python3 -m pytest -k q09
```

## 问题 10（3 分）

实现 `fastest_words`，返回每位玩家输入速度最快的单词。

所有玩家完成输入后，会调用一次该函数。它接受 `time_per_word` 返回的字典。

`fastest_words` 返回一个由单词列表组成的列表，每位玩家对应一个内部列表。嵌套列表的索引表示玩家编号。每位玩家的列表包含其输入速度快于其他所有玩家的单词。

如果出现平局，则索引最小的玩家被视为输入该单词最快的玩家。

例如，两名玩家输入 `Just have fun`：

- 玩家 0 输入 `'fun'` 最快，用时 3 秒。
- 玩家 1 输入 `'Just'` 最快，用时 4 秒。
- 两人输入 `'have'` 都用了 1 秒，因此玩家 0 因索引较小而被视为输入 `'have'` 最快。

```python
>>> player_0 = [5, 1, 3]
>>> player_1 = [4, 1, 6]
>>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [player_0, player_1]})
[['have', 'fun'], ['Just']]
```

使用已提供的辅助函数 `get_time`，从 `times` 中获取单个时间。当尝试访问不存在的时间时，它会提供有用的错误信息。

```python
def get_time(times, player_num, word_index):
    """根据 time_per_word 返回的时间列表，
    返回玩家 player_num 输入 word_index 处单词所花费的时间。"""
```

**重要：** 确保实现不会修改给定的玩家输入列表。对于上面的示例，对 `[player_0, player_1]` 调用 `fastest_words` 不应修改 `player_0` 或 `player_1`。

玩家数量不一定总是两人，因此请将该函数推广为能够处理不确定数量的玩家。

```bash
python3 -m pytest -k q10 --unlock
```

解锁示例：

```python
>>> from cats import fastest_words, get_time
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> get_time([p0, p1], 0, 1)
______
>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})
______
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})  # 平局时选择第一位玩家
______
>>> p2 = [4, 3, 1]
>>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1, p2]})
______
```

```bash
python3 -m pytest -k q10
```

恭喜！现在你可以与课程中的其他学生比赛了。

将 `cats.py` 底部附近的 `enable_multiplayer` 设置为 `True`，然后快速打字吧！

```bash
python3 cats_gui.py
```

# 项目提交

对所有问题运行 pytest，确保所有测试均已解锁并通过：

```bash
python3 -m pytest
```

你也可以检查项目各部分的得分：

```bash
python3 -m pytest --score
```

确认满意后，提交本作业：

1. 在 VS Code 命令面板中运行 `Provenance: Prepare Submission Bundle`。
2. 将生成的 ZIP 文件上传到 Gradescope。

如需回顾提交流程，请参考 Lab 00。

每位搭档都必须提交由自己亲自输入的项目版本。

# 阶段 4：效率（额外挑战）

## 可选问题 EC（0 分）

**注意：** 本题为**可选题**，**不计分**。它是为有兴趣提高代码效率的学生准备的额外挑战。

只有在完成项目中的其他所有问题后，才应尝试本题。

在 Office Hours 和 Project Parties 期间，工作人员会优先帮助解决必做题目的学生。除非排队人数为空，否则不会提供本题相关的帮助。

在本题中，你将实现记忆化装饰器，通过“记住”计算量较大的操作结果来提高程序效率。

请确保熟悉装饰器和记忆化。如需复习，可查看以下内容。

### 装饰器

Python 装饰器允许在不改变既有函数结构的情况下修改该函数。

具体来说，装饰器函数是一种高阶函数，它：

- 接受原函数作为输入。
- 返回一个功能经过修改的新函数。
- 这个新函数必须接受与原函数相同的参数。

下面是一个装饰器示例，它会使一个单输入函数执行两次：

```python
>>> def do_twice(original_function):
...     def repeat(x):
...         original_function(x)
...         original_function(x)
...     return repeat
```

可以在多种场景中使用该函数：

```python
# 将一个值打印两次
>>> @do_twice
... def print_value(x):
...     print(x)
...
>>> print_value(5)
5
5

# 将一个元素添加到列表中两次
>>> lst = []
>>> @do_twice
... def add_to_list(item):
...     lst.append(item)
...
>>> add_to_list(5)
>>> lst
[5, 5]
```

此外，也可以直接调用装饰器函数，而不是使用 `@` 语法，例如：

```python
print_value = do_twice(print_value)
```

不过，通常将装饰器直接放在被修改函数的上方更有用，因为这样可以更清楚地说明代码中的函数如何被修改。

### 记忆化

注意，前面问题中编写的差异函数效率很低：计算机可能会多次进行相同的递归调用。对于一个具有多个参数和三个递归调用的函数，这一点可能不太容易看出。可以先通过课堂上定义的 `fib` 函数来观察。

在上面的树状图中，可以看到许多重复的递归调用。我们的目标是让程序保存已经求值的递归调用结果，以便将来出现相同调用时直接复用。

例如，`fib(5)` 的第一个分支会调用尚未求值的 `fib(3)`，因此必须执行其后续所有递归调用才能求得返回值。然而，当之后遇到作为 `fib(4)` 分支的 `fib(3)` 调用时，已经得到过它的返回值。

如果有办法将这些信息存储在称为**缓存**的结构中，并在需要时取出，就可以避免不必要的计算。这样便不必再对其分支 `fib(1)` 和 `fib(2)` 进行后续递归调用。

这就是**记忆化**的概念：将计算成本较高的结果存入缓存，并在重复执行相同操作时从缓存中取出信息。

本项目将使用两个记忆化装饰器。

`memo` 是一个通用的装饰器，可以对其标注的函数进行记忆化：

- 如果 `memo` 遇到从未见过的输入，会将计算结果存入缓存。
- 如果 `memo` 收到已经见过的输入，会直接取出缓存中的值并返回，不再进行额外计算。

`memo` 的完整实现已经提供。

你的任务是实现 `memo_diff`。

`memo_diff` 是一个高阶函数，接受 `diff_function`，并返回另一个名为 `memoized` 的差异函数。与所有差异函数一样，`memoized` 接受 `typed`、`source` 和 `limit`。

`memoized` 应当执行以下操作：

- 第一次遇到某个 `(typed, source)` 对时，使用 `diff_function` 计算差异，并将该值连同所使用的 `limit`，以 `(value, limit)` 元组的形式存入缓存。
- 再次遇到该 `(typed, source)` 对时，如果提供的 `limit` 小于或等于缓存中的 `limit`，则返回缓存的值。
- 否则，重新计算差异、更新缓存并返回结果。

**重要：** 实现该函数时，请确保使用元组而不是列表将值对存入缓存。字典中的键必须是**不可变的**，因此可以使用元组，但不能使用列表。

### 为什么 `memo_diff` 与 `memo` 不同？

`memo` 只保存函数调用的结果，而 `memo_diff` 还会考虑一个额外的约束 `limit`，它决定缓存结果能否使用。

使用某个 `(typed, source)` 对调用 `memo_diff` 时，它不仅会检查该对是否出现过，还会检查当前的 `limit` 是否小于或等于缓存的 `limit`。这是 `memo` 不会执行的额外检查。

为什么这样处理 `limit`？

`limit` 表示差异函数关心的最大差异，也就是说，超过 `limit` 的差异可以被视为相同。因此，当差异低于 `limit` 时，差异函数会提供准确的差异值；当差异高于 `limit` 时，返回的值可能不准确。

所以，如果某个缓存差异值是使用较高的 `limit` 计算出来的，就可以信任它；但如果是使用较低的 `limit` 计算出来的，则不能信任。

例如，下面第一次调用的结果可以用于预测第二次调用的结果，因为较高的 `limit` 提供了更多信息。但第二次调用的结果不能用于预测第一次调用。

```python
>>> minimum_mewtations("hello", "hasldfasdfsffsfasdf", 100)
17
>>> minimum_mewtations("hello", "hasldfasdfsffsfasdf", 2)
3
```

实现 `memo_diff` 后，最后完成以下操作：

- 使用 `memo` 装饰 `autocorrect`。
- 使用 `memo_diff` 装饰 `minimum_mewtations`。

现在运行 `autocorrect` 和 `minimum_mewtations` 应该会快得多！

**注意：** 如果未通过涉及 `call_count` 的自动评分测试，很可能是问题 7 中的 `minimum_mewtations` 实现没有使用尽可能严格的基本情况，仍需优化。

问题 7 的测试并不十分严格，因此即使已经通过问题 7，基本情况仍可能不够严格。请确保没有进行不必要的递归调用。这里对此要求严格，是因为尽可能严格的基本情况对于代码效率至关重要。

**重要：** 请先自己尝试！只有在某个测试用例上卡住较长时间后，再查看下面的常见错误部分，否则可能无法从项目中学到同样多的内容。

### 常见错误

考虑以下情况：

```python
minimum_mewtations(typed="maooo", source="mao", limit=0)
```

由于不允许进行任何转换，而两个单词又不相同，函数能多快确定结果不可能满足限制？

再考虑：

```python
minimum_mewtations(
    typed="habc",
    source="hmao",
    limit=some_limit_greater_than_zero
)
```

两个字符串都以字符 `h` 开头。在这种情况下，最有效的方法是什么？函数是否还应该尝试：

- “添加”操作，得到 `habc` 和 `mao`？
- “删除”操作，得到 `abc` 和 `hmao`？

你的实现是否利用了这一优化？

**注意：** 自动评分器需要一些运行时间，但不应超过 10 秒。

```bash
python3 -m pytest -k qEC --unlock
```

解锁示例：

```python
>>> from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file
>>> all_words = lines_from_file("data/words.txt")
>>> common_words = lines_from_file("data/common_words.txt")
>>> def my_decorator(func):
...     def wrapper():
...         print("Say Hello")
...         func()
...         print("Say Goodbye")
...     return wrapper
>>> @my_decorator
... def say_hello():
...     print("Hello World")
>>> say_hello()
______
______
______
>>> def magic_decorator(func):
...     def wrapper(x):
...         return func(x * 2)
...     return wrapper
>>> @magic_decorator
... def myfunc(x):
...     return x * 3
>>> print(myfunc(4))
______
```

```bash
python3 -m pytest -k qEC
```