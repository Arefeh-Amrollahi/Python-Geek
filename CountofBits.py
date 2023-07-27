def bit_count(self):
    return bin(self).count("1")

print(bit_count(100))
# 3

print(bit_count(255))
# 8

print(bit_count(-100))
# 3