
while True:
    your_greeting=input('Type your greeting : ').lower()

    if your_greeting  == 'hello':
       print('$0')
    elif your_greeting[0] == "h" and your_greeting != "hello" :
       print('$20')
    else:
       print('$100')
