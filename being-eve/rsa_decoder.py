import math
import bytes

def isPrime(num):
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True 


def prime_generator(max):
    primes = []
    for i in range(2,max):
        if isPrime(i):
            primes.append(i)
    return primes

def main():
    e_Bob, n_Bob = 13, 162991

    ciphertext = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096, 
                128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
                80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
                59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
                13649, 120780, 133707, 66992, 128221]

    #find all prime numbers up to n_Bob//2
    primes = prime_generator(n_Bob//2)


    #Find all pairs of p and q where pq = n_Bob and both p and q are prime
    potential_pairs = []
    for i in primes:
        if n_Bob % i == 0 and n_Bob/i in primes and i <= math.ceil(math.sqrt(n_Bob)):
            potential_pairs.append((i,int(n_Bob/i)))

    print("Potential pairs = " + str(len(potential_pairs))) #Insecure bc there's only one pair of p and q??

    for pair in potential_pairs:
        lamb_n = math.lcm(pair[0]-1,pair[1]-1)
        d_Bob = -1
        for i in range(1,1000000):
            if (e_Bob*i)%lamb_n == 1: 
                d_Bob = i
                break
        
        print("lambda(n) = " + str(lamb_n))
        print("d_Bob = "+ str(d_Bob))

        plaintext = ""
        for cipherchar in ciphertext:
            encoded = (cipherchar**d_Bob)%n_Bob

            #String manipulation so it has the right format for the int and chr functions
            encoded1 = str(hex(encoded))[:4]
            encoded2 = "0x" + str(hex(encoded))[4:]

            plaintext += chr(int(encoded1,16)) + chr(int(encoded2,16))
        
        print(plaintext)

main()

# hex_values = [0x4465, 0x6172, 0x2042, 0x6f62, 0x2c20, 0x6368, 0x6563, 0x6b20, 0x7468, 0x6973, 0x206f, 0x7574, 0x2e20, 0x6874, 0x7470, 0x733a, 0x2f2f, 0x7777, 0x772e, 0x7375, 0x7276, 0x6569, 0x6c6c, 0x616e, 0x6365, 0x7761, 0x7463, 0x682e, 0x696f, 0x2f20, 0x5365, 0x6520, 0x7961, 0x2c20, 0x416c, 0x6963, 0x652e]
# for i in hex_values:
#     print(chr(i))
