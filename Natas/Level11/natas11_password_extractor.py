import base64
import requests
import re


def xor(data, key):
    """Function for performing XOR operation on input data and key."""

    if isinstance(data, (bytes)):
        data = bytearray((data))
    else:
        data = bytearray((data.encode("utf-8")))

    key = bytearray(key.encode("utf-8"))

    output = []
    for i, da in enumerate(data):
        output.append(chr(da ^ key[i % len(key)]))

    return "".join(output)


# Send a GET request to the URL "http://natas11.natas.labs.overthewire.org/"
# The authentication credentials ("natas11", "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg") are passed as a tuple to the "auth" parameter
# This code block is responsible for making the HTTP request and storing the response in the variable "r"
# The response object "r" can be used to access the status code, headers, content, etc. of the HTTP response
r = requests.get(
    "http://natas11.natas.labs.overthewire.org/",
    auth=("natas11", "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"),
)

# Extract the value of the "Set-Cookie" header from the response headers
cookie_temp = r.headers["Set-Cookie"].split("=")[1][:-3]

# Calculate the number of characters needed to make the length of "cookie_temp" a multiple of 4
padding = "=" * (4 - (len(cookie_temp) % 4))

cookie_temp += padding

data_decode = base64.b64decode(cookie_temp.encode("utf-8"))

key_temp = """{"showpassword":"no","bgcolor":"#ffffff"}"""

new_key = xor(data_decode, key_temp)[:4]

paramters_url = """{"showpassword":"yes","bgcolor":"#ffffff"}"""

cookie = xor(paramters_url, new_key)

cookie = base64.b64encode("".join(cookie).encode("utf-8")).decode("utf-8")


cookies = {"data": cookie}

r_password = requests.get(
    "http://natas11.natas.labs.overthewire.org/",
    auth=("natas11", "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"),
    cookies=cookies,
)

content = r_password.text

# Define a regular expression pattern for matching the password for "natas12"
pattern = r"The password for natas12 is ([A-Za-z0-9]+)"

result = re.search(pattern, content)

print(result.group().split()[5])