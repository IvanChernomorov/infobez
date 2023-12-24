def udv(point, p, a=1):
    x = point[0]
    y = point[1]
    k = ((3*pow(x, 2, p)+a) * pow(2*y, -1, p)) % p
    x3 = (pow(k, 2, p) - 2 * x) % p
    y3 = (k*(x-x3)-y) % p
    return x3, y3

def sum(point1, point2, p):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    k = ((y2-y1) * pow(x2 - x1, -1, p)) % p
    x = (pow(k, 2, p) - (x1 + x2)) % p
    y = (k * (x1 - x) - y1) % p
    return x, y

def decomp(k, x, y, p):
    powers = [(x, y)]
    bin_str = bin(k)[-1:1:-1]
    powlen = len(bin_str) - 1
    
    while(powlen > 0):
        powers.append(udv(powers[-1], p))
        powlen -= 1
    
    cur_pow = bin_str.find('1') + 1
    x, y, = powers[cur_pow - 1]
    for i in bin_str[cur_pow:]:
        if(i == '1'):
            x, y = sum((x, y), powers[cur_pow], p)
        cur_pow += 1
    return x, y

p1 = 55066263022277343669578718895168534326250603453777594175500187360389116729240
p2 =  32670510020758816978083085130507043184471273380659243275938904335757337482424
E = 115792089237316195423570985008687907853269984665640564039457584007908834671663

print(decomp(2023, p1, p2, E))
