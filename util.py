import fcntl
import optparse
import re
import struct
import subprocess
import sys
import termios

def popen_hg(*args):
    l = ["hg"]
    l.extend(args)
    p = subprocess.Popen(l, stdout=subprocess.PIPE)
    for x in p.stdout.readlines():
        ret = x.decode("ascii", "ignore").rstrip()
        if len(ret):
            yield ret

def popen_hglog(*args):
    l = ["log"]
    l.extend(args)
    return popen_hg(*l)

def get_size():
    try:
        x = fcntl.ioctl(0, termios.TIOCGWINSZ, '0' * 8)
        return struct.unpack('H' * 4, x)[:2]
    except:
        print(sys.exc_info()[1])

def get_graph_bar_fn(statwidth, maxvalue):
    l = get_size()
    if not l:
        return None
    x = l[1] - statwidth
    if x <= 0:
        return None
    def fn(n):
        return '*' * int((1.0 * n / maxvalue) * x)
    return fn

def parse_option():
    parser = optparse.OptionParser()
    parser.add_option("--after", default='', metavar="YYYY-MM(-DD)")
    parser.add_option("--before", default='', metavar="YYYY-MM(-DD)")
    parser.add_option("--sort", action="store_true", default=False)
    parser.add_option("--graph", action="store_true", default=False, help="requires ioctl(TIOCGWINSZ)")
    opts, args = parser.parse_args()

    r = re.compile(r"^(\d{4}-\d{2}(-\d{2})?)$")
    ad, bd = '', ''

    if opts.after:
        m = r.match(opts.after)
        if m:
            ad = m.groups()[0]
            print("after(>=) '%s'" % ad)
        else:
            print("after(>=) '???'")

    if opts.before:
        m = r.match(opts.before)
        if m:
            bd = m.groups()[0]
            print("before(<) '%s'" % bd)
        else:
            print("before(<) '???'")

    def test_date(date):
        assert len(date) == 10
        return  (not ad and not bd) or \
                (not ad and date < bd) or \
                (not bd and date >= ad) or \
                (ad <= date < bd)
    return test_date, opts.sort, opts.graph
