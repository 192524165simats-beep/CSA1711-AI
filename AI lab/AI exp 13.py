def minimax(tree, depth, max_player):
    if depth == 2:
        return tree

    values = [minimax(x, depth + 1, not max_player)
              for x in tree]

    return max(values) if max_player else min(values)

tree = [[3, 5], [2, 9]]

print("Best value:", minimax(tree, 0, True))
