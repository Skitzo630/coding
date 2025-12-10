def lettergrade():
    numbergrade=int(input())
    print(int(numbergrade)) 
    if numbergrade > 60 and numbergrade <69:
        print('your grade is a f')
    elif numbergrade > 70 and numbergrade < 79:
        print ('your grade is a c')
    elif numbergrade > 80 and numbergrade <89: 
        print ('your grade is a b') 
    elif numbergrade > 90 and numbergrade < 100:
         print('your grade is a A ')
lettergrade()