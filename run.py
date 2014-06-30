
import zmqros
import argparse
import warnings


def main():
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser(
        description="Runs programs for the ZeroMQ-ROS Middleware."
    )

    parser.add_argument(
        "--host", dest="host", type=str, default="localhost",
        help="Determines the host that the subscriber will listen to"
    )

    parser.add_argument(
        "--port", dest="port", type=int, default=5555,
        help="Determines the port that the subscriber will listen to"
    )

    parser.add_argument(
        "--name", dest="name", type=str,
        help="For the client program to set the name of the client"
    )

    parser.add_argument(
        "--program", dest="program", type=str, default="client",
        help="Used to determine what program will run"
    )

    parser.add_argument(
        "--config", dest="config_file", type=str, default=None,
        help="Configuration file used for the name server"
    )

    args = parser.parse_args()

    if args.program == "client":
        zmqros.client.run(args.host, args.port, args.name)
    elif args.program == "nameserver":
        zmqros.nameserver.run(args.host, args.port, args.config_file)


if __name__ == "__main__":
    main()
