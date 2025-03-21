
with open("text.txt","w") as f:
    f.write("hello world")
    f.close()


try:
    with open("text.txt","r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)

finally:
    print("close db connection")

    







#with statement
#expection handeling
#managing file resources i.e. read/write




