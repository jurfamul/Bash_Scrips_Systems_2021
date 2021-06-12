#!/user/bin/python3
class TestError(Exception):
    def __init__(self, description="error test"):
        self.description = description

    def __str__(self):
        return self.description


class TrialError(Exception):
    def __init__(self):
        self.description = "trial error: try again later."


def test(x):
    if x < 10:
        raise TestError("failed test.")
    else:
        print("passed test.")

def trial(y):
    if y != "success":
        raise TrialError()
    else:
        print(y)

x = 1
y = "hello"

try:
    test(x)
except TestError as err:
    print("exception type: {0}, Error message: {1}".format(type(err), str(err)))
finally:
    x = 11

try:
    trial(y)
except TrialError as err:
    print("exception type: {0}, Error message: {1}".format(type(err), str(err)))
finally:
    y = "success"

try:
    test(x)
except TestError as err:
    print("exception type: {0}, Error message: {1}".format(type(err), str(err)))
finally:
    x = 11

try:
    trial(y)
except TrialError as err:
    print("exception type: {0}, Error message: {1}".format(type(err), str(err)))
finally:
    y = "success"