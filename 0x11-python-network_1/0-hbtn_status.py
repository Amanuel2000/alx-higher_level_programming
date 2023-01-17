#!/usr/bin/python3
"""This will Fetch https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(urllib.request.Request("https://alx-intranet.hbtn.io/status")) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))