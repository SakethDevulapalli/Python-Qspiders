# class Building :
#     no_of_floors = 4
#     height_of_floor = 3
#     width_of_floor = 25
#     no_of_rooms = 7

# elite_arcade = Building()
# '''
# How to access the properties of an objects?
# object_name.property
# '''

# print(elite_arcade.height_of_floor)
# print(Building.no_of_floors)


# class Car() :
#     pass

# tata = Car()
# tata.wheelers = 4
# tata.gears = 6
# tata.engine = "2cylinder - petrol engine"
# tata.base_speed = "60kmph"
# tata.max_speed = "120kmph"

# print("tata.wheelers:", tata.wheelers)
# print("tata.gears:", tata.gears)
# print("tata.engine:", tata.engine)
# print("tata.base_speed:", tata.base_speed)
# print("tata.max_speed:", tata.max_speed)



# class Car:
#     wheelers = 4
#     gears = 6
#     base_speed = '60kmph'
#     max_speed = '120kmph'

# tata = Car()
# tata.safety = '*****'
# print('Tata properties: ')
# print('tata.wheelers:', tata.wheelers)
# print('tata.gears:', tata.gears)
# print('tata.base_speed:', tata.base_speed)
# print('tata.max_speed:', tata.max_speed)
# print('tata.safety:', tata.safety)
# print()

# mahindra = Car()
# mahindra.safety = "****"
# print('Mahindra properties: ')
# print('mahindra.wheelers:', mahindra.wheelers)
# print('mahindra.gears:', mahindra.gears)
# print('mahindra.base_speed:', mahindra.base_speed)
# print('mahindra.max_speed:', mahindra.max_speed)
# print('mahindra.safety:', mahindra.safety)
# print()

# toyota = Car()
# print('Toyota properties: ')
# print('toyota.wheelers:', toyota.wheelers)
# print('toyota.gears:', toyota.gears)
# print('toyota.base_speed:', toyota.base_speed)
# print('toyota.max_speed:', toyota.max_speed)
# print()

class Car:
    def __init__(self, wheelers, gears, base_speed, max_speed):
        self.wheelers = wheelers
        self.gears = gears
        self.base_speed = base_speed
        self.max_speed = max_speed

tata = Car(4, 6, "60Kmph", "180Kmph")
print("tata.wheelers:", tata.wheelers)
print("tata.gears:", tata.gears)
print("tata.base_speed:", tata.base_speed)
print("tata.max_speed:", tata.max_speed)