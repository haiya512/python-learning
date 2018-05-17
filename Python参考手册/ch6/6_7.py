def receiver():
    print("ready to receive")
    while True:
        n = (yield)
        print("Got %s" % n)

