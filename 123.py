try:
    with open('H:\\python\\test123.txt', 'w') as f:
        f.write('hello')
    print('successful!')
except Exception as e:
    print(f'error type: {type(e).__name__}')
    print(f'error details: {e}')