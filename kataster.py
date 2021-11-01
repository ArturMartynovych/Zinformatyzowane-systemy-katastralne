import re

FILE = "E:\PW\ROK_3\kataster\project_1\Kontury_eksport_dz.txt"
valid = []

OFU_all = "(R|S|Ł|Ps|Br|Wsr|W|Lzr|Ls|Lz|B|Ba|Bi|Bp|Bz|K|dr|Tk|Ti|Tp|Wm|Wp|Ws|Tr|N)"
OFU_1 = "R|S|Br|Wsr|W|Lzr"  # for OZU R
OFU_2 = "Ł|S|Br|Wsr|W|Lzr"  # for OZU Ł
OFU_3 = "Ps|S|Br|Wsr|W|Lzr"  # for OZU Ps
OFU_4 = "Ls|W"  # for OZU Ls
OFU_5 = "Lz|W"  # for OZU Lz

OZU_1 = "Ł|Ps|Ls|Lz"
OZU = ["R", "Ł", "Ps", "Ls", "Lz"]

OZK_1 = "I|II|III|IV|V|VI"
OZK_2 = "I|II|IIIa|IIIb|IVa|IVb|V|VI|VIz"

start = "\d{1,3}" + "-" + "\d{1,3}" + "/"


def openFileKlasouzytek(path):
    klasouzytek = []
    with open(path, encoding="cp1250") as fileHandler:
        for line in fileHandler:
            line1 = line.strip()
            if line1 == "":
                break
            klasouzytek.append(line1)
            fileHandler.readline()
            line3 = fileHandler.readline().strip()
            val = int(line3)
            for i in range(0, val + 1):
                fileHandler.readline()
    fileHandler.close()
    return klasouzytek


def checkOZU_OZK(klasouzytek):
    for i in klasouzytek:
        pattern1 = f"({start})" + f"({OZU_1})" + f"({OZK_1})"
        result1 = re.fullmatch(pattern1, i)

        pattern2 = f"({start})" + f"({OZU[0]})" + f"({OZK_2})"
        result2 = re.fullmatch(pattern2, i)
        if result1 is not None:
            valid.append(result1.string)
        if result2 is not None:
            valid.append(result2.string)


def checkOFU(klasouzytek):
    for i in klasouzytek:
        pattern = f"({start})" + f"{OFU_all}"
        result = re.fullmatch(pattern, i)
        if result is not None:
            valid.append(result.string)


def checkOFU_OZU_OZK(klasouzytek):
    for i in klasouzytek:
        pattern1 = f"({start})" + f"({OFU_1})" + f"?-({OZU[0]})" + f"({OZK_2})"
        result1 = re.fullmatch(pattern1, i)
        if result1 is not None:
            valid.append(result1.string)

        pattern2 = f"({start})" + f"({OFU_2})" + f"?-({OZU[1]})" + f"({OZK_1})"
        result2 = re.fullmatch(pattern2, i)
        if result2 is not None:
            valid.append(result2.string)

        pattern3 = f"({start})" + f"({OFU_3})" + f"?-?({OZU[2]})" + f"({OZK_1})"
        result3 = re.fullmatch(pattern3, i)
        if result3 is not None:
            valid.append(result3.string)

        pattern4 = f"({start})" + f"({OFU_4})" + f"-({OZU[3]})?" + f"({OZK_1})"
        result4 = re.fullmatch(pattern4, i)
        if result4 is not None:
            valid.append(result4.string)

        pattern5 = f"({start})" + "/" + f"({OFU_5})" + f"-({OZU[4]})?" + f"({OZK_1})"
        result5 = re.fullmatch(pattern5, i)
        if result5 is not None:
            valid.append(result5.string)
    # pattern1 = "\d{1,3}" + "-" + "\d{1,3}/" + (?(?=(OZU_2 == OFU_1))(f"({OZU_2})" + f"({OZK_2})")|(f"({OFU_1})" + f"({OZU_2})" + f"({OZK_2}"))


def validItems(klasouzytek):
    checkOZU_OZK(klasouzytek)
    checkOFU(klasouzytek)
    checkOFU_OZU_OZK(klasouzytek)
    notValid = sorted(list(set(klasouzytek) - set(valid)))
    return set(valid), set(notValid)


def main():
    klasouzytek = openFileKlasouzytek(FILE)
    checkOZU_OZK(klasouzytek)
    checkOFU(klasouzytek)
    checkOFU_OZU_OZK(klasouzytek)
    notValid = sorted(list(set(klasouzytek) - set(valid)))
    for i, line in enumerate(set(notValid)):
        print(i + 1, line)


if __name__ == '__main__':
    # klasouzytek = openFileKlasouzytek(FILE)
    # valid_, notValid = validItems(klasouzytek)
    # for m, line in enumerate(valid):
    #     print(m + 1, line)
    main()
