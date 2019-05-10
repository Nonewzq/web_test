import socket


def run():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 8080))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()

        data = conn.recv(8096)
        data = str(data, encoding='utf-8')
        headers, bodys = data.split("\r\n\r\n")
        temp_list = headers.split("\r\n")
        method, url, protocal = temp_list[0].split(" ")

        if url == "/xxx":
            conn.send(b"123456")
        else:
            conn.send(b"404 not found")

        print(data)

        conn.close()


if __name__ == "__main__":
    run()

