##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

my_email='kanigurav@gmail.com'
password='wjlijkklsszgdygx'

today=(dt.datetime.now().month,dt.datetime.now().day)
# print(today)

data=pd.read_csv('birthdays.csv')
# list_d=data.values.tolist()
birthdays_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in data.iterrows()}
# print(birthdays_dict)

if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as file_name:
        contents=file_name.read()
        contents=contents.replace("[NAME]",birthday_person['name'])
        contents=contents.replace("Angela","Kanishka")

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person['email'],msg=f"Subject:Happy Birthday!\n\n{contents}")



# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



