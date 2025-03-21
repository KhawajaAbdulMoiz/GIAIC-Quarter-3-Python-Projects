def count(a:str):
    vowels = 'aeiouAEIOU'
    counter = 0
    for char in a:
        if(char in vowels):
            counter+=1
    return counter

a= "khawajaabdulmoiz"
result=count(a)
print(f"The Number of Vowels in {a} is {result}")