from hashlib import sha1

def proencrypt(data):
    s1 = sha1()
    s1.update(str(data).encode("utf8"))
    return s1.hexdigest()

