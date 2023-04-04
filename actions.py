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

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action

class EventVenue(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_venue"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Shanti Mittal Auditorium",
                            "subtitle": "Inside LPU campus",
                            "buttons": [
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
                        },
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []

class EventSchedule(Action):
 def name(self):
  """name of the custom action"""
  return "action_event_schedule"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Event Schedule",
                            "subtitle": "Date and Time of event",
                            "buttons": [
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
                                
                            ],
                            "text": "The event runs from 13 to 15 April, 2023. Select a session to get its date and time"
                        },
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []

class SpeakersList(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakers_list"

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
  dispatcher.utter_custom_json(gt)
  return []

class SessionsList(Action):
 def name(self):
  """name of the custom action"""
  return "action_sessions_list"

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
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_one_details",
                                    "title": "View Details"
                                }
                            ]
                        },
                        {
                            "title": "Session 2",
                            "subtitle": "Build chat GPT",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_two_details",
                                    "title": "View Details"
                                }
                            ]
                        },
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
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
