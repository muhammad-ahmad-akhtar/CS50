months = {
    "Janurary": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May": '05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
}
user_input = input("Date: ").strip().capitalize()

if '/' in user_input:
    month, day, year = user_input.split('/')
elif ' ' in user_input:
    month, day, year = user_input.split(' ')
    day = day.removesuffix(",")

if month.isalpha():
    if month in months:
        print(f"{year}-{months[month]}-{int(day):02}")
else:
    print(f"{year}-{int(month):02}-{int(day):02}")