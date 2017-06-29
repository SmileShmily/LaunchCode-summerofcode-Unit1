def get_initials(fullname):
   namelist = fullname.split()
   init = ""
   for aname in namelist:
       init = init + aname[0].upper()
   #print("The initials of ", fullname, " are", init)
   return init

get_initials("Ozzie Smith")
get_initials("bonnie blair")
get_initials("Daniel Day Lewis")