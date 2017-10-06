'''
madlibs
'''

farm_animal = input('Name a farm animal.')
adjective_1 = input('Give me an adjective.')
relative = input('Name a relative.')
food = input('Name a food item.')
day = input('Choose a day of the week.')
time_of_day = input('Choose a time of day.')


reply1 = f"\nThe {farm_animal} is having a {adjective_1} birthday party."
reply2 = f"Please invite your {relative}, I think they will enjoy the {food}."
reply3 = f"The party will be on {day} at {time_of_day}."

print(reply1, reply2, reply3)

