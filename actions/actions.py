# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import numpy as np 
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict
import csv

# custom action to validate the recipe form
class ValidateRecipeForm(FormValidationAction):
    # name of the action to be declared in domain.yml
    def name(self) -> Text:
        return "validate_recipe_form"
    
    # validate the ingredient slot
    def validate_ingredient(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        domain: DomainDict,
        tracker: Tracker,
    ) -> Dict[Text, Any]:
        with open('Recipes.csv', newline='', encoding="utf8") as csvfile:	
            reader = csv.DictReader(csvfile)
            recipes = []
            for row in reader:
                if slot_value.lower() in row['Ingredients']:
                    recipes.append(row['Number'] + " " +row['Title'])
            if len(recipes) == 0:
                dispatcher.utter_message(text="Sorry, I couldn't find any recipes with that ingredient.")
                return {"ingredient": None}
            elif len(recipes) > 5:
                dispatcher.utter_message(text="Here are a few recipes with that ingredient:\n" + '\n'.join(np.random.choice(recipes, 5, replace=False)))
            else:
                dispatcher.utter_message(text="Here are all recipes with that ingredient:\n" + '\n'.join(recipes))
        return {"ingredient": slot_value}
    
    # validate the recipe number slot
    def validate_recipe_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        domain: DomainDict,
        tracker: Tracker,
    ) -> Dict[Text, Any]:
        with open('Recipes.csv', newline='', encoding="utf8") as csvfile:	
            reader = csv.DictReader(csvfile)
            recipe_name = []
            recipe_ingredients = []
            recipe_instructions = []
            for row in reader:
                if slot_value == row['Number']:
                    recipe_name.append(row['Title'])
                    recipe_ingredients.append(row['Ingredients'])
                    recipe_instructions.append(row['Instructions'])
            if len(recipe_name) == 0:
                dispatcher.utter_message(text="Sorry, I couldn't find that recipe.")
                return {"recipe_number": None}
            else:
                dispatcher.utter_message(text="Here are the instructions and ingredients for " + recipe_name[0] + ":\n\n " + recipe_ingredients[0]  + "\n\n" + recipe_instructions[0] )
        return {"recipe_number": slot_value}

