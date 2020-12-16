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

class WideSearch:
    """Implementation of wide search algorithm"""

    def __init__(self, graph):
        self.__graph = graph
        self.__opened = self.__graph.childrens_of(self.__graph.root).copy()
        self.__closed = [self.__graph.root]
        self.__step = 1

    def __restore_path(self, target):
        nodes = [str(target)]
        last_node = target
        while last_node != self.__graph.root:
            nodes.append(str(self.__graph.parent_of(last_node)))
            last_node = self.__graph.parent_of(last_node)
        return ' -> '.join(reversed(nodes))

    def __clear(self):
        self.__opened = self.__graph.childrens_of(self.__graph.root).copy()
        self.__closed = [self.__graph.root]
        self.__step = 1

    def search(self, target):
        """
        Search function, use it to find path to target
        and number of steps, needed to find target.
        """

        current = self.__opened[0]
        while len(self.__opened) != 0:
            if current in self.__closed:
                self.__opened.pop(0)
                current = self.__opened[0]
                continue
            self.__step += 1

            if current == target:
                path, step = self.__restore_path(target), self.__step
                self.__clear()
                return path, step

            self.__closed.append(self.__opened[0])
            self.__opened += self.__graph.childrens_of(self.__opened[0])
            self.__opened.pop(0)
            current = self.__opened[0]
        self.__clear()


class DepthSearch:
    """Implementation of depth search algorithm"""

    def __init__(self, graph):
        self.__graph = graph
        self.__opened = self.__graph.childrens_of(self.__graph.root).copy()
        self.__closed = [self.__graph.root]
        self.__step = 1

    def __restore_path(self, target):
        path = [str(target)]
        last_node = target
        for item in reversed(self.__closed):
            if last_node in self.__graph.childrens_of(item):
                path.append(str(item))
                last_node = item

        return ' -> '.join(reversed(path))

    def __clear(self):
        self.__opened = self.__graph.childrens_of(self.__graph.root).copy()
        self.__closed = [self.__graph.root]
        self.__step = 1

    def search(self, target):
        """
        Search function, use it to find path to target
        and number of steps, needed to find target.
        """

        current = self.__opened[0]
        while len(self.__opened) != 0:
            if current in self.__closed:
                self.__opened.pop(0)
                current = self.__opened[0]
                continue
            self.__step += 1

            if current == target:
                path, step = self.__restore_path(target), self.__step
                self.__clear()
                return path, step

            self.__closed.append(current)
            self.__opened.pop(0)
            self.__opened = self.__graph.childrens_of(current).copy() +\
                self.__opened
            current = self.__opened[0]
        self.__clear()


class RecursiveDepthSearch:
    """Implementation of recursive depth search algorithm"""

    def __init__(self, graph):
        self.__graph = graph

    def search(self, target):
        """
        Search function, use it to find path to target
        and number of steps, needed to find target.
        """

        def func(target, current, path, closed, step):
            if current == target:
                return ' -> '.join(path), step

            closed.append(current)
            for child in self.__graph.childrens_of(current):
                if child not in closed:
                    value = func(target, child,
                                 path + [str(child)],
                                 closed, step + 1)
                    if value is not None:
                        return value
            return None

        return func(target, self.__graph.root, [str(self.__graph.root)], [], 2)
