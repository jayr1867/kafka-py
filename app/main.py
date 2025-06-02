import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client,_ = server.accept()

    message_size = (1).to_bytes(4, "big", signed=True)
    correlation_id = (7).to_bytes(4, "big")

    client.sendall(message_size + correlation_id)


if __name__ == "__main__":
    main()
