import base64
import binascii


encoded_secret = "3d3d516343746d4d6d6c315669563362"

secret = binascii.unhexlify(encoded_secret).decode("utf-8")[::-1]

password = base64.b64decode(secret).decode("utf-8")

print(password)


#! Code PHP:
"""<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
"""