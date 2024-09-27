import random


def group1(self, board):
    possible_moves = self.getPossibleMoves(board)
    
    if possible_moves is None or len(possible_moves)==0:
        self.game.end_turn()
        return None, None
    
    selected_move_index = random.randint(0,len(possible_moves)-1)
    random_move = possible_moves[selected_move_index]
    
    if len(random_move)<3 or random_move[2] is None:
        self.game.end_turn()
        return None, None
    
    valid_moves_for_piece = random_move[2]
    
    if valid_moves_for_piece is None or len(valid_moves_for_piece)==0:
        self.game.end_turn()
        return None, None
    
    selected_choice_index = random.randint(0,len(valid_moves_for_piece)-1)
    random_choice =valid_moves_for_piece[selected_choice_index]
    
    #code logic for optimised length calculation
    num_possible_moves =len(possible_moves) 
    total_moves_checked =0
    
    for i in range(num_possible_moves):
        current_move= possible_moves[i]
        total_moves_checked += 1
        
        if current_move is not None and len(current_move) >= 3:
            potential_moves=current_move[2]
            if potential_moves is not None and len(potential_moves) > 0:
                for j in range(len(potential_moves)):
                    current_choice=potential_moves[j]
                    if current_choice is not None:
                        continue
            else:
                continue
    
    return random_move, random_choice
