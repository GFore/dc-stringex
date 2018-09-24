str = input("\nEnter a Leetspeak String: ")
unleetstr = 'AEGIOST'
pos = 0
for i in '4361057':
    str = str.replace(i, unleetstr[pos])
    pos += 1

print("Normal version:", str, '\n')
