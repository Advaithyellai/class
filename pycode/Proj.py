import random

b = 100
k = 3

print("The rating of the top 5 bowlers(top 5 rated as per the number of wickets secured)\nof the t20 world cup(2022) is as follows:\n")

def rating(input_dict):

    rate = input_dict['wickets']/input_dict['matches']+b/input_dict['average']+b/input_dict['economy']
    rate = round(k*rate, 1)

    print(input_dict['name'] + ":", rate, end="%\n")
    
    return rate

Wanindu = {"name": "Wanindu Hasaranga", "wickets": 15, "average": 13.26, "economy": 6.41, "matches": 8}
Sam = {"name": "Sam Curran", "wickets": 13, "average": 11.38, "economy": 6.52, "matches": 6}
Bas = {"name": "Bas de Leede", "wickets": 13, "average": 13, "economy": 7.68, "matches": 8}
Blessing = {"name": "Blessing Muzarabini", "wickets": 12, "average": 16.58, "economy": 7.65, "matches": 8}
Anrich = {"name": "Anrich Nortje", "wickets": 11, "average": 8.54, "economy": 5.37, "matches": 5}

j = []

for i in (Wanindu, Sam, Bas, Blessing, Anrich):
    rate = rating(i)
    j.append(rate)

print("\nThe range for the bowlers rating is:", max(j)-min(j))
