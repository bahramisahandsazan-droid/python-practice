def calculator (a,b,amal):
    if amal == '+':
        return(a+b)
    elif amal == '-' :
        return(a-b)
    elif amal == '*' :
        return(a*b)
    elif amal == '/' :
        if b == 0 :
            return' b no zeroo'
        else :    
           return(a/b)
    else :
        return('not corect')    
a=int(input('give me first number : '))
b=int(input('give me second number : '))
amal = input ('give me + or - or * or / : ')
                           
answer = calculator (a,b,amal)
print(answer)

