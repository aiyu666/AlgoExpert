def tournamentWinner(competitions, results):
    scores = {}
    for index, result in enumerate(results):
        if result == 0:
            scores[competitions[index][1]] = scores.get(competitions[index][1], 0) + 3
        else:
            scores[competitions[index][0]] = scores.get(competitions[index][0], 0) + 3
    return max(scores, key=scores.get)
