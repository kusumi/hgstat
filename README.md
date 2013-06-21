hgstat
======

## Usage

### commitmonth.py

    [root@localhost hgstat]# ./commitmonth.py -h
    Usage: commitmonth.py [options]

    Options:
      -h, --help            show this help message and exit
      --after=YYYY-MM(-DD)  
      --before=YYYY-MM(-DD)
      --sort                

### commithour.py

    [root@localhost hgstat]# ./commithour.py -h
    Usage: commithour.py [options]

    Options:
      -h, --help            show this help message and exit
      --after=YYYY-MM(-DD)  
      --before=YYYY-MM(-DD)
      --sort                

### commitday.py

    [root@localhost hgstat]# ./commitday.py -h
    Usage: commitday.py [options]

    Options:
      -h, --help            show this help message and exit
      --after=YYYY-MM(-DD)  
      --before=YYYY-MM(-DD)
      --sort                

### annotatemonth.py

    [root@localhost hgstat]# ./annotatemonth.py -h
    Usage: annotatemonth.py [options]

    Options:
      -h, --help            show this help message and exit
      --after=YYYY-MM(-DD)  
      --before=YYYY-MM(-DD)
      --sort                

## Examples

### commitmonth.py

    [root@localhost hg-stable]# /tmp/hgstat/commitmonth.py
    2005-05   208  1.1[%]
    2005-06   341  1.8[%]
    2005-07   271  1.4[%]
    2005-08   363  1.9[%]
    2005-09   186  1.0[%]
    2005-10   117  0.6[%]
    2005-11    77  0.4[%]
    2005-12    48  0.3[%]

    2006-01    65  0.3[%]
    2006-02   163  0.9[%]
    2006-03   193  1.0[%]
    2006-04   138  0.7[%]
    2006-05   206  1.1[%]
    2006-06   182  0.9[%]
    2006-07   199  1.0[%]
    2006-08   292  1.5[%]
    2006-09   171  0.9[%]
    2006-10   388  2.0[%]
    2006-11   132  0.7[%]
    2006-12   279  1.5[%]

    2007-01    53  0.3[%]
    2007-02    67  0.3[%]
    2007-03   172  0.9[%]
    2007-04    88  0.5[%]
    2007-05    89  0.5[%]
    2007-06   265  1.4[%]
    2007-07   294  1.5[%]
    2007-08   237  1.2[%]
    2007-09    79  0.4[%]
    2007-10   134  0.7[%]
    2007-11    80  0.4[%]
    2007-12   217  1.1[%]

    2008-01   196  1.0[%]
    2008-02   215  1.1[%]
    2008-03   236  1.2[%]
    2008-04   133  0.7[%]
    2008-05    69  0.4[%]
    2008-06   144  0.8[%]
    2008-07    77  0.4[%]
    2008-08   111  0.6[%]
    2008-09    91  0.5[%]
    2008-10   234  1.2[%]
    2008-11   152  0.8[%]
    2008-12   111  0.6[%]

    2009-01   176  0.9[%]
    2009-02    81  0.4[%]
    2009-03   132  0.7[%]
    2009-04   333  1.7[%]
    2009-05   418  2.2[%]
    2009-06   307  1.6[%]
    2009-07   292  1.5[%]
    2009-08   132  0.7[%]
    2009-09   106  0.6[%]
    2009-10   175  0.9[%]
    2009-11   268  1.4[%]
    2009-12   205  1.1[%]

    2010-01   129  0.7[%]
    2010-02   252  1.3[%]
    2010-03   241  1.3[%]
    2010-04   263  1.4[%]
    2010-05   188  1.0[%]
    2010-06   228  1.2[%]
    2010-07   248  1.3[%]
    2010-08   444  2.3[%]
    2010-09   428  2.2[%]
    2010-10   300  1.6[%]
    2010-11   168  0.9[%]
    2010-12   162  0.8[%]

    2011-01   107  0.6[%]
    2011-02   181  0.9[%]
    2011-03   326  1.7[%]
    2011-04   286  1.5[%]
    2011-05   371  1.9[%]
    2011-06   319  1.7[%]
    2011-07   177  0.9[%]
    2011-08    75  0.4[%]
    2011-09   110  0.6[%]
    2011-10   215  1.1[%]
    2011-11   196  1.0[%]
    2011-12   162  0.8[%]

    2012-01   291  1.5[%]
    2012-02   151  0.8[%]
    2012-03   131  0.7[%]
    2012-04   229  1.2[%]
    2012-05   271  1.4[%]
    2012-06   268  1.4[%]
    2012-07   222  1.2[%]
    2012-08   208  1.1[%]
    2012-09   179  0.9[%]
    2012-10   217  1.1[%]
    2012-11   109  0.6[%]
    2012-12   202  1.1[%]

    2013-01   300  1.6[%]
    2013-02   242  1.3[%]
    2013-03   101  0.5[%]
    2013-04   221  1.2[%]
    2013-05    51  0.3[%]
    2013-06     7  0.0[%]
    2013-07     0  0.0[%]
    2013-08     2  0.0[%]
    ----------------------------------------
            19166

