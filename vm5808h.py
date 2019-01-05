import telnetlib
import socket
import logging

# 環境変数のため
import settings
import os

HOST = os.getenv("VM5808H_IP_ADDRESS")
ID = os.getenv("VM5808H_USERNAME")
PW = os.getenv("VM5808H_PASSWORD")


logging.basicConfig(level=logging.WARNING)


def check_version():

    try:
        tn = telnetlib.Telnet(host=HOST, timeout=2)
        # tn.set_debuglevel(7)

        logging.debug(tn.read_until(b"Enter Username:").decode("ascii").split("\r\n")[1:-1])
        tn.write(ID.encode("ascii") + "\r".encode('ascii'))

        logging.debug(tn.read_until(b"Password:").decode("ascii").split("\r\n")[1:-1])
        tn.write(PW.encode("ascii") + "\r".encode('ascii'))
        logging.debug(tn.read_until(b">").decode("ascii").split("\r\n")[1:-1])

        # Check version
        tn.write("vr\r".encode("ascii"))
        result = tn.read_until(b">").decode("ascii").split("\r\n")[1:-1]
        logging.debug(result)

        # Ctrl+Q押下と同様
        tn.write("\x11".encode("ascii"))

        return {
            "result": "succeeded",
            "message": result
        }
    except socket.timeout as e:
        return {
            "result": "failed",
            "message": e.args,
            "message_from_kimura": "たぶんHDMIマトリクススイッチャーの電源が入っていません。"
        }


def switch_port(input_port, output_port):

    try:
        tn = telnetlib.Telnet(host=HOST, timeout=2)
        # tn.set_debuglevel(7)

        logging.debug(tn.read_until(b"Enter Username:").decode("ascii").split("\r\n")[1:-1])
        tn.write(ID.encode("ascii") + "\r".encode('ascii'))

        logging.debug(tn.read_until(b"Password:").decode("ascii").split("\r\n")[1:-1])
        tn.write(PW.encode("ascii") + "\r".encode('ascii'))
        logging.debug(tn.read_until(b">").decode("ascii").split("\r\n")[1:-1])

        # Switch input,output
        tn.write("ss {input},{output}\r".format(input=input_port, output=output_port).encode("ascii"))
        result = tn.read_until(b">").decode("ascii").split("\r\n")[1:-1]
        logging.debug(result)

        # Ctrl+Q押下と同様
        tn.write("\x11".encode("ascii"))

        return {
            "result": "succeeded",
            "message": result
        }
    except socket.timeout as e:
        return {
            "result": "failed",
            "message": e.args,
            "message_from_kimura": "たぶんHDMIマトリクススイッチャーの電源が入っていません。"
        }


if __name__ == '__main__':

    print(check_version())

    # switch_port("01", "01")
    # switch_port("02", "02")
    # switch_port("03", "03")
