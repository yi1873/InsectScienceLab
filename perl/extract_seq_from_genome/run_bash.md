提取序列/tab信息
================
November 15, 2018

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

    ## perl: warning: Setting locale failed.
    ## perl: warning: Please check that your locale settings:
    ##  LC_ALL = (unset),
    ##  LC_CTYPE = "en_CN.UTF-8",
    ##  LANG = "en_CN.UTF-8"
    ##     are supported and installed on your system.
    ## perl: warning: Falling back to the standard locale ("C").

-   在该目录下会生成结果test.out.fa
-   perl warning 为设置环境变量问题，可忽略；下同

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

R markdown支持perl脚本运行
==========================

-   根据id提取序列

``` perl
#!/usr/bin/perl -w
use strict;

open IN1,"id.list"||die;
open IN2,"genome.fa"||die;
open OUT,">test.out.v2.fa"||die;

my %hash;
while(<IN1>){
    chomp;
    $hash{$_}=$_;
}

$/=">"; # 设置以">"符号为分割符
while(<IN2>){
      next unless (my ($id,$seq) = /(.*?)\n(.*)/s);
      my $id2=(split(/\s/,$id))[0];
      $seq =~ s/[\d\s>]//g;
      if(exists $hash{$id2}){
            print OUT ">$id2\n$seq\n";
      }
}
$/="\n";

close IN1;
close IN2;
close OUT;
```

    ## perl: warning: Setting locale failed.
    ## perl: warning: Please check that your locale settings:
    ##  LC_ALL = (unset),
    ##  LC_CTYPE = "en_CN.UTF-8",
    ##  LANG = "en_CN.UTF-8"
    ##     are supported and installed on your system.
    ## perl: warning: Falling back to the standard locale ("C").

-   根据id按行提取tab格式信息

``` perl
#!/usr/bin/perl -w
use strict;

open IN1,"../extract_tab_from_tableinfo/id.list"||die;
open IN2,"../extract_tab_from_tableinfo/species_taxonomy.txt"||die;
open OUT,">../extract_tab_from_tableinfo/test.out.v2.txt"||die;

my %hash;
while(<IN1>){
    chomp;
    $hash{$_}=$_;
}

while(<IN2>){
    chomp;
    my @info=split(/\t/);
    if(exists $hash{$info[0]}){
        print OUT "$_\n";
    }else{
        next;
    }
}

close IN1;
close IN2;
close OUT;
```

    ## perl: warning: Setting locale failed.
    ## perl: warning: Please check that your locale settings:
    ##  LC_ALL = (unset),
    ##  LC_CTYPE = "en_CN.UTF-8",
    ##  LANG = "en_CN.UTF-8"
    ##     are supported and installed on your system.
    ## perl: warning: Falling back to the standard locale ("C").
