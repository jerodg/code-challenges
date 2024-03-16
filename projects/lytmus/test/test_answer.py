"""Run your answer against a specific test-case input from a JSON file.

This file serves two purposes:

    * It's a convenience script that allows you to execute your answer with a test-case,
      and view the results in the generated `output.json` file or stdout. It's analogous
      to pressing 'Try Answer' on the side panel, except it doesn't tell you if
      your answer is right or wrong.

    * It's used by the Lytmus platform to execute your answer with private test-cases.

You can execute and test your answer by pressing Try Answer or by running the following command on the command line:
    python test_answer.py <test_case_path>
For example:
    python test_answer.py inputs/window_1.json

--------------------------------------------------------------------------------------
IMPORTANT: You DO NOT need to modify this file. If you decide to do so, please
follow these guidelines:

    1. The name of this file must always be `test_answer.py`. DO NOT rename or
       delete this file.

    2. This file must always accept as a first argument the path to the JSON-encoded
       test file.

    3. This file must always write to a file called `output.json`, located
       in the same folder as `test_answer.py`.
"""

import sys
import json
import argparse


def main():
    # parse the arguments of the `test_answer.py` script
    description = 'Run your answer against a specific test-case input from a JSON file.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument('test_case_path',
                        help=('path to the JSON file containing the test-case input,'
                              ' eg, "inputs/window_1.json"'))
    args = parser.parse_args()

    # run your answer with the desired test-case
    run_answer(args.test_case_path)


def run_answer(test_case_path):
    """Feed the provided test-case to the answer() function, and dump the output to a JSON file.

    Args:
        test_case_path: String with path of test-case file, eg, 'inputs/window_1.json'.
    """
    input_dictionary = load_object_from_file(test_case_path)

    if not input_is_valid(input_dictionary):
        sys.exit(1)

    import answer
    output_object = answer.answer(**input_dictionary)

    # The output object must always be saved to 'output.json'. DO NOT change
    # the name of this file.
    output_path = 'output.json'
    dump_object_to_file(output_object, output_path)


def input_is_valid(input_dictionary):
    """Validates the input from the input file provided when running this script. The input file
    must contain all of the required fields, and the values for those fields must all be of an
    required type.

    Args:
        input_dictionary: A dictionary containing the contents of the input file provided when
                          this script is run.

    Returns:
        A boolean indicating whether the input file contains all required fields and that they all
        contain values of the correct type.
    """

    # Mapping of required field names to the required type of values for that field for the
    # contents of the input file
    required_fields = {
        'window_string': 'unicode',
    }

    fields_are_valid = True
    for field_name, value_type in required_fields.items():
        if not input_dictionary.has_key(field_name):
            print 'Error, input file does not contain the field "%s"' % field_name
            fields_are_valid = False
        elif type(input_dictionary[field_name]).__name__ != value_type:
            print 'Error, field "%s" in input file has the type "%s", but the type should be "%s"' % (
                  field_name, type(input_dictionary[field_name]).__name__, value_type)
            fields_are_valid = False
    return fields_are_valid


def load_object_from_file(filepath):
    """Load the specified JSON-encoded file to a Python object.

    Args:
        filepath: String with path of JSON-encoded file, eg, 'inputs/window_1.json'.

    Returns:
        A Python object holding the content of the JSON-encoded file, eg, {"name": "bill"}.
    """
    try:
        with open(filepath, 'r') as file:
            dictionary = json.loads(file.read())
    except IOError:
        print 'Error: could not read file %s.' % filepath
        sys.exit(1)
    except ValueError:
        print 'Error: the file %s does not contain valid JSON.' % filepath
        sys.exit(1)

    fields_are_valid = True
    if not dictionary.has_key('window_string'):
        fields_are_valid = False
        print 'Error, input JSON file does not have field "window_string"'

    if fields_are_valid:
        return dictionary
    else:
        sys.exit(1)


def dump_object_to_file(object, filepath):
    """Encode the specified Python object as JSON, and write it to the specified file.

    Args:
        object: Python object to be JSON-encoded and dumped to file.
        filepath: String with path of file to create, eg, 'output.json'.
    """
    with open(filepath, 'w') as file:
        file.write(json.dumps(object))


if __name__ == '__main__':
    main()

