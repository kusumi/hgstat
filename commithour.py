#!/usr/bin/env python

if __name__ == '__main__':
    import re
    import util

    test_date, sort, graph = util.parse_option()
    d = dict([(x, 0) for x in range(24)])
    r = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d+):\d+ ")

    for x in util.popen_hg_log("--template", "{date|isodate}\n"):
        m = r.match(x)
        if m:
            date = m.group(1)
            hour = int(m.group(2))
            if test_date(date):
                d[hour] += 1
    if sort:
        l = sorted([(v, k) for k, v in d.items()])
        g = reversed([x[1] for x in l])
    else:
        g = range(24)

    l = d.values()
    tot = sum(l)
    if graph:
        gfn = util.get_graph_bar_fn(19, max(l))
    else:
        gfn = None

    for k in g:
        v = d[k]
        if k < 12:
            s = "AM"
        else:
            s = "PM"
            k -= 12
        if tot:
            p = 100.0 * v / tot
        else:
            p = 0
        if gfn:
            b = gfn(v)
        else:
            b = ''
        print("%2d %2s %5d %4.1f[%%]%s" % (k, s, v, p, b)) # 19

    print('-' * 40)
    print("      %5d changesets" % tot)
