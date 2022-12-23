import random


class Computer:

    PLAYER_TYPE = 'コンピューター'
    condition = {
        'win': 0,
        'lose': 0,
        'draw': 0
    }

    def __init__(self, hand_dict: dict) -> None:
        self.hand_dict = hand_dict

    def pick_random_hand(self) -> str:
        hand_key = random.randrange(1, 3)
        return self.hand_dict[hand_key]
