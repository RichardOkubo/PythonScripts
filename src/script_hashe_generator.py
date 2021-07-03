from hashlib import md5, sha1, sha256, sha512

menu = lambda option, string: {
    "md5": md5(string.encode("utf-8")),
    "sha1": sha1(string.encode("utf-8")),
    "sha256": sha256(string.encode("utf-8")),
    "sha512": sha512(string.encode("utf-8")),
}.get(option, md5(string.encode("utf-8")))

result = menu(
    input("* Choose the type of hash ("
          " md5 [default] | sha1 | sha256 | sha512 ) : "),
    input("* Text to be applied : ")
)

print(f"* Generated hash : {result.hexdigest()}")
