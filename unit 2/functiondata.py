# How to create function with data 
 
# step one. function defintion 
def bnbrefund(accountnumber, refundamount): 
         print ( 'account number:' +str (accountnumber)) 
         print ('refund amount: $ '+ str (refundamount))
            
# step 2 function call (invaction) 
bnbrefund(630303030, 4000) #arguement  are real data 
 
def name_Birthday( name , Birthday): 
         print('my name is ' + name + 'my Birthday is' + Birthday)

name_Birthday('skitzo ', 'june 30') 
 
 # create a function that will convert dollars into pennies 
 # your function should take the dollar amount in as a parameter 
 # and calculate how manny pennies are in that dollar amount 
 # your function should print out the follwing message: 

  # My {13}dollars(s) is equal to {1300} pennies  
   
def dollarconverter(dollar): 
         pennies = dollar * 100 
         print ('my'+ str(dollar) + 's is equal to '+str(pennies)+'pennies ')
           
dollarconverter(630)