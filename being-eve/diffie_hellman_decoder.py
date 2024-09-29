def main():
    for i in range(-97,97):
        if 53 == (7**i) % 97:
            print("X = " + str(i))
            print("Shared secret = " + str((82**i)%97))
main()

