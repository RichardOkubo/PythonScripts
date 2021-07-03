from random import SystemRandom
from random import SystemRandom
from string import ascii_letters, digits

length = 30

chars = ascii_letters + digits + "çÇ!@#$%&*()-=+,.;:/?_[]\{\}'~^\""

rnd = SystemRandom()

print("".join(rnd.choice(chars) for i in range(length)))
