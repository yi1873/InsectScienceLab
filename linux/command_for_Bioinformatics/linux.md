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

    ## total 24
    ## -rw-r--r--  1 lxz  staff    62 Nov 16 11:12 example.sh
    ## -rw-r--r--  1 lxz  staff  1034 Nov 16 13:26 fasta.tar.gz
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
    ## fasta.tar.gz
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
    ## fasta.tar.gz
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
    ## fasta.tar.gz
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
    ## fasta.tar.gz
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
    ## fasta.tar.gz
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
    ## fasta.tar.gz
    ## rnaseq
    ## test.fa.gz

``` bash
gunzip data/test.fa.gz  # 解压data目录下的压缩文件，原文件不保留
ls data  # test.fa.gz已被解压
```

    ## example.sh
    ## fasta.tar.gz
    ## rnaseq
    ## test.fa

``` bash
gzip -c data/fasta.fa.gz  data/test.fa  # 将data目录下的test.fa压缩为fasta.fa.gz,同时保留原文件
ls data  # fasta.fa.gz 与 test.fa同在
```

    ## gzip: can't stat: data/fasta.fa.gz (data/fasta.fa.gz): No such file or directory
    ## <8b><84>5<ee>[
    ## <a4>4<e6><d8><eb><8d><bc><8f>bK<8f><b1><dd>-[%N<<e6>Zf<cb><9c>(<85><82>!<a1><9e>F/PM<f4><e2>R<f4><83>k1<ad>uZP<e3>X<f4><d2><8d><ce><c6>e'Oo<f1><eb><f6><fc><fa>ry=_<90><c6><8f>/<a5>!<8b><de><b4>#<92><a9>
    ## <b8><aa>M5W<ab><d3>g<aa>S)<d8><8e><81><b1><8c>%w<d2>T<92><b1>Rb<b3>LbUcn<c2><e7><e1><f3>[sK6<c3><d0>e<bf><94>z<a2><e7>$<8a><93>i\CT<a3>'3<b4>QHX<b8><b6>#<d4><9d>
    ## q<dd>XN<84><85>I|<89><ee><b4>O<86>\    ]L<d1>^<e3><b4><a8><a4>lx.<90>u<ed><fd><96>9a<88>Ka3<b0><da>@-D8K<a7>w<80><b9><f2><86>U<84><f5><f6>
    <b6><9c><a0>XP,$DQK?<9f><97><cb><e5>z~F<f7>o<bb>9P<bd><91><96>s<9b>N4gDi<8f>\<f1>\<e9><e2><ae><c9><e4>:gH<ab><9d>QH&<af>]<a2>"<d5><bb><a2><a5>KS<be>pbz8r=<e0>XYG<eb><8c>-a<ed><9d><98><90><de>@<83>1W><d1>A<8a><a6>/<e9>(<b2>6M<cd><89>M<ed><ca>/6<89>Q<bb>{<8e>Z<a8><8b>$<e5><93><98>p<e5><be>y<a8>CYPe<9b>yh<91>7K<d1><bd><8d><ba><da>-T<c0><a2><dc>J<f5><b0><bd><8e><b4><84>SWE<bb>I7<b5><b4><96><9b><fd><ee>D<da><c4><f6><d3><db><fb><fd>z<bb><dd><a7>g<<be><c1><84><d3><e7>{<e7><ce>S<85><c2>'<d0><a4>y<9b>rb<9a>    <91>b<cb><b3><a7>(<d0><b1><d5><f4>A7O<80>rBIA<8d><91><b2><cc>=j\G<bf><c2>
    ## m<a1><9e><99>@<cf>T0<9d><f2>(#O<b5><e0><b4><a6><80><e5><a1><f6><c3><b4><a2>3I)5FG<ba><87>)<80><a9><c0>I<ae>5<da>;4<c2><ac><b4><c9>MbR<97><e8><d5><99>q<c0><f8><d8><ae><9a>i<<97><cd><d4><81>S<92>9<8d>l<99>6<ce><<b5>'<ed>$<ad>nC<b1>6L<b2><c2><88><84>qy<fa>n<9a>L<d5><97>k.<q<cd>#<bd><98><c6><e8><96><e1>Md<bd><87><8f><cf>A<e9>4<z<98><c1><9e><a9><e0><d6>:<df>!G<c9><99><f3>o<8d>0<b0>tO?<fd>  <c4><a4><b4>e<89><ba><da>g<ec>{T<8d><82><89><93><ee>-<fe><f2><d8>nN(<db><d1><97>?<a0>f~[r<ee>H<e9><c2><fc>O<aa><e8><f4>\<ce><80>
    ## 
    ## fasta.tar.gz
    ## rnaseq
    ## test.fa

tar
---

``` bash
tar -zcvf data/fasta.tar.gz data/test.fa # tar压缩文件
ls data
tar -zxvf data/fasta.tar.gz  # tar解压文件
```

    ## tar: Failed to set default locale
    ## a data/test.fa
    ## example.sh
    ## fasta.tar.gz
    ## rnaseq
    ## test.fa
    ## tar: Failed to set default locale
    ## x data/test.fa
