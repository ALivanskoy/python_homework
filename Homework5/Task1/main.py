# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data = open('text.txt', 'r', encoding = "utf-8")
input_text = data.read()
print(f"\nОригинальный текст:\n{input_text}")
input_text = input_text.split('\n')
data.close()

output_text = []
for i in input_text:
    if 'абв' not in i.lower():
        output_text.append(i)

output_text = '\n'.join(output_text)

print(f"\nОтредактированный текст:\n{output_text}")