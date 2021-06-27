from os import system
from time import sleep

n = 2

with open("hosts.txt") as f:
    for host in f.read().splitlines():
        system(f"ping -n {n} {host}")
        sleep(1.5)
