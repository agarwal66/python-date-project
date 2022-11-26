import datetime
#input dob
dob=input("Enter your Date of Birth in DD/MM/YYYY format: ")
#inpur current date
cr=input("Enter Current date in DD/MM/YYYY format: ")

#traversing string for date month and year
dob_date=int(dob[0:2])
dob_month=int(dob[3:5])
dob_year=int(dob[6:])
cr_date=int(cr[0:2])
cr_month=int(cr[3:5])
cr_year=int(cr[6:])


#using date time module
DOB=datetime.date(dob_year,dob_month,dob_date)
CR=datetime.date(cr_year,cr_month,cr_date)

#findiing days and time lived
DaysNdTime=CR-DOB

#changing datatype for modification
days_str=str(DaysNdTime)

#removing time
Days_only=days_str.replace(", 0:00:00","")

#returning number of days lived
print("Congratulations you have survived in ṭhe world for",Days_only)
