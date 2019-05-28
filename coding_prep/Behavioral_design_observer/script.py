#!/usr/bin/env python
# -*-coding: utf-8 -*-

#script.py
#Osman Mamun
#CREATED: 05-27-2019

'''
Here I'll design a toy problem to implement an observer design pattern. We all
are interested in celebrity's life style. Whenever a celebrity eats food or
gets a salary raise, it will automatically notify paparazzi and his
agent.
'''
from abc import ABC, abstractmethod

class Observer(ABC):
    '''Baseclass for observer. Every observer should printout the updated
    observable'''
    @abstractmethod
    def update(self, observable, *args):
        pass

class Observable:
    '''Common class behavior for an object to be an observable'''
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, *args):
        for observer in self.__observers:
            observer.update(self, *args)


class Actor(Observable):

    def __init__(self, name, salary, eating_state):
        super().__init__()
        self._name = name
        self._salary = salary
        self._eating_state = eating_state

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
        self.notify_observer(new_salary)

    @property
    def eating_state(self):
        return self._eating_state

    @eating_state.setter
    def eating_state(self, new_eating_state):
        self._eating_state = new_eating_state
        self.notify_observer(new_eating_state)

class Paparazzi(Observer):

    def update(self, actor, new_prop):
        if isinstance(new_prop, bool):
            if new_prop:
                print(f"Hurry up! {actor.name} is eating out with "
                      "his girlfriend. Let's take some quick photos.")
        else:
            print(f"Breaking news! {actor.name}'s salary increased "
                  f" to {new_prop}!")


class Agent(Observer):

    def update(self, actor, new_prop):
        if isinstance(new_prop, bool):
            if new_prop:
                print(f"{actor.name} is eating out with "
                      "his girlfriend. Let's take some rest.")
        else:
            print(f"{actor.name}'s salary increased "
                  f" to {new_prop}. I should get a raise too.")


if __name__ == "__main__":
    actor = Actor('Leaonardo', 80000, False)
    agent = Agent()
    paparazzi = Paparazzi()
    actor.add_observer(agent)
    actor.add_observer(paparazzi)
    print('\n1st update:')
    actor.salary = 90000
    actor.eating_state = True
    actor.remove_observer(paparazzi)
    print('\n2nd update:')
    actor.salary = 95000
    actor.eating_sate = False
    actor.eating_state = True

