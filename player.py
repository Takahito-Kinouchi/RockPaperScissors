class Player:

    PLAYER_TYPE = 'あなた'

    condition = {
        'win': 0,
        'lose': 0,
        'draw': 0
    }

    def __init__(self, hand_dict: dict) -> None:
        self.hand_dict = hand_dict

    def pick_hand(self) -> str:
        key = 0
        while key not in self.hand_dict.keys():
            key = int(input('じゃんけんの手を選択してください\n1. グー 2. チョキ 3. パー\n'))
            if key in self.hand_dict.keys():
                return self.hand_dict[key]
            else:
                print('キーの選択が不正です')
