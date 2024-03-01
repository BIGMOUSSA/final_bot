# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from my_request import send_request_and_store_result

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_nlg"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = tracker.latest_message.get('text', '')
        answer = send_request_and_store_result(query = latest_message)
        dispatcher.utter_message(f"{answer}")
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_default")
        answer = "Merci de reformuler votre question! \n Peut-être aussi votre question n'est pas prise en compte dans cette bot!"
        dispatcher.utter_message(f"{answer}")
        return []