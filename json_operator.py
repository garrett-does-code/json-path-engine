from business_rules.variables import _rule_variable_wrapper
from business_rules.fields import FIELD_TEXT
from business_rules.operators import BaseType, type_operator
from six import string_types
from jsonpath_ng import parse

EQUAL = "="
NOT_EQUAL = "!="
GREATER_THAN = ">"
GREATER_THAN_OR_EQUAL = ">="
LESS_THAN = "<"
LESS_THAN_OR_EQUAL = "<="

class JSONType(BaseType):
    name = "json"

    def _assert_valid_value_and_cast(self, value):
        value = value or {}
        # Must either be a dictionary variable or string JSON path operator
        if not isinstance(value, dict) and not isinstance(value, string_types):
            raise AssertionError("Value is not a json or string evaluation.")
        # Set the BaseType self.value
        return value
    
    def _compare(self, source, target, comparator):
        """Compare value of JSON path to value passed in the operator call.

        Args:
            source (Any): The value evaluated from the JSON path
            target (Any): The value passed in the operator call
            comparator (str): string representation of a boolean operand

        Returns:
            bool: The boolean result of the comparison between source and target.
        """
        compare_val = type(source)(target)
        if comparator == EQUAL:
            return source == compare_val
        if comparator == NOT_EQUAL:
            return source != compare_val
        if comparator == GREATER_THAN:
            return source > compare_val
        if comparator == GREATER_THAN_OR_EQUAL:
            return source >= compare_val
        if comparator == LESS_THAN:
            return source < compare_val
        if comparator == LESS_THAN_OR_EQUAL:
            return source < compare_val
        
    def _remove_quotes(self, val: str):
        if '"' == val[0]:
            return val.strip('"')
        if "'" == val[0]:
            return val.strip("'")
        return val
        
    def _find_match(self, json_path: str):
        """Return the first value evaluated at the json path or None."""
        json_path_exp = parse(json_path)
        return next(
            (match.value for match in iter(json_path_exp.find(self.value))),
            None
        )
        
    def _find_json_bool(self, json_path: str, default: bool = False):
        """Find boolean values in a dictionary via json path.

        Args:
            json_path (str): a json path to a dictionary value (Ex: $.my.dict[*].key)
            default (bool, optional): default value returned if json path is not found. Defaults to False.

        Returns:
            bool: The boolean value of the json path value or the default value if not found
        """
        json_path_exp = parse(json_path)
        return next(
            (match.value for match in iter(json_path_exp.find(self.value))),
            default
        )
        
    @type_operator(FIELD_TEXT, label="$.a.json[*].path =,!=,>,>=,<,<= value")
    def evaluate(self, operator_call: str):
        json_path, comparator, target = operator_call.split(" ", 2)
        target = self._remove_quotes(target)
        match = self._find_match(json_path)
        return self._compare(match, target, comparator) if match else False
    
    @type_operator(FIELD_TEXT, label="$.a.json[*].path")
    def is_true(self, json_path: str):
        return self._find_json_bool(json_path)
    
    @type_operator(FIELD_TEXT, label="$.a.json[*].path")
    def is_false(self, json_path: str):
        return not self._find_json_bool(json_path, True)
    
    @type_operator(FIELD_TEXT, label="$.a.json[*].path contains value")
    def contains(self, operator_call: str):
        json_path, _, substring = operator_call.split(" ", 2)
        substring = self._remove_quotes(substring)
        match = self._find_match(json_path)
        return substring in str(match)
    
def json_rule_variable(label=None):
    return _rule_variable_wrapper(JSONType, label)
