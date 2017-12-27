from collections import namedtuple
from abc import ABCMeta, abstractmethod

Unit = namedtuple('unit', 'name health attack defence resistance speed skills')
Skills = namedtuple('skills', 'a b c seal weapon assist special')

# Another possible implementation, seems worse
# class Skills(object):
#     def __init__(
#         self, 
#         a=None,
#         b=None,
#         c=None,
#         seal=None,
#         weapon=None,
#         assist=None,
#         special=None
#     ):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.seal=seal
#         self.weapon=weapon
#         self.assist=assist
#         self.special=special


class Special(ABCMeta):
    def __init__(self, charge=0, cap=1, this_unit=None):
        self.charge = charge
        self.cap = cap

    @abstractmethod
    def phase(self):
        # Phase which this special decorates with trigger function
        pass

    @abstractmethod
    def triggerFunction(self):
        # Does 'resolve combat as if' only apply to this specific blow?
        pass

    def resetCharge(self):
        self.charge = 0

    def chargeBy(self, amount):
        # Can a 'charge slower' get rid of a special?
        # Can it get it up past the original amount?
        # Are these restrictions necessary?
        self.charge = max(min(self.charge + amount, self.cap), 0)

    def chargeCountdown(self):
        return self.cap - self.charge
