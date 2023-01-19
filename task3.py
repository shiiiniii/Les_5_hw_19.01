#№3 
# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и 
# восстановления данных.
# Входные и выходные данные хранятся в отдельных 
# текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

line = 'aaaaabbbcccc'
count = 0
for i in range(len(line) - 1):
    if i <= len(line):
        if line[i] == line[i + 1]:
            count += 1
        else:
            a = line[i]
            print(count, line[i], sep= '', end='')
            count = 1
print(count, line[i], sep= '', end='')
