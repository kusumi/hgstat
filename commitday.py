#!/usr/bin/env python

if __name__ == '__main__':
    import calendar
    import re
    import util

    test_date, sort, graph = util.parse_option()
    days = list(calendar.day_abbr)
    d = dict([(x, 0) for x in days])
    r = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\S+) ")

    for x in util.popen_hg_log("--template", "{date|shortdate} {date|date}\n"):
        m = r.match(x)
        if m:
            date, day = m.groups()
            if test_date(date) and day in days:
                d[day] += 1
    if sort:
        l = sorted([(v, k) for k, v in d.items()])
        g = reversed([x[1] for x in l])
    else:
        g = days

    l = d.values()
    tot = sum(l)
    if graph:
        gfn = util.get_graph_bar_fn(17, max(l))
    else:
        gfn = None

    for k in g:
        v = d[k]
        if tot:
            p = 100.0 * v / tot
        else:
            p = 0
        if gfn:
            b = gfn(v)
        else:
            b = ''
        print("%3s %5d %4.1f[%%]%s" % (k, v, p, b)) # 17

    print('-' * 40)
    print("    %5d changesets" % tot)
