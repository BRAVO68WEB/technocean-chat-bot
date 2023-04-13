# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Dict, Text, Any, List, Union, Optional
from datetime import datetime
import requests
import yaml
from yaml.loader import SafeLoader

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action

api_base_url = "https://api.technocean.live"

# Load data
with open('event.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)

def time_convert(str):
 return datetime.fromisoformat(str).strftime("%d %B, %Y, %I:%M%p")

class EventDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_details"

 def run(self,dispatcher,tracker,domain):
  
  dispatcher.utter_message(response="utter_event_details")
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []

class EventVenue(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_venue"

 def run(self,dispatcher,tracker,domain):
  
  text = "{} takes place in {}".format(data.get("name"), data.get("venue"))
  
  dispatcher.utter_message(text=text)
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []

class EventSchedule(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_schedule"

 def run(self,dispatcher,tracker,domain):
  
  text = "The event runs from {}".format(data.get("date"))
  
  dispatcher.utter_message(text=text)
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []

class SpeakersList(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakers_list"

 def run(self,dispatcher,tracker,domain):
  text = "Below is the list of the speakers. Select a speaker to view more detals"
  btn_opt = []
  speakers = []
  url = "{}/speakers".format(api_base_url)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   speakers = res_json.get('data')
  for i, speaker in enumerate(speakers):
    speak = {
                "type": "postback",
                "payload": '/speaker_details{"speaker_id":"'+speaker.get('id')+'"}',
                "title": "{}. {}".format(i+1, speaker.get('name'))
            }
    btn_opt.append(speak)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []

class SessionsList(Action):
 def name(self):
  """name of the custom action"""
  return "action_sessions_list"

 def run(self,dispatcher,tracker,domain):
  text = "Below is the list of the events. Select an event to view more detals"
  btn_opt = []
  sessions = []
  url = "{}/events".format(api_base_url)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   sessions = res_json.get('data')
  for i, session in enumerate(sessions):
    sess = {
                "type": "postback",
                "payload": '/session_details{"session_id":"'+session.get('id')+'"}',
                "title": "{}. {}".format(i+1, session.get('name'))
            }
    btn_opt.append(sess)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []
 
class HackathonsList(Action):
 def name(self):
  """name of the custom action"""
  return "action_hackathons_list"

 def run(self,dispatcher,tracker,domain):
  text = "Below is the list of the hackathons. Select a hackathon to view more detals"
  btn_opt = []
  hackathons = []
  url = "{}/hackathons".format(api_base_url)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   hackathons = res_json.get('data').get('hackathons')
  for i, hackathon in enumerate(hackathons):
    hack = {
                "type": "postback",
                "payload": '/hackathon_details{"hackathon_id":"'+hackathon.get('id')+'"}',
                "title": "{}. {}".format(i+1, hackathon.get('name'))
            }
    btn_opt.append(hack)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []
 
class SpeakerDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_details"

 def run(self,dispatcher,tracker,domain):
  speaker_id = tracker.get_slot("speaker_id")
  url = "{}/speakers/{}".format(api_base_url, speaker_id)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   speaker = res_json.get('data')
  text = "Name: {}\nBio: {}\nLinkedin: {}\nWebsite: {}".format(speaker.get('name'), speaker.get('bio'), speaker.get('socials').get('linkedin'), speaker.get('socials').get('websitte'))
  dispatcher.utter_message(text=text, image=speaker.get('profile_pic'))
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []

class SessionDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_details"

 def run(self,dispatcher,tracker,domain):
  session_id = tracker.get_slot("session_id")
  url = "{}/events/{}".format(api_base_url, session_id)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   session = res_json.get('data')
  text = "Title: {}\nVenue: {}\nStarts: {}\nEnds: {}\nParticipants: {}\nRegistration Fee (R): {}\n{}".format(session.get('name'), session.get('schedules')[0].get('location').get('address'), time_convert(session.get('schedules')[0].get('starts_at')), time_convert(session.get('schedules')[0].get('ends_at')), session.get('participations_aggregate').get('aggregate').get('count'), session.get('price'), session.get('description').get('info'))

  btn_opt = []

  for i, speaker in enumerate(session.get('event_speakers')):
    speak = {
                "type": "postback",
                "payload": '/speaker_details{"speaker_id":"'+speaker.get('speaker').get('id')+'"}',
                "title": "{}. {}".format(i+1, speaker.get('speaker').get('name'))
            }
    btn_opt.append(speak)

  dispatcher.utter_message(text=text, image=session.get('banner_url'))
  
  if not len(session.get('event_speakers')):
   dispatcher.utter_message(response="utter_ask_whatelse")
  else:
   dispatcher.utter_message(text="View Speakers info", buttons=btn_opt)
  return []

class HackatonDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_hackathon_details"

 def run(self,dispatcher,tracker,domain):
  hackathon_id = tracker.get_slot("hackathon_id")
  url = "{}/hackathons/{}".format(api_base_url, hackathon_id)
  response = requests.get(url)
  res_json = response.json()
  if not res_json.get('error'):
   hackathon = res_json.get('data')
  text = "Name: {}\nVenue: {}\nStarts: {}\nEnds: {}\n{}".format(hackathon.get('name'), hackathon.get('schedules')[0].get('location').get('address'), time_convert(hackathon.get('schedules')[0].get('starts_at')), time_convert(hackathon.get('schedules')[0].get('ends_at')), hackathon.get('description').get('info'))


  dispatcher.utter_message(text=text, image=hackathon.get('banner_url'))
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []
