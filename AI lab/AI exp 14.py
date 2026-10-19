def alphabeta(tree, depth, alpha, beta, maximizing):
    if depth == 2:
        return tree

    if maximizing:
        best = -999
        for x in tree:
            best = max(best, alphabeta(x, depth+1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for x in tree:
            best = min(best, alphabeta(x, depth+1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

tree = [[3, 5], [2, 9]]
print("Best value:", alphabeta(tree, 0, -999, 999, True))