### commithour.py

    [root@localhost hg-stable]# /tmp/hgstat/commithour.py
     0 AM   775  4.0[%]
     1 AM   609  3.2[%]
     2 AM   371  1.9[%]
     3 AM   219  1.1[%]
     4 AM    95  0.5[%]
     5 AM    78  0.4[%]
     6 AM    70  0.4[%]
     7 AM   153  0.8[%]
     8 AM   351  1.8[%]
     9 AM   586  3.1[%]
    10 AM   877  4.6[%]
    11 AM  1074  5.6[%]
     0 PM  1025  5.3[%]
     1 PM  1366  7.1[%]
     2 PM  1284  6.7[%]
     3 PM  1451  7.6[%]
     4 PM  1425  7.4[%]
     5 PM  1387  7.2[%]
     6 PM  1093  5.7[%]
     7 PM  1039  5.4[%]
     8 PM   833  4.3[%]
     9 PM   888  4.6[%]
    10 PM  1055  5.5[%]
    11 PM  1062  5.5[%]
    ----------------------------------------
          19166

### commitday.py

    [root@localhost hg-stable]# /tmp/hgstat/commitday.py
    Mon  2941 15.3[%]
    Tue  2895 15.1[%]
    Wed  2975 15.5[%]
    Thu  2877 15.0[%]
    Fri  2932 15.3[%]
    Sat  2210 11.5[%]
    Sun  2336 12.2[%]
    ----------------------------------------
        19166

### annotatemonth.py

    [root@localhost hg-stable]# /tmp/hgstat/annotatemonth.py
    2005-05     366  0.1[%]
    2005-06    1635  0.4[%]
    2005-07     353  0.1[%]
    2005-08    2082  0.5[%]
    2005-09    3065  0.7[%]
    2005-10     477  0.1[%]
    2005-11     120  0.0[%]
    2005-12     319  0.1[%]

    2006-01     114  0.0[%]
    2006-02     845  0.2[%]
    2006-03     268  0.1[%]
    2006-04     595  0.1[%]
    2006-05    1163  0.3[%]
    2006-06    1109  0.2[%]
    2006-07    2048  0.5[%]
    2006-08    1541  0.3[%]
    2006-09     460  0.1[%]
    2006-10    1928  0.4[%]
    2006-11     811  0.2[%]
    2006-12     732  0.2[%]

    2007-01     120  0.0[%]
    2007-02     139  0.0[%]
    2007-03     388  0.1[%]
    2007-04     982  0.2[%]
    2007-05     480  0.1[%]
    2007-06     762  0.2[%]
    2007-07    2131  0.5[%]
    2007-08     845  0.2[%]
    2007-09     188  0.0[%]
    2007-10     853  0.2[%]
    2007-11     539  0.1[%]
    2007-12     955  0.2[%]

    2008-01     929  0.2[%]
    2008-02    1064  0.2[%]
    2008-03    2490  0.6[%]
    2008-04     452  0.1[%]
    2008-05      82  0.0[%]
    2008-06    1369  0.3[%]
    2008-07     379  0.1[%]
    2008-08     656  0.1[%]
    2008-09     665  0.1[%]
    2008-10    3875  0.9[%]
    2008-11    2131  0.5[%]
    2008-12    1825  0.4[%]

    2009-01    6295  1.4[%]
    2009-02    2108  0.5[%]
    2009-03    1411  0.3[%]
    2009-04    2746  0.6[%]
    2009-05    9249  2.0[%]
    2009-06    7613  1.7[%]
    2009-07    1927  0.4[%]
    2009-08    3450  0.8[%]
    2009-09    1932  0.4[%]
    2009-10   11839  2.6[%]
    2009-11    8351  1.8[%]
    2009-12    2145  0.5[%]

    2010-01    2674  0.6[%]
    2010-02    2986  0.7[%]
    2010-03     968  0.2[%]
    2010-04    1831  0.4[%]
    2010-05    1540  0.3[%]
    2010-06   35666  7.9[%]
    2010-07    1532  0.3[%]
    2010-08   37602  8.3[%]
    2010-09   38943  8.6[%]
    2010-10   14999  3.3[%]
    2010-11    3668  0.8[%]
    2010-12    1891  0.4[%]

    2011-01    1106  0.2[%]
    2011-02   15351  3.4[%]
    2011-03    8416  1.9[%]
    2011-04    5608  1.2[%]
    2011-05   19118  4.2[%]
    2011-06   30798  6.8[%]
    2011-07    1853  0.4[%]
    2011-08    1079  0.2[%]
    2011-09    3479  0.8[%]
    2011-10    8253  1.8[%]
    2011-11   10548  2.3[%]
    2011-12   12793  2.8[%]

    2012-01    9676  2.1[%]
    2012-02    3063  0.7[%]
    2012-03    3505  0.8[%]
    2012-04    7895  1.7[%]
    2012-05    6177  1.4[%]
    2012-06    8263  1.8[%]
    2012-07    9653  2.1[%]
    2012-08    4841  1.1[%]
    2012-09    4739  1.0[%]
    2012-10    3752  0.8[%]
    2012-11    1540  0.3[%]
    2012-12    3863  0.9[%]

    2013-01    4852  1.1[%]
    2013-02    4964  1.1[%]
    2013-03    1681  0.4[%]
    2013-04    4656  1.0[%]
    2013-05    3155  0.7[%]
    2013-06      79  0.0[%]
    2013-07       0  0.0[%]
    2013-08       2  0.0[%]
    ----------------------------------------
             452454 lines from 10659 changesets
