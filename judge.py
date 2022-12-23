class Judge:

    WIN_CONDITION = 3

    victor: str = ''
    result: dict = {}

    def __init__(self, player, computer) -> None:
        self.player = player
        self.computer = computer

    def declare_winner(self, player_hand: str, computer_hand: str) -> None:
        if player_hand == computer_hand:
            self.player.condition['draw'] += 1
            self.computer.condition['draw'] += 1
        elif ((player_hand == 'グー' and computer_hand == 'チョキ') 
                or (player_hand == 'チョキ' and computer_hand == 'パー') 
                or (player_hand == 'パー' and computer_hand == 'グー')):
            self.player.condition['win'] += 1
            self.computer.condition['lose'] += 1
        else:
            self.player.condition['lose'] += 1
            self.computer.condition['win'] += 1

    def declare_victor(self) -> None:
        if self.player.condition['win'] == self.WIN_CONDITION:
            print('Playerの優勝です!')
            self.victor = 'player'
        elif self.computer.condition['win'] == self.WIN_CONDITION:
            print('Computerの優勝です!')
            self.victor = 'computer'

        self.result = self.player.condition
