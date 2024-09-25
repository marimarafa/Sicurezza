
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAn1Q4/NisrrEa/Su+tTERKnsTelXHanenIe8nYbudpY9ymyXJ\n5SZDLVivQZ8Ml0g0ivNQ134ZzqGkMt8COK5odoworlmpDFCU+w5HmOlyy91/NPJ1\nLFSUV2B4GJhCBcGeK4VtKhimpDdWLiuo9E3I+GF7QAOFvt+4lCY1xycUHkzrVXuI\nLKOjYahZf0hPs6CeoySeVKvhIhb1u4yJLlbQgeQUyOs420rgHiUf+OxJ5n+KKWZe\n9NmwyHro37P631BCJtZM/Iov8im9/y9TWraFZP59QOUbjcUokv0YOK8b31MkNeA/\nt9LPQg2lTpaCTpbwJ1NmYA2uWD+WGCJm3AemgQIDAQABAoIBAA7SsJyWx0tXWcny\nVG3vWzKnEahWK6p+6EiIGJNcokLhZh8DXysCVMn2ur4G/zkMiYA149sF4H5wsQyJ\n4onbHAfkwUd7OvbU1mTHBCfjQYAFouHjqWgO6bV5WaL8I1moFOrlS8MuA5mP4Q+E\nQKs97gkW/0xKJ5rFnfABNWFKWZz56FpD7/zBTmgy2wtHMJYUmt2BskO86pFgeEw8\nmW6d/GNtX0Y2N7OENcDd8vGcJg91ZGx3D8YXVk+fCZXEVxFarQPuNx9xwCRATo1D\niek2yumuVVL1chyCIxXzDV+yBCOgAJM5OYj0C1VnU4EVvViXg44QOjC+wQYB4tEa\nx2auf+MCgYEAvPvPFuY4D9SEqcmUR9NsYr/EOgs7YTsTpGPyGbsHTFZmicIF/Obh\n0iIut3k7A5pg/lnLuyPKQBD6xsNZNsyY67oz4mMBfrPBxIsZZMhmDQNgyL67YI0h\ntUxIZyhT437FrXFbnXf9udEp0WoOtxbdwIinefrK/4OS4o3lPFo1eRsCgYEA19RT\nW2fpzXjHYBjsCix4zO8BF20LKKml1YAuRT6kR72bczzpZQA7vVhzZYd9uo+hAsPr\nGrsIm4m6NMoAMYnO6V+Wfzcr4IqvJnI9z9yUjaml3UPp0uGAfEPEmRmeeAl+g+gx\nuFyjj/enUlxELVc4JAOlD9q/pvC2J91VZ/hnFJMCgYAV8/ZphZLLm/dRNd5ovZGg\nowArcfSS5ebxOL796DD/2CWPKR/C8hsXauscWxPU5lEQGuREt/KdoJtRDY5GhFvb\nPkUarj+VNVJz/2iSwYjBSDws9aMUozBgPB1JBnFAQxC5hiqLT04FENwXvIc7E4fs\n/rLdw5ljNyiP8sXHTf9aMwKBgQCk9kFcDNlz1cu1lHbc887E/Cx+ZjbwNnJs89Lp\n1A4mUzK8aqMNMpd2imNxB5U+gccT4QESZkAW+bbb4EUzl9wRHaFezKF5tyZWIV1D\nQZo9iJwguWa/auIUmItsZVts7fzH/zH5cr0FLcmytpjZet+LD0obCxwPEc54O8Cq\nff7zhwKBgCteXoEnI7oOk50We0DlpzURvB90LbraqUF0xrSEsDNLonTEwcffdssE\npglmYr8MTa7tbc/7jJhbYe4r2J5cDfiqgEYRGj5oKlHLo9MCEKdSD22JsXq/GzjJ\nwke5+Zl4vYARKmH1IfTI0Ofpghc3Z/NBfRqTGD4CmOVd1jwC6aA5\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn1Q4/NisrrEa/Su+tTER\nKnsTelXHanenIe8nYbudpY9ymyXJ5SZDLVivQZ8Ml0g0ivNQ134ZzqGkMt8COK5o\ndoworlmpDFCU+w5HmOlyy91/NPJ1LFSUV2B4GJhCBcGeK4VtKhimpDdWLiuo9E3I\n+GF7QAOFvt+4lCY1xycUHkzrVXuILKOjYahZf0hPs6CeoySeVKvhIhb1u4yJLlbQ\ngeQUyOs420rgHiUf+OxJ5n+KKWZe9NmwyHro37P631BCJtZM/Iov8im9/y9TWraF\nZP59QOUbjcUokv0YOK8b31MkNeA/t9LPQg2lTpaCTpbwJ1NmYA2uWD+WGCJm3Aem\ngQIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
