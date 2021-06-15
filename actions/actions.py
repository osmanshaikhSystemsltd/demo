# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json


class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_fallback"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         slot = tracker.get_slot("fallback")
         message = tracker.latest_message.get('text')
         url = "http://52.152.235.114:3449/index/"
         fmsg = url + message
         resp = requests.get(fmsg)
         
         if resp.status_code != 200:
             print("something went wrong")
        
         json_data = json.loads(resp.text)
         #print(json_data['answers'][0]['context'])
         
         #dispatcher.utter_message(text=f"Hello World! The latest message is: {message}")
         
         #dispatcher.utter_message(text=json_data['answers'][0]['context'])
         dispatcher.utter_message(text=json_data[0])
#         dispatcher.utter_message(text= json_data['answers'][0]['score'])

         return []
     
class ActionLocal(Action):
     def name(self) -> Text:
         return "action_localapi"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         slot = tracker.get_slot("fallback")
         #message = tracker.latest_message.get('text')
         url = "http://127.0.0.1:3449/getTaxCertificate"
         fmsg = url #+ message
         resp = requests.get(fmsg)
         
         if resp.status_code != 200:
             print("something went wrong")
        
         #json_data = json.loads(resp.text)
         #print(json_data['answers'][0]['context'])
         
         #dispatcher.utter_message(text=f"Hello World! The latest message is: {message}")
         
         #dispatcher.utter_message(text=json_data['answers'][0]['context'])
         dispatcher.utter_message(text=resp.text)
#         dispatcher.utter_message(text= json_data['answers'][0]['score'])

         return []
#slot = "what is the hotline number?"
#url = "http://40.117.255.42:3449/index/"
#temp = url + slot
#resp = requests.get(temp)
            
#if resp.status_code != 200:
#    print("something went wrong")
            
#json_data = json.loads(resp.text)
#print("Context is: ", json_data['answers'][0]['context'])
#print("Score is: ", json_data['answers'][0]['score'])

