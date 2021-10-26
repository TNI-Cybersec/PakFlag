# Flaggen : CTF Flag Generator
# https://github.com/TNI-Cybersec/Flaggen

from hashlib import pbkdf2_hmac
from os import urandom


def gen_flag(name: str, n: int, dkl: int) -> None:
    flags = []
    for i in range(n):
        salt = urandom(32)
        key = pbkdf2_hmac(hash_name='md5', password=name.encode(), salt=salt, iterations=1337, dklen=dkl)
        flag = f"{name}{{{key.hex()}}}"
        flags.append(flag + '\n')
        print("{}".format(flag))
    write_flag(flags)


def write_flag(flag):
    with open(filename, mode='w') as file:
        file.writelines(flag)


def main():
    name = input("Flags' name\t: ").strip()

    length = input("Length\t\t: ")
    length = int(length) if length.isnumeric() else None

    num = input("Number\t\t: ")
    num = int(num) if num.isnumeric() else 100

    global filename
    filename = f"{name}_flags.txt"
    open(filename, mode='w')

    print('-' * 50)
    gen_flag(name, num, length)
    print('-' * 50)

    print('All flags has been saved as "{}"'.format(filename))


if __name__ == '__main__':
    main()
