# Nama : Durotun Nafisah Amalia Ahli
# Nim  : 20051397041
# Kelas: D4 Manajemen Informatika 2020A

print("+" + "-" * 18 + "+")
i = 1
while i <= 10:
    n = 1
    while n <= 10:
        print("| %4d |" % (i*n), end="")
        n = n + 1
    print(""),
    i = i + 1
print("+" + "-" * 18 + "+")