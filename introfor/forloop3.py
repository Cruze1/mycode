#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
print()

for x in farms:
    print(x)   # each time through the loop, this will print the KEY

print()

for x in farms:
	print(x.get("name")) # just display the value of "name", NOT the entire dict
print()
