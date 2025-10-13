word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()

# word = list(input() + ' запретил букву')
# alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#
# for i in alph:
#     if i in word:
#         s = "".join(word).strip()
#         s = s.replace('  ', ' ')
#         print(s, i)
#         while i in word:
#             word.remove(i)