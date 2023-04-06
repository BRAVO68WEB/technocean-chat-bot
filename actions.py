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
  btn_opt = [
                {
                    "type": "postback",
                    "payload": "/speakers_list",
                    "title": "List Speakers"
                },
                {
                    "type": "postback",
                    "payload": "/sessions_list",
                    "title": "List Sessions"
                },
                
            ]
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []

class EventSchedule(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_schedule"

 def run(self,dispatcher,tracker,domain):
  
  text = "The event runs from {}. Select a session to get its date and time".format(data.get("date"))
  btn_opt = [
                {
                    "type": "postback",
                    "payload": "/session_one_details",
                    "title": "Session One details"
                },
                {
                    "type": "postback",
                    "payload": "/session_two_details",
                    "title": "Session Two detail"
                },
            ]
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []

class SpeakersList(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakers_list"

 def run(self,dispatcher,tracker,domain):
  ext = "The event runs from {}. Select a session to get its date and time".format(data.get("date"))
  btn_opt = [
                {
                    "type": "postback",
                    "payload": "/session_one_details",
                    "title": "Session One details"
                },
                {
                    "type": "postback",
                    "payload": "/session_two_details",
                    "title": "Session Two detail"
                },
            ]
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "John Doe 1",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Software Engineer",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/speakers_one_details",
                                    "title": "View Details"
                                }
                            ]
                        },
                        {
                            "title": "John Doe 2",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Software Engineer",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/speakers_two_details",
                                    "title": "View Details"
                                }
                            ]
                        },
                    ]
                }
            }
        }
  dispatcher.utter_message(json_message=gt)
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
                "payload": "/session_details/{}".format(session.get('title')),
                "title": session.get('title')
            }
    btn_opt.append(sess)
  
  dispatcher.utter_message(text=text, buttons=btn_opt)
  return []
 
class SpeakerOneDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_one_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "John Doe 1",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Software Engineer",
                            "text": "His details will be written here"
                        }
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []

class SpeakerTwoDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_two_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "John Doe 2",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Software Engineer",
                            "text": "His details will be written here"
                        }
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []

class SessionOneDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_one_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Session 1",
                            "subtitle": "Importance of chat gpt",
                            # "buttons": [
                            #     {
                            #         "type": "postback",
                            #         "payload": "/session_one_details",
                            #         "title": "View Details"
                            #     }
                            # ]
                        }
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []

class SessionTwoDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_two_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Session 2",
                            "subtitle": "Building chat gpt",
                            # "buttons": [
                            #     {
                            #         "type": "postback",
                            #         "payload": "/session_one_details",
                            #         "title": "View Details"
                            #     }
                            # ]
                        }
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
