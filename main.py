from micro.micro_manager import MicroManager

def main():
    micro_port = "COM3"
    micro = MicroManager(port = micro_port)
    micro.connect()

    try:
        while True:
            if micro.connection.is_open > 0:
                data = micro.receive_data()
                if data is not None:
                    print(data)
    except KeyboardInterrupt:
        print("Interrupted")
    finally:
        micro.disconnect()


if __name__ == '__main__':
    main()





