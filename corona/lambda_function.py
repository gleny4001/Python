
from __future__ import print_function
from botocore.vendored import requests
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
par(states, "state", parsed1)
par(deaths_states, "deaths", parsed1)
par(active_states, "active", parsed1)
par(new_cases_states, "todayCases", parsed1)
# countries
par(cases_country, "cases", parsed2)
par(country, "country", parsed2)
par(deaths_country, "deaths", parsed2)
par(active_country, "active", parsed2)
par(new_cases_country, "todayCases", parsed2)

# List to dictionary {cases:deaths}
dct = {x: {"cases": y, "deaths": z, "active": q, "todayCases": p} for x, y, z, q, p in
       zip(states, cases_states, deaths_states, recovered_states, active_states, new_cases_states)}
dct1 = {x: {"cases": y, "deaths": z, "active": q, "todayCases": p} for x, y, z, q, p in
        zip(country, cases_country, deaths_country, active_country, new_cases_country)}

# Merge two dictionaries
dct.update(dct1)

# Sorting the data
od = collections.OrderedDict(sorted(dct.items()))


# Extract individual datas
def _cases(input):
    return od.get(input, {}).get("cases")


def _deaths(input):
    return od.get(input, {}).get("deaths")


def _recovered(input):
    return od.get(input, {}).get("recovered")


def _active(input):
    return od.get(input, {}).get("active")


def _new_cases(input):
    return od.get(input, {}).get("todayCases")


# Output
def print_all(input):
    input = input.upper()
    if input not in states and input not in country:
        input = input.title()
        if len(get_close_matches(input, od.keys())) > 0:
            guess = get_close_matches(input, od.keys())[0]
            return ("In " + str(guess) + ", there are " + str(_cases(guess)) + " cases, " + str(
                _deaths(guess)) + " deaths, " + str(_active(guess)) + " active, and "
                    + str(_new_cases(guess)) + " new cases today.")
        else:
            return "Couldn't find " + input
    else:
        return ("In " + input + ", there are " + str(_cases(input)) + " cases, " + str(
            _deaths(input)) + " deaths, " + str(_active(input)) + " active, and"
                + str(_new_cases(input)) + " new cases today.")


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_state_status_response(intent):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """

    session_attributes = {}
    card_title = "United States"
    speech_output = print_all(intent['slots']['state']['value'])
    reprompt_text = print_all(intent['slots']['state']['value'])
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_country_status_response(intent):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """

    session_attributes = {}
    card_title = "International"
    speech_output = print_all(intent['slots']['country']['value'])
    reprompt_text = print_all(intent['slots']['country']['value'])
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "COVID-19 statistics"
    speech_output = "Say a country or a state to check latest COVID19 status"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Say a country or a state to check latest covid ninteen status"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Stay healthy"
    speech_output = "To prevent virus, remeber to wash your hands, cough into your elbow, don't touch your face, stay home if you can!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "StateStatus":
        return get_state_status_response(intent)
    elif intent_name == "CountryStatus":
        return get_country_status_response(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])