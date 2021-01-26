from subprocess import Popen, PIPE
from time import sleep


def call_command(lping):
    p = Popen(["ping", "-c", "1", str(lping)],
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    return output


def get_response_time(elems):
    new_string = []
    for elem in elems:
        try:
            new_string.append(elem[elem.index("time"):].split("=")[
                              1].split("ms")[0].strip())
        except (IndexError, ValueError):
            continue
    return new_string


def repeat_command(lping):
    new_string = call_command(lping)
    try:
        new_string = new_string.decode("utf-8").split("\n")
        new_string = get_response_time(new_string)[0]
        print(f"Pingando {lping}: {new_string}ms")
        sleep(0.3)
        return new_string
    except IndexError:
        print(f"ERROR! Cannot ping {lping}... Trying again!")
        sleep(0.6)
        return [str(lping), "ERROR"]


def ping(lping, times=""):
    out = []
    err = []
    if times == "":
        try:
            while True:
                ret = repeat_command(lping)
                if "ERROR" in ret:
                    err.append(ret)
                else:
                    out.append(ret)
        except KeyboardInterrupt:
            pass
    else:
        for i in range(int(times)):
            ret = repeat_command(lping)
            if "ERROR" in ret:
                err.append(ret)
            else:
                out.append(ret)
    if err:
        return out, err
    else:
        return out


if __name__ == "__main__":
    ip = input("IP: ")
    times = input("How many times? Press enter to run indefinitely: ")
    result = ping(ip, times)

    max_ping, min_ping = max(result), min(result)
    total = 0
    for i in result:
        total += int(i)
    average = total / len(result)
    print(f"Max ping: {max_ping}ms, ", end="")
    print(f"Min ping: {min_ping}ms, ", end="")
    print(f"Average ping: {average:.2f}ms")
