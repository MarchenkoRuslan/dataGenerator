import random
import re
import invRegex


class RandomString(object):
    def __init__(self, regex):
        self.possible_strings = list(invRegex.invert(regex))

    def random_string(self):
        return random.choice(self.possible_strings)

#single
# exampple = RandomString('\d{1,7}')
# print(exampple.random_string())


#multiple
for s in invRegex.invert(r"[A-Z]{3}\d{3}"):
    print (s)


