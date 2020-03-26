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

# Output

def print_all():
    print("Enter a state or a country for a COVID-19 status: ", end="")
    user_i = input()
    user_i = user_i.upper()
    if user_i == str(-1):
        return False
    if user_i not in states and user_i not in country:
        user_i = user_i.title()
        if len(get_close_matches(user_i, od.keys())) > 0:
            guess = get_close_matches(user_i, od.keys())[0]
            print("In " + str(guess) + ", there are " + str(_cases(guess)) + " cases, " + str(_deaths(guess)) + " deaths, " + str(_active(guess)) + " active, and " + str(_new_cases(guess)) + " new cases today.")
        else:
            print("Couldn't find " + user_i)
    else:
        print("In " + user_i + ", there are " + str(_cases(user_i)) + " cases, " + str(_deaths(user_i)) + " deaths, " + str(_active(user_i)) + " active, and "
            + str(_new_cases(user_i)) + " new cases today.")


# while True:
#     print_all()
#     if print_all() == False:
#         break
