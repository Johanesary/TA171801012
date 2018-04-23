import os
data=[]
flag=False
with open('D:/FTP/speech/output.txt','r') as f:
    for line in f:
        if line.startswith('sentence1:'):
            flag=True
        if flag:
            data.append(line)
        if line.strip().endswith('</s>'):
            flag=False
text = str(''.join(data))
panjangpesan = len(text) - 6
m = text[15:panjangpesan]
print(m)