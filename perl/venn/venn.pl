#!/usr/bin/perl -w
use strict;
use Getopt::Long;
use Pod::Usage;

my ($help);
my $title = "";

GetOptions(
	'help'=>\$help,
	'title:s'=>\$title,
);

pod2usage 1 if($help or @ARGV < 2 or @ARGV > 7);

my %venn;
my %lab;
my $count = 0;
for my $name(@ARGV){
	open FL,"$name" or die "Cannot open file: $name\n";
	my @fam = <FL>;
	close FL;
	chomp @fam;
	my %fam;
	for(@fam){
		next if(/^\s*$/);
		$fam{$_} = 1;
	}
	for(keys %fam){
		$venn{$_} += 2**$count;
	}
	$name = `basename $name`;
	chomp $name;
	$name =~ s/.txt//;
	$lab{2**$count} = $name;
	$count ++;
}

my %count;
for(keys %venn){
	$count{$venn{$_}} ++;
}

open FL,"./venn$count.svg";
while(<FL>){
	if(/>(\d+)<\/text>/){
		my $num = defined $count{ $1 } ? $count{ $1 } : 0;
		s/>(\d+)<\/text>/>$num<\/text>/;
	}elsif(/>([A-Z])<\/text>/){
		my $flag = 2 ** (ord($1) - ord("A"));
		my $lab = defined $lab{$flag} ? $lab{$flag} : "undef";
		s/>[A-Z]<\/text>/>$lab<\/text>/;
	}else{
		s/>Title<\/text>/>$title<\/text>/;
	}
	print;
}
close FL;

=head1 NAME

=head1 SYNOPSIS

 perl venn.pl --title "test title" xxx1.txt  xxx2.txt xxx3.txt > test.svg
 perl venn.pl --title "test title" dataset/*.txt > test.svg


=head1 OPTIONS

 --help        help
 --title       title for graph

=cut

