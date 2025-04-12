answer = "YES"
while answer=="YES":
    sentence=str(input("\n\nType any sentence, paragraph or essay and i will tell you its word count : "))
    arr=sentence.split()
    
    print("\nWord count is : ",len(arr))

    choice=str(input("\nDo you want to continue : "))
    answer=choice.upper()
