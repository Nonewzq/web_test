import socket


def f1():
    return b"f1,xxx"


def f2():
    return b"f2,ooo"


routers = {
    "/xxx": f1,
    "/ooo": f2,
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
            response = func_name()
        else:
            response = b"404"

        conn.send(response)

        # if url == "/xxx":
        #     conn.send(b"123456")
        # else:
        #     conn.send(b"404 not found")

        print(data)

        conn.close()


if __name__ == "__main__":
    run()

