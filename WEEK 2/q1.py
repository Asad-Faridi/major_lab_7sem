class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print("car brand is :",self.make)
        print("car model is:",self.model)
        print("car is manufactured in year:",self.year)
c1=Car("toyota","camry",2020)
c1.display_info()
c2=Car("honda","civic",2022)
c2.display_info()