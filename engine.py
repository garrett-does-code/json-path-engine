from json_operator import json_rule_variable
from business_rules.variables import BaseVariables
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_TEXT
from business_rules import run_all

class ExampleEngine:
    def __init__(self, rules: list, tweet: dict) -> None:
        self.rules = rules
        self.business_actions = []
        self.variables = PostVariables(tweet)
        self.actions = PostActions(self.business_actions)

    def run_rules(self):
        run_all(
            rule_list=self.rules,
            defined_variables=self.variables,
            defined_actions=self.actions,
            stop_on_first_trigger=False
        )

class PostVariables(BaseVariables):
    def __init__(self, tweet: dict) -> None:
        self.tweet = tweet

    @json_rule_variable
    def tweet_data(self):
        return self.tweet

class PostActions(BaseActions):
    def __init__(self, business_actions) -> None:
        self.business_actions = business_actions

    @rule_action(params={"title": FIELD_TEXT, "action_type": FIELD_TEXT, "description": FIELD_TEXT})
    def add_action(self, title, action_type, description):
        action = {
            "title": title,
            "action_type": action_type,
            "description": description
        }
        self.business_actions.append(action)
