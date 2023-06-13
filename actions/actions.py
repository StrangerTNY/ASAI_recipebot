# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_give_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Hello World!")
        
        # get the location slot
#        location = tracker.get_slot('location')

        # read the CSV file
        with open('Recipes.csv','r') as file:
            reader = csv.DictReader(file)
            # get a list of universities in the desired location
            #output = [row for row in reader if row['Location'] == location]
            for row in reader:
                if row['Title'] == 'Warm Comfort':
                    dispatcher.utter_message("I looked up the Warm Comfort Recipe for you! Here is it:")
                    return 
            
            dispatcher.utter_message("Im sorry, i do not know any meal with that name.")
            return
        if output: # there is at least one value
            # build your reply according to the output
            reply  = f"This is a list of universities in {location}:"
            reply += "\n- " + "\n- ".join([item['Name'] for item in output])
            # utter the message
            dispatcher.utter_message(reply)

        else: # the list is empty
            dispatcher.utter_message(f"I could not find universities in {location}")
        return []
