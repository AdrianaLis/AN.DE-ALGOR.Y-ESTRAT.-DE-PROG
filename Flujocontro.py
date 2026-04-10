name = 'Antony'

if name == 'Debora':
   print('Hi Debora!')
elif name == 'George':
   print('Hi George!')
else:
   print('Who are you?')


   spam = 0
while spam < 5:  # Continue while spam is less  than 5
    print('Hello, world.')
    spam = spam + 1  # Increment counter to avoid infinite loop

    for i in range(5):
       print(f'Will stop at 5! or 4? ({i})')
       