letters = 'abcdefghijklmnopqrstuvwxyz'
enter_text = input('Введите что вы хотите зашифровать: ').lower()
key = int(input('Введите ключ для шифрации: '))
finished = ''

for i in enter_text:
	p = letters.find(i)
	p1 = p + key
	if i in letters:
		finished = finished + letters[p1]
	else:
		finished = finished + i

print(finished)