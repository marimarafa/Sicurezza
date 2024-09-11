import base64


def LeggiBinario(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            for v in dati:
                fou.write(str(v))
                fou.write("\n")



def ScriviBinario(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.readlines()
            for num in nums:
                a = int(num).to_bytes()
                fou.write(a)



# esempio
LeggiBinario("pitone.jpeg", "pitone.txt")
ScriviBinario("pitone.txt", "pitone1.jpeg")
 
# E, in modo più coompatto...

def LeggiBinarioHex(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            for v in dati:
                s = hex(v)[2:]
                if len(s) < 2:
                    s = "0" + s
                    fou.write(s)


def ScriviBinarioHex(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.read()
            for i in range(0, len(nums) // 2):
                v = int(nums[2 * i] + nums[2 * i + 1], 16)
                a = v.to_bytes()
                fou.write(a)


# esempio
LeggiBinarioHex("pitone.jpeg", "pitoneHex.txt")
ScriviBinarioHex("pitoneHex.txt", "pitone1Hex.jpeg")

# Ora le dimensioni del .txt sono doppie di quelle del file originale
 
# Possiamo fare di meglio? base64
def LeggiBinarioB64(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            fou.write(base64.b64encode(dati).decode("ascii"))


def ScriviBinarioB64(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.read()
            fou.write(base64.b64decode(nums))


# esempio
LeggiBinarioB64("pitone.jpeg", "pitoneB64.txt")
ScriviBinarioB64("pitoneB64.txt", "pitone1B64.jpeg")