import json
import os
from engine import ExampleEngine
from rules import RULES

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/sample_data/twitter_data.json", "r") as f:
    test_tweet = json.loads(f.read())

def test_example_engine():
    ee = ExampleEngine(RULES, test_tweet)
    ee.run_rules()
    super_user_action = [a for a in ee.business_actions if a["title"] == "Super User"]
    bad_path_action = [a for a in ee.business_actions if a["title"] == "Bad Path"]
    assert super_user_action
    assert not bad_path_action