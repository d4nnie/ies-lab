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
import boat_problem as bp


def __parse_state(text: str):
    text = text.replace(' ', '')
    states = text[1:len(text) - 1].split(',')
    return [state == 'П' for state in states]


@click.command()
@click.option('-o', '--opening-state', type=str,
              help='Specify opening state.')
@click.option('-t', '--target-state', type=str,
              help='Specify target state.')
@click.option('-w', '--wide-search', is_flag=True,
              help='Use wide-search algorithm.')
@click.option('-d', '--depth-search', is_flag=True,
              help='Use depth-search algorithm.')
def cli(opening_state, target_state, wide_search, depth_search):
    """
    Command-line user interface function,
    designed to be program entry.
    """

    opening_states = __parse_state(opening_state)
    graph = bp.StateSpace(opening_states[0], opening_states[1],
                          opening_states[2], opening_states[3])

    target_states = __parse_state(target_state)
    target_state = bp.State(target_states[0], target_states[1],
                            target_states[2], target_states[3])

    def show_path_and_step(algo):
        try:
            path, step = algo.search(target_state)
            print('Path:', path, '\nStep:', step)
        except TypeError:
            print('Specified failed opening or target state.')

    if wide_search:
        print('Wide-search algorithm...')
        show_path_and_step(gpt.WideSearch(graph))
    if depth_search:
        if wide_search:
            print() # Print empty line
        print('Depth-search algorithm...')
        show_path_and_step(gpt.DepthSearch(graph))


cli()
