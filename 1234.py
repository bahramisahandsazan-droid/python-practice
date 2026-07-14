try:
    with open('students.json', 'w') as f:
        f.write('test')
    print('successful!')
except Exception as e:
    print(f'error type: {type(e).__name__}')
    print(f'error details: {e}')