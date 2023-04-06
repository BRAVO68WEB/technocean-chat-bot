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
import yaml
from yaml.loader import SafeLoader

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action

# Load data
with open('event.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)

class EventVenue(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_venue"

 def run(self,dispatcher,tracker,domain):
  
  text = "{} takes place in {}".format(data.get("name"), data.get("venue"))
  
  dispatcher.utter_message(text=text)
  return []

class EventSchedule(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_schedule"

 def run(self,dispatcher,tracker,domain):
  
  text = "The event runs from {}. Select a session to get its date and time".format(data.get("date"))
  btn_opt = []
  sessions = data.get('sessions')
  for session in sessions:
    sess = {
                "type": "postback",
                "payload": '/session_details{"session_id":"'+session.get('session_id')+'"}',
                "title": session.get('title')
            }
    btn_opt.append(sess)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []

class SpeakersList(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakers_list"

 def run(self,dispatcher,tracker,domain):
  text = "Below is the list of the speakers. Select a speaker to view more detals"
  btn_opt = []
  speakers = data.get('speakers')
  for speaker in speakers:
    speak = {
                "type": "postback",
                "payload": '/speaker_details{"speaker_id":"'+speaker.get('speaker_id')+'"}',
                "title": speaker.get('name')
            }
    btn_opt.append(speak)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []

class SessionsList(Action):
 def name(self):
  """name of the custom action"""
  return "action_sessions_list"

 def run(self,dispatcher,tracker,domain):
  text = "Below is the list of the sessions. Select a session to view more detals"
  btn_opt = []
  sessions = data.get('sessions')
  for session in sessions:
    sess = {
                "type": "postback",
                "payload": '/session_details{"session_id":"'+session.get('session_id')+'"}',
                "title": session.get('title')
            }
    btn_opt.append(sess)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []
 
class SpeakerDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_details"

 def run(self,dispatcher,tracker,domain):
  speaker_id = tracker.get_slot("speaker_id")
  speaker = next((item for item in data.get('speakers') if item["speaker_id"] == speaker_id), None)
  text = "Name: {}\nDesignation: {}\n{}".format(speaker.get('name'), speaker.get('designation'), speaker.get('details'))
  dispatcher.utter_message(text=text, image=speaker.get('img_url'))
  dispatcher.utter_message(response="utter_ask_whatelse")
  return []

class SessionDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_details"

 def run(self,dispatcher,tracker,domain):
  session_id = tracker.get_slot("session_id")
  session = next((item for item in data.get('sessions') if item["session_id"] == session_id), None)
  text = "Title: {}\nVenue: {}\nDate: {}\nTime: {}\nSpeaker: {}".format(session.get('title'), session.get('venue'), session.get('date'), session.get('time'), session.get('speaker'))
  speaker_id = session.get('speaker_id')
  btn_opt = [{
                "type": "postback",
                "payload": '/speaker_details{"speaker_id":"'+speaker_id+'"}',
                "title": "View Speaker Info"
            }]
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []
