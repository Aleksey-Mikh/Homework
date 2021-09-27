"""
Implement custom dictionary that will memorize 10 latest
changed keys. Using method "get_history" return this keys.

Example:

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()

output: ["bar"]
"""


class TypeException(Exception):
    """class exception which calls when the type is incorrect"""

    def __init__(self, message):
        super().__init__(message)


class HistoryDict:

    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.dictionary = dictionary
            self.history_list = []
        else:
            raise TypeException(f"{dictionary} isn't a dict")

    def set_value(self, key, value):
        if key.__hash__ and key.__eq__:
            self.dictionary.update([(key, value)])
            self.history_list.append(key)
        else:
            raise TypeException(f"{key} can't be a dictionary key")

    def get_history(self):
        self.history_list = self.history_list[:10]
        return self.history_list


def main():
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    print(d.get_history())


if __name__ == '__main__':
    main()
