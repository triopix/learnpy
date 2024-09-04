# What is a dictionary?
# Collection of "values" that are stored using a "key"
# dicts store key-value pairs which are all unique

# define a dict entry by "{key}": "{value}"
vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R1100",
    "er5": "Kawasaki ER5",
    "can-am": "Bombardier Can-Am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT650",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
}

my_vehicle = vehicles['fiesta']
print(my_vehicle)

learner = vehicles.get("er5")
print(learner)
