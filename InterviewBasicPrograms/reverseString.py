string = "hello123python"
revString = ""
i = 0
lengthOfString = len(string)
for i in range(lengthOfString - 1, -1 ,-1):
    revString += string[i]
print(revString)
