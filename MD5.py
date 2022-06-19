import codecs
a = 0x67452301
b = 0xefcdab89
c = 0x98badcfe
d = 0x10325476

t = ( 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8,
    0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193,
    0xa679438e, 0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51,
    0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905,
    0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681,
    0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60,
    0xbebfbc70, 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244,
    0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92,
    0xffeff47d, 0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314,
    0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 )

s = ( 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7,
    12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10,
    15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21 )

j = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
    1,6,11,0,5,10,15,4,9,14,3,8,13,2,7,12,
    5,8,11,14,1,4,7,10,13,0,3,6,9,12,15,2,
    0,7,14,5,12,3,10,1,8,15,6,13,4,11,2,9)

def F(X,Y,Z):
    outputF = (X & Y) | ((~X) & Z)
    return outputF

def G(X,Y,Z):
    outputG = (X & Z) | (Y & (~Z))
    return outputG

def H(X,Y,Z):
    outputH = X ^ Y ^ Z
    return outputH

def I(X,Y,Z):
    outputI = Y ^ (X | (~Z))
    return outputI

def circularShiftLeft(data,bit):
    data=data & 0xffffffff
    dataShifted = ((data << bit) | (data >> (32 - bit))) & 0xffffffff
    return dataShifted

def block(a,b,c,d,M,s,t):
    temp_a,temp_b,temp_c,temp_d=a, b, c, d
    for i in range(64):
        if (i < 16):
            tempStore=F(b, c, d)
        elif (i < 32):
            tempStore=G(b, c, d)
        elif (i < 48):
            tempStore=H(b, c, d)
        else:
            tempStore=I(b, c, d)
        a=b + circularShiftLeft((a + tempStore + M[j[i]] + t[i]),s[i])
        a, b, c, d=d, a, b, c
    a, b, c, d = (a + temp_a) & 0xffffffff,(b + temp_b) & 0xffffffff,(c + temp_c) & 0xffffffff,(d + temp_d) & 0xffffffff
    return a, b, c, d


def reverse_hex(hex_str):
    hex_str_list = []
    for i in range(0,len(hex_str),2):
        hex_str_list.append(hex_str[i:i+2])
    hex_str_list.reverse()
    hex_str_result = ''.join(hex_str_list)
    return hex_str_result

def getMList(hexList):
    M=[]
    hexStr = ''.join(hexList).split('0x')
    hexStr = ''.join(hexStr)
    for i in range(16):
        M.append(hexStr[i*8:(i*8+8)])
        M[i] = reverse_hex(M[i])
        #print("hex"+M[i])
        M[i] = int(("0x"+M[i]),16)
        #print(hex(M[i]))
    return M

def hashMD5():
    global a,b,c,d
    input_str = input("输入字符串：")
        # "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    hexList=list(map(hex,(map(ord,input_str))))
    listLen = len(hexList) * 8
    hexList.append("0x80")
    while (len(hexList)*8 + 64) % 512 != 0:
        hexList.append("0x00")

    hexListLen = hex(listLen)[2:]
    hexListLen = hexListLen.rjust(16,'0')
    hexListBigOrder = reverse_hex(hexListLen)
    hexListAppend = []
    for i in range(0,len(hexListBigOrder),2):
        hexListAppend.append('0x'+ hexListBigOrder[i:i+2])
    hexList.extend(hexListAppend)

    for i in range(int(len(hexList)/64)):
        hexListi=hexList[i*64:(i+1)*64]
        M=getMList(hexListi)
        a, b, c, d = block(a,b,c,d,M,s,t)
        #print(hex(a),hex(b),hex(c),hex(d))

    a = reverse_hex(str(hex(a))[2:])
    b = reverse_hex(str(hex(b))[2:])
    c = reverse_hex(str(hex(c))[2:])
    d = reverse_hex(str(hex(d))[2:])
    hashmd5 = ''.join((a,b,c,d))
    print("哈希值为：",hashmd5)
















