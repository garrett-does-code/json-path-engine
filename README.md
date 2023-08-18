# JSON Path Engine

## Summary
Combine JSON Path with the Venmo Business Rules engine.

## Components
* [Venmo Business Rules](https://github.com/venmo/business-rules)
* [JSONPath for Python](https://pypi.org/project/jsonpath-ng/)
* Install [poetry dependency manager](https://python-poetry.org/)

## Usage
The enhancement to Venmo Business Rules allows for a JSONType. This type can have rules with 
operators like `evaluate`, `contains`, `is_true`, and `is_false` that take a JSON path as an 
argument.

Given a JSON object like:
```
{"key": {"nestedKey": [{"listedKey": "hello"}, {"listedKey": "world"}]}}
```
an example JSON path would be `$.key.nestedKey[*].listedKey`. This would evaluate to two values: "hello" and "world".

## Testing
The example I implemented uses a simple JSON object I found from this [Sitepoint article](https://www.sitepoint.com/twitter-json-example/). 
The JSON is an example of a social media post. Sample rules were written in `rules.py` to show some capabilities of the JSONType.
