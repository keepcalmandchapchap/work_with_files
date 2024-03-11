with open('1.txt', encoding='utf-8') as f1:
    text1 = f1.read()
with open('2.txt', encoding='utf-8') as f2:
    text2 = f2.read()
with open('3.txt', encoding='utf-8') as f3:
    text3 = f3.read()

def count_line_length(text):
    return len(text.split('\n')) 

main_dict = {
    '1':{'file_name': '1.txt', 'text': text1},
    '2':{'file_name': '2.txt', 'text': text2},
    '3':{'file_name': '3.txt', 'text': text3}
            }
lengthes_list = []

for i in main_dict.values():
    i['length'] = count_line_length(i['text'])
    lengthes_list.append(i['length'])

lengthes_list.sort()

def create_text():
    text_list = []
    position = 0
    for length in lengthes_list:
        for v in main_dict.values():
            if length == v['length']:
                position += 1
                text_list.append(v['file_name'])
                text_list.append(str(position))
                text_list.append(v['text'])
    return '\n'.join(text_list)

full_text = create_text()

with open('sorted_text.txt', 'w', encoding='utf-8') as f4:
    f4.write(full_text)


