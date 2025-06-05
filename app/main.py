import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client,_ = server.accept()


    rec_msg = client.recv(1024)

    message_size = (1).to_bytes(4, "big", signed=True)
    correlation_id = rec_msg[8:12]

    client.sendall(message_size + correlation_id)
    client.close()

if __name__ == "__main__":
    main()
