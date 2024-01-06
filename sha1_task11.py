import hashlib
# function to check integrity of message
def msg_check(msg, h, htype):
    hash = ""
    if htype == "SHA1":
        m = hashlib.sha1()
        m.update(msg.encode())
        hash = m.hexdigest()
    elif htype == "SHA1":
        m = hashlib.sha256()
        m.update(msg.encode())
        hash = m.hexdigest()
    if hash == h:
        return "message is valid"
    else:
        return "message has been modified"

mess = "1234567"
md = hashlib.sha1()
md.update(mess.encode())
hash1 = md.hexdigest()
#modifying message
mess = mess+ "8"
# check message validity
rep = msg_check(mess, hash1, "SHA1")
print("the result: ", rep)