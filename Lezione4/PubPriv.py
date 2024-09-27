
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
# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAwNP2Ics3B4Or5+8pzy2d0mbi4s24D5vPa7zR4p56n+wRQpSV\nbCME4qRF2DF8zL8xRq072869xcw9H1FZPSo3k/GPwWLFWnRw+q4XFUcNA1UWnwQi\nzW0S5j0T54Ah/ing7fIRMGVWeg8YGeyz4GpqdEAwIPQDMjcrpcoYwj9/zv7VOVox\nH4y9VQO8rl09hHlRjqPT+TVDe/MAJVvqn21cnMRmQO1nKLF12sCsnZqtf3jHtD3/\nSaajbhkfJ8IIxcj7w65rOcdWi5kBDYx7b3PrvDt/uoucfS6rU9C0n/M2J5a3+2tN\ntsZV9V37frdiDitfqOMK8GKSDqvlvwLW0LL1+QIDAQABAoIBAAIPQYXC4eeWpHNp\nvoyT9CeXKb06bUjdZS3Faoh9INosb1LCu4XYKekxz/0rKiYVtLUIjKcgYi6Gq/B1\nsfpRRR6zadGq+Giq7bn/ugdkJuNuOTuhk62WCKmk5V2HpNVOJTTlbQGTU4UiPCOq\nv5EaEeED/n+bm50hsbmnmvQYMYlIcsX/a3VOb4janrMvYKgQf/+5RopRfK0gDKyd\n18dtMNZSTPm8kR0NL1Uk+5Z7xMEbmFnuvo1h+DNh45G6TtPrd/oivHZWhwq0UnAz\nlbELS30hIqsH3I1Qsg15+dV2RTBl2lL6l0Z4Pje9wYHAjok+uTmpx2wEI1d7GPOd\nyb5CiXECgYEA00RYl1LJuad8ZrMdwSv1BmfHoHcq/hWylPaank87nwKw3tBo+k32\n/C9LmFvKx9pSi/FcSZ3k+lKLldXBAD0S5rt8Myii1NJcFjrV1TQG2c3SM5rXYnBK\nDMDwEpifjrNYf5/TyIcyoMPLAHyU4NmWoVnV2Tarj6wKqJvcI7c8OlsCgYEA6agi\ntsqbNay9n+1Sj5ElL0aTsXZTyBnq6jUmFy+oIremEmW2lTj5PNc6TAp1eok6Lglt\n93P6IgfFgiVui2Bfz7DlM0kZwxoE6Ss1OcAvb2YjJ33dVuCNFEVV6eoIFDFNUOwU\ngGjN+H2nAQooQC5E2H+woyv6iRuFSU9/b8pd+TsCgYEAmz8rFrAIerv/53wSDmSd\n3sIeaOWJG0OYgmyg/FpfBp80l9dwfRcTuweKNoClh60AYcPQPGyh2e0Uk9uKwwEe\nRZ1aTEG9PkUC1HcRsWVU73KW18MeKUE4uRyCjjfHcFaMXuR0/XOUGZ0nLMlfocdj\nMFhSlBbfhWk4P+SgpUI+KOcCgYA6yLozErYJwvPSEHr8859PTYpK02IwrZSUZ9q1\nap/6XAnEByLwV+0ciWl5SAhWU7/3ZRftcZg0h5ABNjmhhxWTwwVm6bU5iIpDv0Mc\nzGUiuaeOf/P3r3bO6sK6ns55hg3Vlg9yXuuy4KnrcQq/WuSnMzjVVHMrm2jlEMMW\n9Oq/kQKBgQCEvrNSeCSgAe2NPeTjuKAtavVbIzAv+y7GK8Mf+BhkdiO+DUqdl6He\nZbnnIlSwljd38Mj75JPUaE8RNi0eCfDHHShbvAE3Zn+CO4TPht06TEPJtmlZMs6A\nfezvmNMfat7qvC9FHOmUTu/65EZnb5ft1RrvFIfeIKvZBfd5I9Wl7g==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwNP2Ics3B4Or5+8pzy2d\n0mbi4s24D5vPa7zR4p56n+wRQpSVbCME4qRF2DF8zL8xRq072869xcw9H1FZPSo3\nk/GPwWLFWnRw+q4XFUcNA1UWnwQizW0S5j0T54Ah/ing7fIRMGVWeg8YGeyz4Gpq\ndEAwIPQDMjcrpcoYwj9/zv7VOVoxH4y9VQO8rl09hHlRjqPT+TVDe/MAJVvqn21c\nnMRmQO1nKLF12sCsnZqtf3jHtD3/SaajbhkfJ8IIxcj7w65rOcdWi5kBDYx7b3Pr\nvDt/uoucfS6rU9C0n/M2J5a3+2tNtsZV9V37frdiDitfqOMK8GKSDqvlvwLW0LL1\n+QIDAQAB\n-----END PUBLIC KEY-----"
Gimmi = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtV2KtG3Eili7N9dIcpj+\nEJxyZNTXxaBw9cV9YvnfbpcS+vfH4Z2O3Mhm9YAaxILSMJGD/lhqYJmCaj9Lc8JP\nXtIGN1GOl/Gt5VmerkKW4ff9i26HckoP0JpIK2fpBVJYwXsm3mocY1Ss2yxkdOk0\ntfbINs5/n3fKVrlF5HXISmogCvsK049axY/F7ivQ6dz1n18JcRS5aZgPUUx6XZlW\nxiswyPjhMu0DlAy03Mpw9TrxTJesI0bFtJ1eqKvAMKcKhaHKeDZpNInhVuiRPA6/\nROW6KzjNjTKhiwz8YHROZ+zgpKGtePccBvOU91SK9CaD1CnXPZD+wZA0U7+EIh0F\nOQIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key_collega = RSA.import_key(Gimmi)


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
message = ""
encrypted_message = encrypt_message(message, public_key_collega)
decrypted_message = decrypt_message(encrypted_message, key_pair)   

#print("Original Message:", message)
#print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)  
