from games import *

class GameOfNim(Game):
    # A state has the player to move, a cached utility, a list of moves in
    # the form of a list of (r, n) positions, and a board as a list with 
    # number of objects in each row.

    def __init__(self, board=[3,1]):
        # make the initial game state
        # player 'MAX' goes first
        # get valid moves for the starting board
        moves = []
        for r, n_objects in enumerate(board):
            for n in range(1, n_objects + 1):
                moves.append((r, n))
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        # legal moves are at least one object, all from the same row
        return state.moves

    def result(self, state, move):
        # return the state that results from making a move from a state
        # copy the current board
        board = state.board.copy()
        r, n = move
        board[r] -= n
        
        # get new valid moves
        moves = []
        for r, n_objects in enumerate(board):
            for n in range(1, n_objects + 1):
                moves.append((r, n))
        
        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        return GameState(to_move=next_player, utility=0, board=board, moves=moves)

    def utility(self, state, player):
        if self.terminal_test(state):
            # player who has to move in terminal state loses
            return 1 if state.to_move == player else -1
        return 0

    def terminal_test(self, state):
        # a state is terminal if there are no objects left
        return sum(state.board) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # making the game
    #nim = GameOfNim(board=[7, 5, 3, 1]) # bigger board to search for more testing
    print(nim.initial.board)
    print(nim.initial.moves)
    print(nim.result(nim.initial, (1,3)))
    utility = nim.play_game(alpha_beta_player, random_player)
    if (utility > 0):
        print("MAX won the game")
    else:
        print("MIN won the game")
