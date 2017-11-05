print("Enter the text to be tested in your file sample.txt")
text=input()
with open("sample.txt",'a') as f:
    f.write(text+'\n')
print("Here is the text you wrote in the file sample.txt")
with open("sample.txt",'r') as f:
    for line in f:
        print(line)
    print("Enter the letter to be counted")
    ip=input()
    f.seek(0)
    cnt=0
    for line in f:
        for letter in line:
            if letter==ip:
                cnt+=1
    print(cnt)