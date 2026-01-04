# take a list of nums and return even nums

def even_num(liss):
    result = [i for i in liss if i %2 ==0]
    return(result)

nums = [1,2,3,4,5,6,7,8,9,10]

print(even_num(nums))

# assign values into dictonary and print them with x,y

def dic_ele(di):
    for x,y in di.items():
        print(x,y)

dicc = {"name":"bhargav",'age':27}

dic_ele(dicc)

# create a file write content in that and also read it 

file = open("D:\Passion\coding-daily\summary.txt",'w')

file.write("today its sunday, i want to ace this AI at any cost")
file.writelines(["\n one \n", "two \n","three \n"])
file.close()
print("file is created")

file1 = open("D:\Passion\coding-daily\summary.txt",'r')
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
file1.close()

