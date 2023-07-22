#  convert dec to bin using recrusion


def find(dec):
    if dec == 0:
        return
    else:
        find(int(dec / 2))
        print(dec % 2, end="")


find(200)
