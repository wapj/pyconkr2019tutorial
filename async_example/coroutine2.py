class HighNumberException(Exception):
    pass


def infinite_pingpong(param):
    while True:
        try:
            msg_from_caller = yield param
            print(msg_from_caller)
        except HighNumberException:
            break
        except GeneratorExit:
            print("코루틴 종료! " + msg_from_caller)


def coru_throw():
    for x in range(10):
        coru = infinite_pingpong(f"pping {x}")

        if x > 1:
            try:
                coru.throw(HighNumberException)
            except HighNumberException as e:
                print(e)

        print(next(coru))
        coru.send(f"ppong {x}")


def coru_close():
    for x in range(100):
        coru = infinite_pingpong(f"pingping {x}")
        print(next(coru))
        coru.send(f"pongpong {x}")

        if x >= 3:
            coru.close()  # 종료시에는 모든 코루틴을 종료시킨다.

try:
    coru_throw()
except HighNumberException as e:
    print(e)
