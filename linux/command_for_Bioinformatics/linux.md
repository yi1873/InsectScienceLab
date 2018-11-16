Linux commands
================
<xiang_zhi_@126.com>
November 16, 2018

Information
===========

-   学习生物信息，Linux是必须掌握的内容，其实常用的Linux命令也就30个左右，而且这些命令都是单词的简写，记忆起来并不困难。
-   命令不用死记，遇到使用的命令百度用法即可，如 linux gzip ...
-   Copied from [生信信息常用30个Linux命令系列](https://mp.weixin.qq.com/s/vaizJyXOdHK2_DA0utpiTA)
-   R markdown支持bash命令运行，linux命令可直接在Rmd运行

cd / ls
-------

-   cd：Change directory
-   ls：List files \*修改工作目录，cd和ls应该是使用最多的两个命令。

``` bash
cd data  # 进入到data目录
ls -l    # 查看data目录下的文件(-l列出详细信息)
```

    ## total 16
    ## -rw-r--r--  1 lxz  staff    78 Nov 16 14:17 id.list
    ## -rw-r--r--  1 lxz  staff  2688 Nov 16 11:12 test.fa

``` bash
cd ../   # 返回上一级目录
ls       # 查看目录
```

    ## command_for_Bioinformatics
    ## fastq2fasta

pwd
---

-   pwd: print working directory

``` bash
pwd   # 显示当前工作目录
```

    ## /Users/lxz/Desktop/github/InsectScienceLab/linux/command_for_Bioinformatics

cp
--

-   cp: Copy file

``` bash
cp data/test.fa data/test.v2.fa   # 将test.fa复制为test.v2.fa
ls data   # 查看data下的文件
```

    ## id.list
    ## test.fa
    ## test.v2.fa

mv
--

-   mv: Move file 移动文件，相当于windows下的剪切粘贴，如果剪切粘贴到同一目录下，则为重命名。

``` bash
mv data/test.v2.fa data/test.v3.fa  # 重命名为test.v3.fa
ls data
```

    ## id.list
    ## test.fa
    ## test.v3.fa

rm
--

-   rm: Remove file 删除文件

``` bash
rm data/test.v3.fa  #删除data目录下test.v3.fa
ls data  # 查看data下的文件
```

    ## id.list
    ## test.fa

ln
--

-   ln: Link files 创建连接文件

``` bash
ln -s data/test.fa data/fasta.fa    # 在data目录下创建一个快捷方式
ls  data
```

    ## fasta.fa
    ## id.list
    ## test.fa

``` bash
rm data/fasta.fa    # 删除data目录的fasta.fa软链接 
```

mkdir
-----

-   mkdir：Make directory 创建文件夹

``` bash
mkdir -p data/rnaseq # 在data目录创建一个名为rnaseq的目录 
ls data
```

    ## id.list
    ## rnaseq
    ## test.fa

split
-----

-   split 文件分割

``` bash
split -l 2 data/id.list data/id.   # 对id.list按每个文件两行进行切份，以'data/id.'为输出前缀, 'data/'代表路径
ls data/id.*  # 查看切份文件
```

    ## data/id.aa
    ## data/id.ab
    ## data/id.ac
    ## data/id.list

cat
---

-   cat: concatenate 连接
-   cat的一个作用是查看文件，一般是比较小的文件，行数小于一个屏幕，最多不要超过两个屏幕，否则会刷屏；
-   cat另一个作用是合并多个文件，一般配合重定向合并为一个新文件或者将一个文件内容追加到另一个文件结尾。

``` bash
cat data/id.aa data/id.ab data/id.ac > data/all.id  # 将多个文件合并
cat data/all.id   # 打id.list文件打印至屏幕
rm -f data/id.a* data/all.id
```

    ## M37699.gene3
    ## AY528718.1.gene4
    ## AF091113.2.gene6
    ## M63556.1.gene9
    ## M63556.1.gene10

less
----

-   less 查看文件，按q退出

``` bash
less data/id.list  # 查看文件
```

    ## M37699.gene3
    ## AY528718.1.gene4
    ## AF091113.2.gene6
    ## M63556.1.gene9
    ## M63556.1.gene10

more
----

-   more也是查看工具

``` bash
more data/id.list
```

    ## M37699.gene3
    ## AY528718.1.gene4
    ## AF091113.2.gene6
    ## M63556.1.gene9
    ## M63556.1.gene10

wc
--

-   wc为计数工具

``` bash
wc data/id.list  # 对id.list进行计数
```

    ##        5       5      78 data/id.list

``` bash
less data/id.list | wc -l    # wc -l只统计行数; '|'为管道符，使用频率非常高，可理解为next；
```

    ##        5

grep
----

-   grep对fasta文件计数

``` bash
less data/test.fa | grep '>' | wc -l  # fasta格式以'>'开头，只需提取'>'计数即可
```

    ##        5

-   grep为提取特征值

``` bash
less data/id.list | grep 'gene4' # 提取含'gene4'字符的行； '|'管道符在后面命令中会经常用到
```

    ## AY528718.1.gene4

``` bash
less data/id.list | grep -v 'gene4'  # 提取不含'gene4'行
```

    ## M37699.gene3
    ## AF091113.2.gene6
    ## M63556.1.gene9
    ## M63556.1.gene10

``` bash
less data/id.list | grep -v 'gene4' | wc -l  # 先提取不含'gene4'行，再计数；使用两次管道符
```

    ##        4

``` bash
less data/id.list | egrep  'gene4|gene6'  # 提取含'gene4'或'gene6'行
```

    ## AY528718.1.gene4
    ## AF091113.2.gene6

sed
---

-   字符替换工具

``` bash
less data/id.list | sed 's/gene/GENE/'   # 将'gene'替换为'GENE'
```

    ## M37699.GENE3
    ## AY528718.1.GENE4
    ## AF091113.2.GENE6
    ## M63556.1.GENE9
    ## M63556.1.GENE10

g(un)zip
--------

-   gzip是文件压缩工具，默认直接对源文件进行处理

``` bash
gzip data/test.fa   # 压缩data目录下的test.fa文件，原文件不保留
ls data  # test.fa文件已被压缩
```

    ## id.list
    ## rnaseq
    ## test.fa.gz

``` bash
gunzip data/test.fa.gz  # 解压data目录下的压缩文件，原文件不保留
ls data  # test.fa.gz已被解压
```

    ## id.list
    ## rnaseq
    ## test.fa

``` bash
gzip -c data/test.fa > data/test.fa.gz  # 将data目录下的test.fa压缩为fasta.fa.gz,同时保留原文件
ls data  # test.fa.gz 与 test.fa同在
rm data/test.fa.gz
```

    ## id.list
    ## rnaseq
    ## test.fa
    ## test.fa.gz

tar
---

-   tar同样是文件压缩工具

``` bash
tar -zcvf data/fasta.tar.gz data/test.fa # tar压缩文件
ls data
```

    ## tar: Failed to set default locale
    ## a data/test.fa
    ## fasta.tar.gz
    ## id.list
    ## rnaseq
    ## test.fa

``` bash
tar -zxvf data/fasta.tar.gz  # tar解压文件
rm -f data/fasta.tar.gz
```

    ## tar: Failed to set default locale
    ## x data/test.fa
