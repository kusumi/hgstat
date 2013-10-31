#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    import util

    test_date, sort, graph = util.parse_option()
    d = {}

    for x in util.popen_hg_log("--template", "{date|shortdate}\n"):
        if test_date(x):
            x = x[:-3] # cut -DD
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    if not d:
        print("No data")
        sys.exit(1)

    l = d.values()
    tot = sum(l)
    if graph:
        gfn = util.get_graph_bar_fn(21, max(l))
    else:
        gfn = None
    done = []

    def fn(k):
        v = d.get(k, 0)
        if tot:
            p = 100.0 * v / tot
        else:
            p = 0
        if gfn:
            b = gfn(v)
        else:
            b = ''
        print("%7s %5d %4.1f[%%]%s" % (k, v, p, b)) # 21
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
    print("        %5d changesets" % tot)
