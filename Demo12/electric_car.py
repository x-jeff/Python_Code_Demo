class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        self.make=make#汽车品牌
        self.model=model#汽车型号
        self.year=year#生产年份
        self.odometer_reading=0#里程数

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''

    def __init__(self,battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a "+str(self.battery_size)+"-kWh battery.")


class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery=Battery()

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()