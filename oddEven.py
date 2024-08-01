try:
    x=int(input('Enter the numbber to check odd or even: '))
    if (x%2)==0:
        print("Even number")
    else:
        print('Odd number')
except:
    print('Floating Point Number')