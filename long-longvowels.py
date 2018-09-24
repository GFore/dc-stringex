str = input("\nEnter a Word: ")

newvowels = ['aaaaa', 'eeeee', 'iiiii', 'ooooo', 'uuuuuu']
pos = 0
for v in ['aa', 'ee', 'ii', 'oo', 'uu']:
    str = str.replace(v, newvowels[pos])
    pos += 1

print("Long-long Vowels version:", str, '\n')