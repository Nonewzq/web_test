import socket


def f1(request):
    """

    :param request:
    :return:
    """
    f = open("index.html", "rb")

    data = f.read()
    f.close()
    return data


def f2(request):
    """

    :param request:
    :return:
    """
    return b"f2,ooo"


def f3(request):
    import time
    f = open("aricle.html", "r")
    data = f.read()
    data = data.replace("@@@test@@@", str(time.time()))
    data = bytes(data, encoding="utf-8")
    f.close()
    return data


def f4(request):

    f = open("dbtest.html", "r")
    data = f.read()
    data = bytes(data,encoding="utf-8")
    f.close()
    return data

routers = {
    "/xxx": f1,
    "/ooo": f2,
    "/aricles": f3,
    "/mysql":f4
}


def run():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 8080))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        # print(type(sock.accept()))
        data = conn.recv(8096)
        data = str(data, encoding='utf-8')
        headers, bodys = data.split("\r\n\r\n")
        temp_list = headers.split("\r\n")
        method, url, protocal = temp_list[0].split(" ")
        func_name = ""

        for item in routers:
            if item == url:
                func_name = routers[item]

        if func_name:
            response = func_name(data)
        else:
            response = b"404"
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        conn.send(response)
        print(data)
        conn.close()


if __name__ == "__main__":
    run()

