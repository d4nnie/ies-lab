"""
MIT License

Copyright (c) 2020 Daniil Shchepetilnikov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class State:
    """Class, representing current state in boat problem"""

    def __init__(self, human, cabbage,
                 wolf, goat, parent=None):
        self.human = human
        self.cabbage = cabbage
        self.wolf = wolf
        self.goat = goat
        self.__parent = parent

    def __eq__(self, other):
        try:
            return self.human == other.human and\
                self.cabbage == other.cabbage and\
                self.wolf == other.wolf and\
                self.goat == other.goat
        except AttributeError:
            return False

    def __str__(self):
        result_string = '['

        if self.human:
            result_string += 'П, '
        else:
            result_string += 'Л, '
        if self.cabbage:
            result_string += 'П, '
        else:
            result_string += 'Л, '
        if self.wolf:
            result_string += 'П, '
        else:
            result_string += 'Л, '
        if self.goat:
            result_string += 'П]'
        else:
            result_string += 'Л]'

        return result_string

    def __cross_empty(self):
        return State(not self.human, self.cabbage,
                     self.wolf, self.goat, self)

    def __cross_cabbage(self):
        if self.human == self.cabbage:
            return State(not self.human, not self.cabbage,
                         self.wolf, self.goat, self)
        return self

    def __cross_wolf(self):
        if self.human == self.wolf:
            return State(not self.human, self.cabbage,
                         not self.wolf, self.goat, self)
        return self

    def __cross_goat(self):
        if self.human == self.goat:
            return State(not self.human, self.cabbage,
                         self.wolf, not self.goat, self)
        return self

    @property
    def parent(self):
        """Get parent state of current state"""

        return self.__parent

    def childrens(self) -> list:
        """Generate childrens of current state"""

        def erase_failed(states: set) -> list:
            result_list = []
            for state in states:
                if state.wolf == state.goat != state.human or\
                   state.cabbage == state.goat != state.human:
                    continue
                result_list.append(state)

            return result_list

        return erase_failed([self.__cross_empty(),
                             self.__cross_cabbage(),
                             self.__cross_wolf(),
                             self.__cross_goat()])


class StateSpace:
    """Class, representing state space of boat problem"""

    def __init__(self, human, cabbage,
                 wolf, goat):
        self.__opening_state: State =\
            State(human, cabbage, wolf, goat)
        self.__knows_states = []

    @property
    def root(self) -> State:
        """Get opening state of state space"""

        return self.__opening_state

    def parent_of(self, state: State) -> State:
        """Get parent state of specified state in space"""

        for known_state in self.__knows_states:
            if known_state == state:
                return known_state.parent
        return None

    def childrens_of(self, state: State) -> list:
        """Get childrens of node"""

        self.__knows_states += state.childrens()
        return state.childrens()
