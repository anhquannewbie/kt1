"""
Lớp:D19CQAT01-N
MSSV:N19DCAT064
Họ và tên:ĐẶNG ANH QUÂN
Nhóm TH:02
Bài C.3: Cho một tệp văn bản tiếng Anh, hãy viết chương trình đếm: 
- Tổng số từ trong sách 
- Số lần mỗi từ được sử dụng. 
- Số lượng các từ khác nhau được sử dụng
"""

from re import *
with open('words.txt', encoding='utf8') as f:
    lines = f.readlines()
words = []
for line in lines: 
    words.extend(line.split())

numberWords = dict()
s=0
regex = '[^A-Za-z,.]+'
for word in words:
    word = sub(regex,'',word)

    if numberWords.get(word) == None:
        numberWords[word] = 1
    else:
        numberWords[word] = numberWords[word] + 1

for word in numberWords.keys():
    print(word, numberWords.get(word))
    s+=numberWords.get(word)


print("Number of words: ",s)
print("non-duplicate words: ",len(numberWords));

