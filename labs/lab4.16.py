'''4.16 LAB: Interstate highway numbers

Primary U.S. interstate highways are numbered 1-99. Odd numbers 
(like the 5 or 95) go north/south, and evens (like the 10 or 90) 
go east/west. Auxiliary highways are numbered 100-999, and service 
the primary highway indicated by the rightmost two digits. Thus, 
I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid 
auxiliary highway because 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary 
highway. If auxiliary, indicate what primary highway it serves. 
Also indicate if the (primary) highway runs north/south or east/west.
'''

highwayNumber = int(input())   

# filter out impossible highway numbers
if not((highwayNumber >= 1) and (highwayNumber <= 999)):
   print(f"{highwayNumber} is not a valid interstate highway number.")

# whoops, missed a few
elif highwayNumber % 100 == 0:
   print(f"{highwayNumber} is not a valid interstate highway number.")

else:
   # determine primary highway and even|odd
   primaryNumber = highwayNumber % 100
   evenOdd = primaryNumber % 2
      
   if highwayNumber > 100:
      # // auxiliary //
      print(f"I-{highwayNumber} is auxiliary, serving I-{primaryNumber}", end="")
      
   else: 
      # // primary //
      print(f"I-{highwayNumber} is primary", end="")
      
   # // even|odd :: N-S|E-w //
   if evenOdd == 1:   
        NESW="north/south."
   else:
        NESW="east/west."  
   print(", going " + NESW)
