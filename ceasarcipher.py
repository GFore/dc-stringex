task = input("e to Encrypt or d to Decrypt: ")
str = input("\nInput string: ").lower()
rot = int(input("Shift amount: "))
if task == 'd': rot = 0 - rot
alpha = 'abcdefghijklmnopqrstuvwxyz'
c_str = ''

for i in str:
    if i in alpha:                  # only encrypt/decrypt letters
        x = alpha.find(i)           # translate the letter to a number 0 - 25, where a=0, b=1, ...

        e = (x + rot) % 26          # formula for encryption letter shift, e is the shifted number

        c_str += alpha[e]           # convert the shifted number back to a letter and concatenate it to the new str

    else:                          # not a letter so leave as-is
        c_str += i

print("\n%s version:" % ('Encrypted' if task == 'e' else 'Decrypted'), c_str, '\n')




# lbh zhfg hayrnea jung lbh unir yrnearq
# you must unlearn what you have learned