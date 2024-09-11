# Sapendo che la chiave di cifra è: XXXXIsASecretKey

# (non conoscete i primi 4 caratteri della chiave)

# e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==

# NB: la parte ignota delle chiave contiene esclusivamente maiuscole e minuscole

# Trovare la decodifica del messaggio.
# prova di decifra brute force



from Lezione2.messaggioCif import decrypt


enc = "OgJuOYJZT0FDb47DBOkNgA=="
key = "XXXXIsASecretKey"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    dec = decrypt(enc, key)
                    print("La chiave è: ", key, " e la stringa è: ", dec)
                except:
                    # continua
                    continue
