import hashlib


def getHashString(string):
    """
    gets a string and returns the hexadecimal representation of its hash using sha256.

    :param string: the string to find its hash value.
    :return: the hash (hexadecimal).
    """
    # Hash functions expect bytes as input: the encode() method turns strings to bytes
    output = hashlib.sha256(string.encode())
    return f'string: {string}, hash: {output.hexdigest()}'


def getHashImage(source):
    """
    gets an image source and returns the hexadecimal representation of its hash using sha256.

    :param source: the source of the image to find its hash value.
    :return: the hash (hexadecimal).
    """
    try:
        # The "rb" argument denotes that the file should be in read-only mode, and read as bytes.
        with open(source, "rb") as file:
            # We use hexdigest() to convert bytes to hex
            hash = hashlib.sha256(file.read()).hexdigest()
            return f'image: {source}, hash: {hash}'
    except IOError:
        return "file not found"


print(getHashString("backpack"))
print(getHashString("image.png"))
print(getHashImage("image.png"))

block_1038 = {'index': 1038, 'timestamp': "2020-02-25T08:07:42.170675",
              'data': [{'sender': "bob", 'recipient': "alice", 'amount': "$5", }],
              'hash': "83b2ac5b",
              'previous_hash': "2cf24ba5f"}
