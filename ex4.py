#learning python the hard way
#ex4.py

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#avg_p_p_c = car_pool_capacity / passengers  # the car_pool_capacity variable does not exist.. or does not have a value assigned to the variable
#avg = carpool_capacity / passengers
#print avg

print "There are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."






