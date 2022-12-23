from computer import Computer
from judge import Judge
from player import Player


class JankenController:

    HAND_DICT = {
        1: 'グー',
        2: 'チョキ',
        3: 'パー',
    }

    def __init__(self) -> None:
        self.rounds = 1

    def main(self) -> None:
        player = Player(self.HAND_DICT)
        computer = Computer(self.HAND_DICT)
        judge = Judge(player, computer)

        while True:
            self.display_line('start')

            player_hand = player.pick_hand()
            computer_hand = computer.pick_random_hand()

            self.display_hand(player_hand, player.PLAYER_TYPE)
            self.display_hand(computer_hand, computer.PLAYER_TYPE)

            judge.declare_winner(player_hand, computer_hand)

            self.display_current_condition(player.condition)

            self.rounds += 1

            if player.condition['win'] == judge.WIN_CONDITION or computer.condition['win'] == judge.WIN_CONDITION:
                self.display_line('end')
                judge.declare_victor()
                break

    def display_line(self, type: str) -> None:
        if type == 'start':
            print(f'--------------------【{self.rounds}回目】--------------------\n')
        elif type == 'end':
            print('-------------------------------------------------------------\n')

    def display_hand(self, hand: str, player_type: str) -> None:
        print(f'{player_type}の選択した手は{hand}です')

    def display_current_condition(self, condition: dict) -> None:
        print(f"【現在】{condition['win']} 勝 {condition['lose']} 負 {condition['draw']} 分け")


if __name__ == '__main__':
    JankenController().main()
