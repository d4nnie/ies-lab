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

import networkx as nx
import matplotlib.pyplot as plt
import EoN as eon


class Graph:
    """Class, represting a directed graph"""

    def __init__(self, adjlist, root=int()):
        self.__root = root
        self.__graph = nx.parse_adjlist(adjlist,
                                        create_using=nx.DiGraph,
                                        nodetype=int)

    @property
    def root(self) -> int:
        """Get root of graph"""

        return self.__root

    def childrens_of(self, node) -> list:
        """Get list of child nodes of specified node"""

        return list(self.__graph.successors(node))

    def parent_of(self, node):
        """Get parent node of specified node"""

        try:
            return list(self.__graph.predecessors(node))[0]
        except IndexError:
            return None

    def visualize(self):
        """Visualize graph like tree"""

        tree = nx.bfs_tree(self.__graph, self.__root)
        plt.figure(figsize=(8, 8))
        pos = eon.hierarchy_pos(tree, self.__root)
        nx.draw(self.__graph, pos=pos, with_labels=True, arrows=True)
        plt.show()
