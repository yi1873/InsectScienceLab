# InsectScienceLab
* 植保所昆功组生信入门培训专用
* 包含linux/perl/R画图/常用生信软件/生信通识课等
* 从 **入门** 到 **放弃** 系列
* http://www.allitebooks.com/ 下载相关书籍
* 不定期持续更新

# 编程基础入门
## Linux
* 必学项，须熟练操作服务器，记住常用的几个命令即可，
* [生信常用到的linux命令](https://github.com/yi1873/InsectScienceLab/blob/master/linux/command_for_Bioinformatics/linux.md)
* [fastq2fasta awk实现](https://github.com/yi1873/InsectScienceLab/blob/master/linux/fastq2fasta/example.sh)

## perl/python scripts
*  脚本语言编程，建议学python; 脚本语言可先学会使用，再慢慢看代码学习;
* select.pl
  [根据id提取序列信息](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_seq_from_genome/example.sh) / 
  [根据id提取表格信息](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_tab_from_tableinfo/example.sh)

  [又get一项新技能, R markdown可直接运行bash/perl](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_seq_from_genome/run_bash.md)
* [合并多个表格结果](https://github.com/yi1873/InsectScienceLab/blob/master/perl/merge_single_tab/example.sh)
* [venn绘图](https://github.com/yi1873/InsectScienceLab/blob/master/perl/venn/example.sh)
* [split_fasta.py](https://github.com/yi1873/InsectScienceLab/blob/master/python/split_fasta/example.sh): 将fasta格式文件切成多份，在blast比对时可将文件切成多份同时比对，可加快比对速度;
* [JGI网站爬虫](https://github.com/yi1873/InsectScienceLab/blob/master/python/extractJGI_taxon/extractJGI_taxon.md)

## R scripts
* R必学，画图非常方便，先从画图入手学；再慢慢提升到数据处理；
* Books
  [R for data science](https://github.com/yi1873/InsectScienceLab/tree/master/R/books)
* [heatmap](https://github.com/yi1873/InsectScienceLab/blob/master/R/heatmap/heatmap.md)
* [Pearson correlation between samples](https://github.com/yi1873/InsectScienceLab/blob/master/R/correlation_plot/pearson_corr_plot.md) 

# 生信通识课
* 多为网络资源汇总，拓宽知识面
## 测序原理
* 主要理解二代Illumina测序原理，重点理解**边合成边测序**与**桥式PCR**；
* Illumina/Solexa Genome Analyzer测序的基本原理是边合成边测序。在Sanger等测序方法的基础上，通过技术创新，用不同颜色的荧光标记四种不同的dNTP，当DNA聚合酶合成互补链时，每添加一种dNTP就会释放出不同的荧光，根据捕捉的荧光信号并经过特定的计算机软件处理，从而获得待测DNA的序列信息；
* 测序过程：
  1. DNA待测文库构建。 超声波把DNA打断成小片段，一般200--500bp，两端加上不同的接头
  2. Flowcell。一个flowcell，8个channel，很多接头
  3. 桥式PCR扩增。每个DNA片段将在各自位置集中成束，每一束含有单个DNA模板的很多拷贝，目的：将碱基的信号强度放大，达到测序所需的信号要求。
  4. 测序。边合成边测序。反应所需材料，dNTP的3’端特殊处理，不能继续反应，因此每次只能添加一个碱基，另外每个碱基有一种颜色。dNTP添加到链上后，所有未使用游离dNTP和DNA聚合酶会被洗脱掉。接着，再加入激发荧光所需的缓冲液，用激光激发荧光信号，并有光学设备完成荧光信号的记录，最后利用计算机分析将光学信号转化为测序碱基。这样荧光信号记录完成后，再加入化学试剂淬灭荧光信号并去除dNTP 3’-OH保护基团，以便能进行下一轮的测序反应
* [动画演示](http://v.youku.com/v_show/id_XNzEzNzk1NTA0.html) / [知乎](https://zhuanlan.zhihu.com/p/20702684)
## 生信基本知识和概念

## 常用数据库

## 常用生信软件 

## 生信操作

# 进阶

## 机器学习
* [Machine Learning](https://github.com/yi1873/machine_learning) 
* Books 
  [Maching learning with R](https://github.com/yi1873/machine_learning/blob/master/Packt%20Machine%20Learning%20with%20R%202nd.Edition.pdf)

