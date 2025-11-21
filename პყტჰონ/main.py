a = int(input("კათეტის სიგრძე"))
b = int(input("კათეტის სიგრძე"))
c = (a**2 + b**2) **0.5
s = (a*b) / 2

print("ჰიპოტენუზა:", c)
print("ფართობი:", s)

seconds = int(input("წამების რაოდენობა:"))
hours = seconds // 3600
balance = seconds % 3600
minute = balance // 60
seconds_secend = balance % 60
print(hours, 'საათი', minute, 'წუთი',seconds_secend, 'წამი' )