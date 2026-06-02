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


'''
Methods: 
    - Object/Instance method
    - Class method
    - Static method
'''
'''Using the Object/Instance Methods:e'''
class Car:
    name = "CAR"
    version = 1.0

    def __init__(self, engine, base_speed, max_speed):
        self.engine = engine
        self.base_speed = base_speed
        self.max_speed = max_speed

    def info(self):
        print("Engine:", self.engine)
        print("Base.speed:", self.base_speed)
        print("Max_speed:", self.max_speed)

    @classmethod
    def class_version(cls, new_version):
        cls.version = new_version

    @classmethod
    def props(cls) :
        print('Name:', cls.name)
        print('Version:', cls.version)

    def update_engine_type(self, new_engine_type):
        self.engine = new_engine_type

    def update_base_speed(self, new_base_speed):
        self.base_speed = new_base_speed
    
    def update_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed

tata = Car("EV", "60Kmph", "180Kmph")
print("Before update:")
print('Name:', tata.name)
print('Version:', tata.version)
tata.info()
print()
print("After update:")
tata.update_engine_type("Petrol")
tata.update_base_speed("80kmph")
tata.update_max_speed("160kmph")
tata.info()
# lambrogini = Car("petrol engine", "120Kmph", "380Kmph")
# lambrogini.info()