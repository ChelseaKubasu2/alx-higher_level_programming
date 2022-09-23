#!/usr/bin/python3
"""Fetch content from https://alx-intranet.hbtn.io/status"""
import urllib.request


# Evaluate if running this script directly
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        # Get response body
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
