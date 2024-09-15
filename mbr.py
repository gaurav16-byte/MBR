import os

dic = dict(zip(list('0123456789ABCDEF'), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#USE WHEN SYSTEM IS USING MBR PARTITION SCHEME
'''
f = open(r'\\.\PhysicalDrive0', 'rb')
mbr_hex = f.read(512).hex()
f.close()
'''

#USE WHEN YOUR SYSTEM ISN'T MBR AND YOU HAVE THE HEXADECIMAL DATA OF THE SECTOR
'''
mbr_hex = 'add the hex here'
'''
mbr = []
for i in range(0, len(mbr_hex), 2):
    mbr.append(mbr_hex[i:i+2])

boot_code = mbr[:446]
part1 = mbr[446:462]
part2 = mbr[462:478]
part3 = mbr[478:494]
part4 = mbr[494:510]
sig_code = mbr[510:]

def endian(bytess):
    bytess.reverse()
    hexa = ''
    for i in bytess:
        hexa += i

    return hexa

def hex_to_decimal(dic, hexa):
    count = 0
    for i in range(len(hexa)):
        count += dic[hexa[i].upper()] * (16 ** (len(hexa) - i - 1))
    return count

def bin_to_decimal(binary):
    count = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            count += 2 ** (len(binary) - i - 1)
    return count

def chs(head, sector, cylinder):
    h = s = c = 0
    head = str(bin(head))[2:]
    sector = ((8-len(str(bin(sector))[2:])) * '0') + str(bin(sector))[2:]
    cylinder = ((8-len(str(bin(cylinder))[2:])) * '0') + str(bin(cylinder))[2:]
    h = bin_to_decimal(head)

    cylinder = sector[:2] + cylinder
    sector = sector[2:]
    s = bin_to_decimal(sector)
    c = bin_to_decimal(cylinder)
    return h, s, c

def partition(part):
    print(f"Partition 1: {part}")
    if part[0] == '80':
        print(f"Partition 1 is bootable")
    else:
        print(f"Partition 1 is not bootable")
    h, s, c = hex_to_decimal(dic, part[1]), hex_to_decimal(dic, part[2]), hex_to_decimal(dic, part[3])
    head, sector, cylinder = chs(h,s,c)
    print(f"Starting Head Sector Cylinder: ({head},{sector},{cylinder})")
    print(f"Partition Type: {part[4]}")
    ending_h, ending_s, ending_c = hex_to_decimal(dic, part[5]), hex_to_decimal(dic, part[6]), hex_to_decimal(dic, part[7])
    head, sector, cylinder = chs(ending_h, ending_s, ending_c)
    print(f"Ending Head Sector Cylinder: ({head},{sector},{cylinder})")
    start_sector = hex_to_decimal(dic, endian(part[8:12]))
    print(f"Starting Sector: {start_sector}")
    partition_size = hex_to_decimal(dic, endian(part[12:])) * 512
    size_MB = partition_size / (1024*1024)
    size_GB = partition_size / (1024*1024*1024)
    print(f"Partition Size: {size_MB}MB, {size_GB}GB\n")

for i in [part1, part2, part3, part4]:
    partition(i)
