
# import math
# int_ip = [int(x) for x in input().split('.')]
# c = 0
# mask_bits=8
# if int_ip[0] in range(0,127):
#     c=1
#     print("CLASS A")
# elif int_ip[0] in range(128,192):
#     c=2
#     mask_bits+=8
#     print("CLASS B")
# elif int_ip[0] in range(192,240):
#     c=3
#     mask_bits += 16
#     print("CLASS C")
# else:
#     print("CLASS D or E")
#
# num_subnets = int(input())
# mask_bits+=int(math.ceil(math.log(num_subnets,2)))
# print(mask_bits)

ch='{0:08b}'.format(128)
k=int(ch)^int'({0:08b}'.format(0))