提取序列/tab信息
================
November 14, 2018

select.pl
=========

-   该脚本为简单整合几项常用提取信息命令，如根据id提取序列；根据id按行提取tab格式信息等。
-   最近又get一项新技能，R markdown支持运行bash命令，更方便记录管理和运行bash命令行。
-   直接将该run\_bash.Rmd文件、id、序列文件/tab文件、perl脚本下载至同一目录，直接在Rstudio中点Knit运行即可 （mac系统自带perl，可直接运行； window系统估计需要安装perl，但未测试过）

根据id提取基因序列
------------------

``` bash
perl select.pl -cls fa -l id.list -s genome.fa -o test.out.fa
```

-   在该目录下会生成结果test.out.fa

根据id按行提取tab格式信息
-------------------------

-   “\\”反斜杠用于命令换行，主要是为了命令可读性，实际为一条命令

``` bash
perl select.pl -cls line -l ../extract_tab_from_tableinfo/id.list \
    -s ../extract_tab_from_tableinfo/species_taxonomy.txt  \
    -o ../extract_tab_from_tableinfo/test.out.txt
```

    ## perl: warning: Setting locale failed.
    ## perl: warning: Please check that your locale settings:
    ##  LC_ALL = (unset),
    ##  LC_CTYPE = "en_CN.UTF-8",
    ##  LANG = "en_CN.UTF-8"
    ##     are supported and installed on your system.
    ## perl: warning: Falling back to the standard locale ("C").

-   在extract\_tab\_from\_tableinfo目录下会生成结果test.out.txt
