cars=100
space_in_a_car=4.0
drivers=24
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("there are cars",cars,"cars available.")
print("threr are only",drivers,"drivers available.")
print("there will be",cars_not_driven,"empty cars today.")
print("we can transport",carpool_capacity,"pepole today")
print("we have",passengers,"to carpool today.")
print("we need to put about",average_passengers_per_car,"in each cars.") 


'''sample output:
  
there are cars 100 cars available.
threr are only 24 drivers available.
there will be 76 empty cars today.
we can transport 96.0 pepole today
we have 90 to carpool today.
we need to put about 3.75 in each cars.'''
