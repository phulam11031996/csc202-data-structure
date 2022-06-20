import sys
import collections


# list[list[str]] - > str
def tsort(edge_list: list[list[str]]) -> str:
    """Performs a topological sort of the given graph.

    The graph is specifed as a list of edges, where each edge is a list
    of two vertices.  The result will be a string formatted identically
    to the Unix utility tsort.  That is, a string with one vertex per
    line in topologically sorted order.

    For example:

    >>> print(tsort([['101', '202'], ['202', '203']]))
    101
    202
    203

    Args:
        edge_list: the graph to be topologically sorted, given as a list
            of edges.

    Returns:
        a string containing a topological ordering for the given graph

    Raises:
        ValueError:
            if the graph contains a cycle (isn't acyclic) with the
            message, "input contains a cycle"
    """
    # Build an adjacency list
    d = collections.defaultdict(list)
    for edge in edge_list:
        d[edge[0]] = [0]
        d[edge[1]] = [0]
    for edge in edge_list:
        d[edge[1]][0] += 1
        d[edge[0]].append(edge[1])
    
    print(d)

    # Push all vertices with an in-degree of zero on to a stack
    stack = []
    for vertex in d:
        if d[vertex][0] == 0:
            stack.append(vertex)

    # While the stack is not empty
    expected = ''
    while len(stack) > 0:
        popped = stack.pop()  # Pop and output a vertex
        expected += str(popped) + '\n'
        for edge in d[popped]:
            if edge in d:
                d[edge][0] -= 1  # Reduce the in-degree
                if d[edge][0] == 0:  # n-degree of a vertex is 0, push the vertex
                    stack.append(edge)
    for vertex in d:
        if d[vertex][0] > 0:
            raise(ValueError)

    return expected


# NOTE: You should not modify the main function.  You also don't need
# to write tests for the main function.
def main(argv: list[str]) -> None:
    # if len(argv) != 2:
    #     print('usage: python3 tsort <filename>', file=sys.stderr)
    #     sys.exit(1)

    # with open(argv[1]) as file:
    #     edge_list = [line.split() for line in file]
    edges = [
            ['3', '8'], ['3', '10'], ['5', '11'], ['7', '8'], ['7', '11'],
            ['8', '9'], ['11', '2'], ['11', '9'], ['11', '10']
        ]

    print(tsort(edges))


if __name__ == '__main__':
    main(sys.argv)
