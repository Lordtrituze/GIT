"""def alternatingSums(a):
    team1 = []
    team2 = []
    for i in range(len(a)):
        if i % 2 == 0:
            team1.append(a[i])
        else:
            team2.append(a[i])
    print("team A is", team1)
    print("team B is", team2)
    team1 = sum(team1)
    team2 = sum(team2)
    return [team1, team2]
"""
def alternatingSums(a):
    sum_a = 0
    sum_b = 0

    for i in range(0, len(a), 2):
        sum_a += a[i]

    for i in range(1, len(a), 2):
        sum_b += a[i]

    return [sum_a, sum_b]
