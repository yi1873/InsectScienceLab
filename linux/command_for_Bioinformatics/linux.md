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
    ## -rw-r--r--  1 lxz  staff    62 Nov 16 11:12 example.sh
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

    ## example.sh
    ## test.fa
    ## test.v2.fa

mv
--

-   mv: Move file 移动文件，相当于windows下的剪切粘贴，如果剪切粘贴到同一目录下，则为重命名。

``` bash
mv data/test.v2.fa data/test.v3.fa  # 重命名为test.v3.fa
ls data
```

    ## example.sh
    ## test.fa
    ## test.v3.fa

rm
--

-   rm: Remove file 删除文件

``` bash
rm data/test.v3.fa  #删除data目录下test.v3.fa
ls data  # 查看data下的文件
```

    ## example.sh
    ## test.fa

ln
--

-   ln: Link files 创建连接文件

``` bash
ln -s data/test.fa data/fasta.fa    # 在data目录下创建一个快捷方式
ls  data
```

    ## example.sh
    ## fasta.fa
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

    ## example.sh
    ## rnaseq
    ## test.fa

g(un)zip
--------

-   gzip是文件压缩工具，默认直接对源文件进行处理

``` bash
gzip data/test.fa   # 压缩data目录下的test.fa文件，原文件不保留
ls data  # test.fa文件已被压缩
```

    ## example.sh
    ## rnaseq
    ## test.fa.gz

``` bash
gunzip data/test.fa.gz  # 解压data目录下的压缩文件，原文件不保留
ls data  # test.fa.gz已被解压
```

    ## example.sh
    ## rnaseq
    ## test.fa

``` bash
gzip -c data/test.fa > data/test.fa.gz  # 将data目录下的test.fa压缩为fasta.fa.gz,同时保留原文件
ls data  # test.fa.gz 与 test.fa同在
```

    ## example.sh
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
    ## example.sh
    ## fasta.tar.gz
    ## rnaseq
    ## test.fa
    ## test.fa.gz

``` bash
tar -zxvf data/fasta.tar.gz  # tar解压文件
```

    ## tar: Failed to set default locale
    ## x data/test.fa
