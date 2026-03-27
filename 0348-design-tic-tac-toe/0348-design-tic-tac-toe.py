class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1

        self.rows[row] += score
        if abs(self.rows[row]) == self.n:
            return player
        self.cols[col] += score
        if abs(self.cols[col]) == self.n:
            return player

        if row == col:
            self.diag += score
            if abs(self.diag) == self.n:
                return player

        if row + col == self.n - 1:
            self.anti_diag += score
            if abs(self.anti_diag) == self.n:
                return player

        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)