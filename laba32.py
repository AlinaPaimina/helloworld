text = ''
b = ''
while True:
    text = input()
    if 'стоп' in text:
        break
    b = str(b) + ' ' + str(text)
print(b)

