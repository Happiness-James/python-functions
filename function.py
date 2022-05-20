def multiple_and_greet(*numbers,**students):
    num= 1
    for x in numbers:
        num*= x
        print(num)
    print (f"Hello {students}")
           
        
