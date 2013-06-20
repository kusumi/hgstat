import optparse
import re
import subprocess

def popen_hg(*args):
    l = ["hg"]
    l.extend(args)
    p = subprocess.Popen(l, stdout=subprocess.PIPE)
    for x in p.stdout.readlines():
        yield x.decode("ascii").rstrip()

def popen_hglog(*args):
    l = ["log"]
    l.extend(args)
    return popen_hg(*l)

def parse_option():
    parser = optparse.OptionParser()
    parser.add_option("--after", default='', metavar="YYYY-MM(-DD)")
    parser.add_option("--before", default='', metavar="YYYY-MM(-DD)")
    parser.add_option("--sort", action="store_true", default=False)
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
    return test_date, opts.sort
