from tkinter import *
import requests
import json
import collections
from difflib import get_close_matches

response_states = requests.get("https://corona.lmao.ninja/states")
response_country = requests.get('https://coronavirus-19-api.herokuapp.com/countries')

# Extract data to json obj
data1 = response_states.text
data2 = response_country.text
parsed1 = json.loads(data1)
parsed2 = json.loads(data2)

# Json object to list
states = []
cases_states = []
deaths_states = []
active_states = []
new_cases_states = []

country = []
cases_country = []
deaths_country = []
active_country = []
new_cases_country = []


# Putting items in lists
def par(list, inst, parsed):
    for item in parsed:
        list.append(item[inst])


# states
par(cases_states, "cases", parsed1)
par(states, "state",parsed1)
par(deaths_states, "deaths",parsed1)
par(active_states, "active",parsed1)
par(new_cases_states,"todayCases", parsed1)
# countries
par(cases_country, "cases",parsed2)
par(country, "country",parsed2)
par(deaths_country, "deaths",parsed2)
par(active_country, "active",parsed2)
par(new_cases_country,"todayCases", parsed2)
# List to dictionary {cases:deaths}
dct = {x: {"cases": y, "deaths": z, "active": q, "todayCases": p} for x, y, z, q, p in
       zip(states, cases_states, deaths_states, active_states, new_cases_states)}
dct1 = {x: {"cases": y, "deaths": z, "active": q, "todayCases": p} for x, y, z, q, p in
        zip(country, cases_country, deaths_country, active_country, new_cases_country)}

# Merge two dictionaries
dct.update(dct1)

# Sorting the data
global od
od = collections.OrderedDict(sorted(dct.items()))


# for key, value in od.items():print(key, value)


# Extract individual datas
def _cases(input):
    return od.get(input, {}).get("cases")


def _deaths(input):
    return od.get(input, {}).get("deaths")



def _active(input):
    return od.get(input, {}).get("active")


def _new_cases(input):
    return od.get(input, {}).get("todayCases")


def status_all():
    print(e1_value.get())
    region = e1_value.get().upper()
    if region == str(-1):
        return False
    if region not in states and  region not in country:
        region = region.title()
        if len(get_close_matches(region, od.keys())) > 0:
            guess = get_close_matches(region, od.keys())[0]
            t1.delete(1.0, END)
            t1.insert(END, "In " + str(guess) + ", there are " + str(_cases(guess)) + " cases, " + str(
                _deaths(guess)) + " deaths, " + str(_active(guess)) + " active, and " + str(
                _new_cases(guess)) + " new cases today.")
        else:
            t1.delete(1.0, END)
            t1.insert(END, "Couldn't find " +  region)
    else:
        t1.delete(1.0, END)
        t1.insert(END, "In " + region + ", there are " + str(_cases(region)) + " cases, " + str(
            _deaths(region)) + " deaths, " + str(_active(region)) + " active, and "
              + str(_new_cases(region)) + " new cases today.")



window = Tk()
window.title("COVID-19 status")
b1 = Button(window, text="Enter",command=status_all)
b1.grid(row = 2, column = 1)

e1_value=StringVar()
e1 =Entry(window,textvariable=e1_value)
e1.grid(row=2, column =0)

t1=Text(window,height=5, width=30)
t1.grid(row=0,column =0)
window.mainloop()