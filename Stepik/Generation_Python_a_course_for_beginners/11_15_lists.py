#В операционной системе Windows полное имя файла состоит из буквы диска, после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
# put your python code here
lst = input()
wrd = lst.split('\\')
print(*wrd, sep = '\n')   