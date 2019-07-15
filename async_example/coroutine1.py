def coru1(param):
    while True:
        try:
            msg_from_caller = yield param
            print(msg_from_caller)
        except GeneratorExit:
            print("제너레이터 종료하오")


cr = coru1("ping")

print(next(cr))
cr.send("pong")
cr.send("pong2")
cr.close()
cr.throw(StopIteration)
