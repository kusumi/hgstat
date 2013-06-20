#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    import util

    test_date, sort = util.parse_option()
    d = {}
    s = util.popen_hglog("--template", "{date|shortdate}\n")

    for x in s.split('\n'):
        if x and test_date(x):
            x = x[:-3] # cut -DD
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
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
        if not tot:
            p = 0
        else:
            p = 100.0 * v / tot
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
    print("        %5d" % tot)
