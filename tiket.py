sen = int(input('sen ra beh :'))
if sen<0 :
    print('out of')
elif sen <5 and sen>=0:
    print('tiket kodak =rayegan')
elif sen >=5 and sen <=12 :
    print ('tiket kodak =50000 toman')
elif sen >12 and sen<=18 :
    print ('tiket nojavan =80000 toman')
elif sen>18 and sen<=65 :
    print ('tiket bozorgsal =120000 toman')
else :
    print('tiket salmand =60000 toman')
