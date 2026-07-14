def check_grade(nomre) :
    if nomre > 20 :
       return 'out of range'
    elif nomre < 0 :
        return 'out of range'
    elif nomre >= 18 :
        return 'aali'
    elif nomre >=14 and nomre <18 :
        return 'khob'
    elif nomre >=10 and nomre <14 :
        return 'ghabool'
    else :
        return 'mardood'
result = check_grade(23)
print(result)