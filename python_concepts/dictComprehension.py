#1.converting faranhiet to celcius, Formula:dictionary={key:expression for (key,value) in iterable}
temp_in_f={'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
temp_in_c={key:round((value-32)*(5/9)) for (key,value) in temp_in_f.items()}
print(temp_in_c)

#2.Conditional statements, Formula:dictionary={key:expression for (key,value) in iterable if conditional}
weather={'New York':'snowing','Boston':'sunny','Los Angeles':'sunny','Chicago':'cloudy'}
sunny_weather={key:value for (key,value) in weather.items() if value=='sunny'}
print(sunny_weather)

#3.If-else Statement, Formula:dictionary={key:(if/else) for (key,value) in iterable}
desc_cities={key:("WARM" if value>=40 else "COLDS") for (key,value) in temp_in_f.items()}
print(desc_cities)

#4.Calling function values, Formula:dictionary={key:function(value) for (key,value) in iterable}
def check_temp(value):
    if value>=70:
        return "HOT"
    elif 69>=value>=40:
        return "WARM"
    else:
        return "COLD"
describe_cities={key:check_temp(value) for (key,value) in temp_in_f.items()}
print(describe_cities)
