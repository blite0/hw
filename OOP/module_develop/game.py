import models
import settings
import exceptions

player_name = ''


def play():
    global player_name
    player_name = input("Please enter your name\n")
    player = models.Player(player_name)
    level = 1
    opponent = models.Enemy(level)
    start_game = input("Write 'start' to start the game\n")

    if start_game == 'start':
        while True:
            try:
                player.attack(opponent)
                player.defence(opponent)
            except exceptions.EnemyDown:
                level += 1
                opponent = models.Enemy(level)
                settings.score = (level - 1) * 5 + player.allowed_attacks


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        print('Gameover')
        print('Score :', settings.score)
        file = open('scores.txt', 'a')
        file.write(f"Name: {player_name}, Scores: {settings.score}" + '\n')
        file.close()
        result_sort = exceptions.Score()
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')
