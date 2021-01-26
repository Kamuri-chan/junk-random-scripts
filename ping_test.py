import myPing as ping
import rel  # this is a file i cannot upload because contains sensible and secret information
# ^ but it's a dictionary of ips in this format: {'normal_name': (technical_name, ip)}


def ping_test(times=4):
    relation = rel.relation
    out = {}
    err = []
    for k, v in relation.items():
        r = ping.ping(relation[k][1], 4)
        if isinstance(r, tuple):
            out[relation[k][1]] = r[0]
            err.append(r[1])
        else:
            out[relation[k][1]] = r
    if err:
        return out, err
    else:
        return out


def average(values):
    if len(values) > 0:
        avg = 0
        for i in values:
            if i is not None:
                avg += float(i)
        avg = avg / len(values)
        return avg
    else:
        return 0


def max(values):
    m = 0
    it = 0
    for i in range(len(values)):
        if values[i] is not None:
            if it == 0:
                m = values[i]
            elif values[i] < m:
                m = values[i]
    return m


def min(values):
    m = 0
    it = 0
    for i in range(len(values)):
        if values[i] is not None:
            if it == 0:
                m = values[i]
            elif values[i] < m:
                m = values[i]
    return m


if __name__ == "__main__":
    r = ping_test()
    out = []
    err = []
    if isinstance(r, tuple):
        out = r[0]
        err = r[1]
    else:
        out = r
    info_list = {}
    for k, v in out.items():
        info_list[k] = max(v), min(v), average(v)

    for k, v in info_list.items():
        if v[2] == 0:
            v = (v[0], v[1], "error")
        else:
            v = (v[0], v[1], f"{v[2]:.2f}")
        print(f"{k}: max ping: {v[0]}, min ping: {v[1]}, average ping: {v[2]}")
    if err:
        print(err)
