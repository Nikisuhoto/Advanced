text = list(input())
#
# while text:
#     print(text.pop(), end='')

text_in_list = []

for i in range(len(text)):

    text_in_list.append(text.pop())

print(''.join(text_in_list))
