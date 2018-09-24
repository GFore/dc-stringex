str = input("Enter String: ").upper()
leetstr = '4361057'
pos = 0
for i in 'AEGIOST':
    str = str.replace(i, leetstr[pos])
    pos += 1

print("Leetspeak version:", str)
