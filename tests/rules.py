RULES = [
    {
        "conditions": {
            # Follower count > 20000 AND account is not private
            "all": [
                {
                    "name": "tweet_data",
                    "operator": "evaluate",
                    "value": "$.user.followers_count > 20000"
                },
                {
                    "name": "tweet_data",
                    "operator": "is_false",
                    "value": "$.user.protected"
                }
            ]
        },
        "actions": [
            {
                "name": "add_action",
                "params": {
                    "title": "Super User",
                    "action_type": "promotion",
                    "description": "We should give this person a blue checkmark"
                }
            }
        ]
    },
    {
        "conditions": {
            "any": [
                {
                    "name": "tweet_data",
                    "operator": "contains",
                    "value": "$.user.location contains 'Australia'"
                }
            ]
        },
        "actions": [
            {
                "name": "add_action",
                "params": {
                    "title": "Australian",
                    "action_type": "regional",
                    "description": "This user would benefit from Australian news in their feed"
                }
            }
        ]
    },
    {
        "conditions": {
            # Tweet text contains '#Angular' OR a hashtags object has text containing 'Angular'
            "any": [
                {
                    "name": "tweet_data",
                    "operator": "contains",
                    "value": "$.text contains '#Angular'"
                },
                {
                    "name": "tweet_data",
                    "operator": "contains",
                    "value": "$.entities.hashtags[*].text contains 'Angular'"
                },
            ]
        },
        "actions": [
            {
                "name": "add_action",
                "params": {
                    "title": "Angular User",
                    "action_type": "enhanced_interests",
                    "description": "Suggest Angular programming accounts to this user"
                }
            }
        ]
    },
    {
        "conditions": {
            # An invalid JSON path will not raise an exception
            "all": [
                {
                    "name": "tweet_data",
                    "operator": "evaluate",
                    "value": "$.not.valid[*].path != 'Hello World'"
                }
            ]
        },
        "actions": [
            {
                "name": "add_action",
                "params": {
                    "title": "Bad Path",
                    "action_type": "fail_scenario",
                    "description": "This will not result in an action"
                }
            }
        ]
    }
]