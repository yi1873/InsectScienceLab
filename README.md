# InsectScienceLab
* 植保所昆功组生信入门培训专用
* 包含linux/perl/R画图/常用生信软件/生信通识课等
* 从 **入门** 到 **放弃** 系列
* http://www.allitebooks.com/ 下载相关书籍
* 不定期持续更新

## 1.编程基础入门
## 1.1 Linux
* 必学项，须熟练操作服务器，记住常用的几个命令即可
* [生信常用到的linux命令](https://github.com/yi1873/InsectScienceLab/blob/master/linux/command_for_Bioinformatics/linux.md)
* [fastq2fasta awk实现](https://github.com/yi1873/InsectScienceLab/blob/master/linux/fastq2fasta/example.sh)

## 1.2 perl/python scripts
* 脚本语言编程，建议学python; 脚本语言可先学会使用，再慢慢看代码学习;
* select.pl
  [根据id提取序列信息](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_seq_from_genome/example.sh) / 
  [根据id提取表格信息](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_tab_from_tableinfo/example.sh)

  [又get一项新技能, R markdown可直接运行bash/perl](https://github.com/yi1873/InsectScienceLab/blob/master/perl/extract_seq_from_genome/run_bash.md)
* [合并多个表格结果](https://github.com/yi1873/InsectScienceLab/blob/master/perl/merge_single_tab/example.sh)
* [venn绘图](https://github.com/yi1873/InsectScienceLab/blob/master/perl/venn/example.sh)
* [split_fasta.py](https://github.com/yi1873/InsectScienceLab/blob/master/python/split_fasta/example.sh): 将fasta格式文件切成多份，在blast比对时可将文件切成多份同时比对，可加快比对速度;
* [JGI网站爬虫](https://github.com/yi1873/InsectScienceLab/blob/master/python/extractJGI_taxon/extractJGI_taxon.md)

## 1.3 R scripts
* R必学，画图非常方便，先从画图入手学；再慢慢提升到数据处理；
* Books
  [R for data science](https://github.com/yi1873/InsectScienceLab/tree/master/R/books)
* [heatmap](https://github.com/yi1873/InsectScienceLab/blob/master/R/heatmap/heatmap.md)
* [Pearson correlation between samples](https://github.com/yi1873/InsectScienceLab/blob/master/R/correlation_plot/pearson_corr_plot.md) 

## 2.生信通识课
* 多为网络资源汇总，拓宽知识面
## 2.1 测序原理
* 主要理解二代Illumina测序原理([动画演示](http://v.youku.com/v_show/id_XNzEzNzk1NTA0.html) / [知乎](https://zhuanlan.zhihu.com/p/20702684))，重点理解**边合成边测序**与**桥式PCR**；
* Illumina/Solexa Genome Analyzer测序的基本原理是**边合成边测序**。在Sanger等测序方法的基础上，通过技术创新，用不同颜色的荧光标记四种不同的dNTP，当DNA聚合酶合成互补链时，每添加一种dNTP就会释放出不同的荧光，根据捕捉的荧光信号并经过特定的计算机软件处理，从而获得待测DNA的序列信息；
```
  测序过程：
  1. DNA待测文库构建 超声波把DNA打断成小片段，一般200--500bp，两端加上不同的接头
  2. Flowcell      一个flowcell，8个channel，很多接头
  3. 桥式PCR扩增    每个DNA片段将在各自位置集中成束，每一束含有单个DNA模板的很多拷贝，目的：将碱基的信号强度放大，达到测序所需的信号要求。 
  4. 测序          边合成边测序。反应所需材料，dNTP的3’端特殊处理，不能继续反应，因此每次只能添加一个碱基，另外每个碱基有一种颜色。dNTP添加到链上后，所有未使用游离dNTP和DNA聚合酶会被洗脱掉。再加入激发荧光所需的缓冲液，用激光激发荧光信号，并有光学设备完成荧光信号的记录，最后利用计算机分析将光学信号转化为测序碱基。
```
## 2.2 生信基本知识和概念
### 2.2.1 reads层面
* **reads**  
```
  指测序的结果，1条序列一般称为1条reads，一般为fastq格式；
```
* **fastq格式**  [示例](https://github.com/yi1873/InsectScienceLab/blob/master/linux/fastq2fasta/test.fastq)
```
  FASTQ是基于文本的保存生物序列和其测序质量信息的标准格式。其序列以及质量信息都是使用一个ASCII字符标示，最初由Sanger开发，目的是将FASTA序列与质量数据放到一起，目前已经成为高通量测序结果的标准。
  FASTQ文件中每个序列通常有四行：
    第一行是序列标识以及相关的描述信息，以‘@’开头；
    第二行是序列
    第三行以‘+’开头，后面是序列标示符、描述信息，或者什么也不加
    第四行是质量信息，和第二行的序列相对应，每一个序列都有一个质量评分，根据评分体系的不同，每个字符的含义表示的数字也不相同。
```
*  **Q20/Q30**  
```
  高通量测序中,每测一个碱基会给出一个相应的质量值,这个质量值是衡量测序准确度的. 
  碱基的质量值13,错误率为5%, 质量值20的错误率为1%, 质量值30的错误率为0.1%. 
  Q20与Q30则表示质量值大于等于20或30的碱基所占百分比.
  比如一共测了1G的数据量,其中有0.9G的碱基质量值大于或等于20,那么Q20则为90%. 
```
*  **k-mer**  
```
  将reads分成包含k个碱基的字符串，一般长短为m的reads可以分成m-k+1个k-mers.
```


### 2.2.2 基因组层面
* **fasta格式**  [示例](https://github.com/yi1873/InsectScienceLab/blob/master/linux/fastq2fasta/out.fa)
```
  fasta格式是最基本的表示序列信息（核苷酸或者蛋白质）的格式。
  fasta格式包含id和seq两部分:
    第一部分是序列的定义行，该行的开头是>符号，紧跟着后面的就是该条序列的名称；
    第二部分就是序列，所有的序列可以放在一行存储，也可以多行存储。
```
*  **Contig N50** 
```
   Reads拼接后会获得一些不同长度的Contigs.将所有的Contig长度相加,能获得一个Contig总长度.
   然后将所有的Contigs按照从长到短进行排序,如获得Contig 1,Contig 2,contig 3....
   将Contig按照这个顺序依次相加,当相加的长度达到Contig总长度的一半时,最后一个加上的Contig长度即为Contig N50.
 ```
    

## 2.3 常用数据库
### 2.3.1 nr/nt库
* nt (Nucleotide Sequence Database),核酸序列数据库
* nr (Non-Redundant Protein Sequence Database)非冗余蛋白库 
```
  完整的nr/nt 数据库和预先构建好的blast 索引可以从ncbi 的ftp 服务器上下载得到，地址：https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/
```

### 2.3.2 kegg库
* Kyoto Encyclopedia of Genes and Genomes [(KEGG)](https://www.kegg.jp/)是综合性功能数据库，最核心的为KEGG PATHWAY和KEGG ORTHOLOGY数据库。
* KEGG ORTHOLOGY数据库中将行使相同功能的基因聚在一起，称为 Ortholog Groups (KO entries);
* Blast/Diamond 作blastp比对，取最佳比对结果作KEGG功能注释；
* KEGG富集分析软件 KOBAS http://kobas.cbi.pku.edu.cn（可下载KEGG数据库）
```
  KEGG PATHWAY数据库中包含6类生物代谢通路，分别为:
      细胞过程（Cellular Processes）
      环境信息处理（Environmental Information Processing）
      遗传信息处理（Genetic Information Processing）
      人类疾病（Human Diseases）
      新陈代谢（Metabolism）
      生物体系统（Organismal Systems）
```
### 2.3.3 GO库
* Gene Ontology [(GO)](http://www.geneontology.org/), 是生物学功能注释的一个标准词汇表术语（GO term）;
* Blast/Diamond 作blastp比对，取最佳比对结果作GO功能注释；
```
  GO是生物学功能注释的一个标准词汇表术语（GO term），将基因的功能分为三部分：
      1）分子功能（Molecular Function)
      2）基因所处的细胞组分（Cellular Component）
      3）基因以及参与的生物学过程（Biological Process）
```

### 2.3.4 COG库
* Clusters of Orthologous Groups [(COG)](http://clovr.org/docs/clusters-of-orthologous-groups-cogs/)即同源蛋白簇，根据细菌、藻类和真核生物完整基因组的编码蛋白系统进化关系分类构建而成。
* Blast/Diamond 作blastp比对，取最佳比对结果作COG功能注释；

### 2.3.5 SwissProt
* [SwissProt](https://www.uniprot.org/uniprot/?query=reviewed:yes) 高质量的蛋白数据库，蛋白序列得到实验的验证；
* 下载链接 http://www.uniprot.org/downloads
* Blast/Diamond 作blastp比对，取最佳比对结果作SwissPort功能注释;

### 2.3.6 TrEMBL
* [TrEMBL](https://www.uniprot.org/uniprot/?query=reviewed:no)

### 2.3.7 Pfam
* Pfam
* [InterProScan](https://www.ebi.ac.uk/interpro/interproscan.html)作pfam注释;

## 2.4 常用生信软件 
### 2.4.1 质控软件 
* fastqc

### 2.4.2 比对软件
* blast
* diamond
* bwa
* kallisto
* kraken

### 2.4.3 进化分析软件
* **fasttree**


## 2.5 生信操作
### 转录组流程

### 基因组流程

### 宏基因组流程

## 2.6 组学文献阅读
* 各类组学文章千篇一律，多阅读几篇文献下来就能发现组学文章套路；
* [转录组文献示例](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115196/)/[基因组文献示例](https://www.cell.com/cell/fulltext/S0092-8674(11)01268-2?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867411012682%3Fshowall%3Dtrue)/[宏基因组文献示例](https://www.nature.com/articles/nature08821)
* 杂志订阅 https://feedly.com 


## 3.进阶
## 3.1 统计分析 

## 3.2 机器学习
* [Machine Learning](https://github.com/yi1873/machine_learning) 
* Books 
  [Maching learning with R](https://github.com/yi1873/machine_learning/blob/master/Packt%20Machine%20Learning%20with%20R%202nd.Edition.pdf)

