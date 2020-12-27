from collections import defaultdict


class Share:
    """
    Share Class handles common data shared between Signals and Slots

    There are 4 types of data.
    1. args
    2. single
    3. multi
    4. history

    Each of data has 3 methods.
    1. get
    2. update
    3. remove
    """
    def __init__(self):
        self.args = dict()
        self.single = defaultdict(dict)
        self.multi = defaultdict(lambda: defaultdict(list))
        self.history = defaultdict(lambda: defaultdict(list))

    """
    Arg Data
    """
    def get_args(self, fn, key=None):
        if key is None:
            return self.args[fn]
        return self.args[fn][key]

    def update_args(self, fn, args):
        self.args[fn] = args

    def remove_args(self, fn):
        del self.args[fn]

    """
    Single Data
    """
    def get_single(self, fn, key=None):
        if key is None:
            return self.single[fn]
        return self.single[fn][key]

    def update_single(self, fn, key, val):
        self.single[fn][key] = val

    def remove_single(self, fn):
        del self.single[fn]

    """
    Multi Data
    """
    def get_multi(self, fn, key=None):
        if key is None:
            return self.multi[fn]
        return self.multi[fn][key]

    def update_multi(self, fn, key, vals):
        self.multi[fn][key] += vals

    def remove_multi(self, fn):
        del self.multi[fn]

    """
    History Data
    """
    def get_history(self, code=None, key=None):
        if code is None:
            return self.history
        elif key is None:
            return self.history[code]
        return self.history[code][key]

    def update_history(self, code, key, vals):
        self.history[code][key] += vals

    def remove_history(self, code):
        del self.history[code]