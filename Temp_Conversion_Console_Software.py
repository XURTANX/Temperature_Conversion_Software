# -*- coding: utf-8 -*-

class TemperatureConversionClass(object):
    def __init__(self , Choice):
        self.Choice = Choice
        while True:
            Degree = int(input('Enter the value to convert : '))
            if self.Choice == 'CF':
                print('{} F' , self.celsius_to_fahrenheit(Degree))
                break
            elif self.Choice == 'CK':
                print('{} K' , self.celsius_to_kelvin(Degree))
                break
            elif self.Choice == 'FC':
                print('{} C' , self.fahrenheit_to_celsius(Degree))
                break
            elif self.Choice == 'FK':
                print('{} K' , self.fahrenheit_to_kelvin(Degree))
                break
            elif self.Choice == 'KC':
                print('{} C' , self.kelvin_to_celsius(Degree))
                break
            elif self.Choice == 'KF':
                print('{} F' , kelvin_to_fahrenheit(Degree))
                break


    def celsius_to_fahrenheit(self , Value):
        self.Value = Value
        return (self.Value * 9 / 5) + 32

    def fahrenheit_to_celsius(self , Value):
        self.Value = Value
        return (self.Value - 32) * 5 / 9

    def kelvin_to_celsius(self , Value):
        self.Value = Value
        return self.Value - 273.15

    def celsius_to_kelvin(self , Value):
        self.Value = Value
        return self.Value + 273.15
    
    def kelvin_to_fahrenheit(self , Value):
        self.Value = Value
        return (self.Value - 273.15) * 9 / 5 + 32

    def fahrenheit_to_kelvin(self , Value):
        self.Value = Value
        return (self.Value - 32) * 5 / 9 + 273.15

if __name__ == "__main__":
    Options = ['CF' , 'CK' , 'FC' , 'FK' , 'KC' , 'KF']
    print('Enter [CF] Celsius to Fahrenheit[CK] for Celsius to Kelvin , [FC] for Fahrenheit to Celsius , [FK] for Fahrenheit to Kelvin , [KC] for Kelvin to Celsius , [KF] for Kelvin to Fahrenheit.')
    while True:
        Option = input('Enter your choice in uppercase lettes then hit enter : ')
        if Option in Options:
            TemperatureConversionClass(Option)
            break
