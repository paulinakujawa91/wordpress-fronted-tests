import random


def get_random_string():
    ints = range(33, 127)
    random_string = ''

    for i in range(10):
        random_string += chr(random.choice(ints))
    return random_string

def confirm_javascript_alert():
    # Wait for the alert to be displayed and store it in a variable
    alert = wait.until(expected_conditions.alert_is_present())
    # Press the OK button
    alert.accept()