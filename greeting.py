import datetime

hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning, sir"
elif hour < 18:
    greeting = "Good afternoon, sir"
else:
    greeting = "Good evening, sir"

print(greeting)
 