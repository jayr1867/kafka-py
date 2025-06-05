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

    api_version = int.from_bytes(rec_msg[6:8], "big")

    if api_version < 0 or api_version > 4:
        error_code = (35).to_bytes(2, "big", signed=True)
        client.sendall(message_size + correlation_id + error_code)
        client.close()
        return

    client.sendall(message_size + correlation_id)
    client.close()

if __name__ == "__main__":
    main()
