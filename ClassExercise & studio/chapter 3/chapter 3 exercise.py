#studio


#prompt user for exchange rate from dollars to pounds
exchange_rate=float(input("How many the exchange rate from dollars to pounds?"))

#prompt user for number of falgs to sell
num_flags=int(input("How many flags are you going to sell?"))
#fix values
pounds_per_pint=3.79
dollars_per_flag=3
#how many pounds to sell flags for
pounds_per_flag=dollars_per_flag*exchange_rate
print("pound per flag:",pounds_per_flag)

#how much we're gonna make(in pounds)
revenue=pounds_per_flag*num_flags
#print number pints
num_pints=int(revenue/pounds_per_pint)
print("You got",num_pints,"pints of REAL ale.")