# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_coding(input_list):
    output_list = []
    count = 0
    for i in range(len(input_list)):
        if input_list[i] != input_list[i-1] and i != 0:
            output_list.append((input_list[i-1], count))
            count = 1
        elif i == len(input_list) - 1:
            count += 1
            output_list.append((input_list[i], count))
        else:
            count += 1
    return output_list


def rle_decoding (input_list):
    output_list = ""
    for i in input_list:
        output_list += i[0]*i[1]
    return output_list


with open("input.txt", "r") as data:
    text = data.read()

print(f"Первичный текст:\n{text}\n")

text = rle_coding(text)
print(f"RLE-кодированный текст:\n{text}\n")
with open("rle_coding.txt", "w") as data:
     data.write(str(text))

text = rle_decoding(text)
print(f"RLE-декодированный текст:\n{text}\n")
with open("rle_decoding.txt", "w") as data:
    data.write(text)