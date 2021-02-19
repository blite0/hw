class GameOver(Exception):
    def __str__(self):
        print('Gameover')


class EnemyDown(Exception):
    pass


class Score():
    def __init__(self):
        with open('scores.txt') as sorter:
            lines = [line.split('Scores: ') for line in sorter]
        file = open("scores.txt", 'w')

        for line in sorted(lines, key=lambda x: int(x[1]), reverse=True)[:10]:
            file.write('Scores: '.join(line))
