import game
import exceptions
import random


class Enemy(object):

    def __init__(self, level, lives=1):
        self.level = level
        self.lives = level

    def select_attack(self):
        return random.randrange(1, 4)

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            raise exceptions.EnemyDown


class Player(object):
    def __init__(self, name, lives=2, score=0, allowed_attacks=1):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    def fight(self, attack, defense):
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) \
                or (attack == 3 and defense == 1):
            return 1
        elif attack == defense:
            return 0
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.GameOver

    def attack(self, enemy_obj):
        player_attack = int(input('Кем будешь атаковать ?Волшебник - 1, Воин - 2, Разбойник - 3 ' '\n'))
        enemy_attack = enemy_obj.select_attack()
        fight_play = self.fight(player_attack, enemy_attack)
        if fight_play == 0:
            print("It's a draw!")
        elif fight_play == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.allowed_attacks += 1
        elif fight_play == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        player_attack2 = int(input('Кем будешь защищаться ?Волшебник - 1, Воин - 2, Разбойник - 3' '\n'))
        enemy_attack2 = enemy_obj.select_attack()
        fight_play = self.fight(player_attack2, enemy_attack2)
        if fight_play == 0:
            print("It's a draw!")
        elif fight_play == 1:
            print("You attacked successfully!")
        elif fight_play == -1:
            print("You missed!")
            self.decrease_lives()
