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

import click
import graph_tool as gpt


@click.command()
@click.option('-v', '--visualize', is_flag=True,
              default=False, help='Visualize graph.')
@click.option('-p', '--path', required=True,
              help='Read file from path.')
@click.option('-w', '--wide-search', type=int,
              help='Find node with wide-search algorithm.')
@click.option('-d', '--depth-search', type=int,
              help='Find node with depth-search algorithm.')
def cli(visualize, path, wide_search, depth_search):
    """
    Command-line user interface function,
    designed to be program entry.
    """

    with open(path, 'r') as adjlist:
        content = adjlist.read()
    graph = gpt.Graph(content.split('\n'))

    if wide_search is not None:
        algo = gpt.WideSearch(graph)
        path, step = algo.search(wide_search)
        click.echo('Wide-search algorithm...\nPath: {}\nStep: {}'
                   .format(path, step))

    if depth_search is not None:
        if wide_search is not None:
            print() # Print empty line

        algo = gpt.RecursiveDepthSearch(graph)
        path, step = algo.search(depth_search)
        click.echo('Iterative depth-search algorithm...\nPath: {}\nStep: {}\n'
                   .format(path, step))

        algo = gpt.RecursiveDepthSearch(graph)
        path, step = algo.search(depth_search)
        click.echo('Recursive depth-search algorithm...\nPath: {}\nStep: {}'
                   .format(path, step))

    if visualize:
        graph.visualize()


cli()
