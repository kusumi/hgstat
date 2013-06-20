#!/usr/bin/env python

if __name__ == '__main__':
    import re
    import util

    test_date, sort = util.parse_option()
    days = "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    d = dict([(x, 0) for x in days])
    p = util.popen_hglog("--template", "{date|isodate} @{date|date}\n")
    r = re.compile(r"^(\d{4}-\d{2}-\d{2}) .+ @(\S+) ")

    for x in p:
        if x:
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

    tot = sum(d.values())
    for k in g:
        v = d[k]
        if not tot:
            p = 0
        else:
            p = 100.0 * v / tot
        print("%s %5d %4.1f[%%]" % (k, v, p))

    print('-' * 40)
    print("    %5d" % tot)
