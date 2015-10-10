import re

p = re.compile(r'(?P<hours>[01]\d|2[0-3]):(?P<minutes>[0-5]\d)')
for m in re.finditer(p, "Today 16:00, yesterday 08:30"):
    print "group of {0}: {1}, {2}"\
        .format(
            m.group(),
            m.group("minutes"),
            m.group("hours")
    )
    # print "Groups for: " + m.group()
    # for g in m.groups():
    #    print g