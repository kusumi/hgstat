#!/usr/bin/env python

if __name__ == '__main__':
    import calendar
    import re
    import sys
    import util

    test_date, sort = util.parse_option()
    d = {}
    c = []

    # e.g. 969b00db2418 Sat Mar 03 21:27:38 2012 +0900:
    r = re.compile(r"(\S+) [a-zA-Z]+ ([a-zA-Z]+) (\d+) \d+:\d+:\d+ (\d+) \S+:")
    months = dict([(x, i) for i, x in enumerate(calendar.month_abbr)])

    for f in util.popen_hg("manifest"):
        for x in util.popen_hg("annotate", "-cd", f):
            m = r.match(x)
            if m:
                l = m.groups()
                k = "%s-%02d-%02d" % (l[3], months[l[1]], int(l[2]))
                if test_date(k):
                    c.append(m.groups()[0])
                    k = k[:-3]
                    if k in d:
                        d[k] += 1
                    else:
                        d[k] = 1
    if not d:
        print("No data")
        sys.exit(1)

    done = []
    tot = sum(d.values())

    def fn(k):
        if k in d:
            v = d[k]
        else:
            v = 0
        if tot:
            p = 100.0 * v / tot
        else:
            p = 0
        print("%s %5d %4.1f[%%]" % (k, v, p))
        done.append(k)

    if sort:
        l = sorted([(v, k) for k, v in d.items()])
        g = reversed([x[1] for x in l])
        for k in g:
            fn(k)

    l = sorted(d.keys())
    begy, begm = [int(x) for x in l[0].split('-')]
    endy, endm = [int(x) for x in l[-1].split('-')]

    for y in range(begy, endy + 1):
        for m in range(begm if y == begy else 1, 13):
            k = "%d-%02d" % (y, m)
            if k not in done:
                fn(k)
            if y == endy and m == endm:
                break
        if not sort and not (y == endy and m == endm):
            print('')

    print('-' * 40)
    print("        %5d lines from %d changesets" % (tot, len(set(c))))
