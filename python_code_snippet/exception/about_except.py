class FuckError(Exception):
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    try:
        raise FuckError(2*2)
    except FuckError as e:
        print("Fuck Exception, value", e.value)
