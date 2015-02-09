# coding: utf-8


class ModifyDict(dict):

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(
                '"{}" does not have "{}" attribute.'.format(self.__class__.__name__, item),
            )

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError:
            raise AttributeError(
                '"{}" does not have "{}" attribute.'.format(self.__class__.__name__, item),
            )
