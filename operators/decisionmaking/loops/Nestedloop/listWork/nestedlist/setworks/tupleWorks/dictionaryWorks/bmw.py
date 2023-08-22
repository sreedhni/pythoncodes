variable=["Bus", "car", {"Bus":["car", "bus", {"car":"bus", "Car":["bus", "car", ["BMW"]],},"Bus"]},"Bus"]
# print BMW as a string output
# for m in variable:
m=(variable[2].get("Bus"))
# k=m.get("Bus")
j=m[2].get("Car")
# l=j.get("Car")
t=j[2]
print(t[0])