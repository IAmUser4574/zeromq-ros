
import zmqros
import sys
import socket
import argparse
import warnings


def main():
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser(
        description="Runs the ZeroMQ-ROS Midedleware."
    )

    parser.add_argument(
        "--host", dest="host", type=str, default="localhost",
        help="Determines the host that the subscriber will listen to"
    )

    parser.add_argument(
        "--port", dest="port", type=int, default=5555,
        help="Determines the port that the subscriber will listen to"
    )

    args = parser.parse_args()
    zmqros.run(args.host, args.port)


if __name__ == "__main__":
    main()
