import random

def group2(self, board):
    possible_moves = self.getPossibleMoves(board)

    if possible_moves is None or len(possible_moves) == 0:
        self.game.end_turn()
        return None, None
    
    best_move = None
    best_choice = None
    best_score = float('-inf')  # Start with the worst possible score

    for move in possible_moves:
        if len(move) < 3 or move[2] is None:
            continue
        
        valid_moves_for_piece = move[2]
        
        if valid_moves_for_piece is None or len(valid_moves_for_piece) == 0:
            continue
        
        for choice in valid_moves_for_piece:
            if valid_move_position(board, move, choice):
                score = evaluate_move(board, move, choice)
                
                if score > best_score:
                    best_score = score
                    best_move = move
                    best_choice = choice
    
    if best_move is None or best_choice is None:
        self.game.end_turn()
        return None, None
    
    return best_move, best_choice

def valid_move_position(board, move, choice):
    """Checks if the move and choice positions are valid on the board."""
    board_size = 8  # Assuming an 8x8 board
    if 0 <= move[0] < board_size and 0 <= move[1] < board_size and \
       0 <= choice[0] < board_size and 0 <= choice[1] < board_size:
        return True
    return False

def evaluate_move(board, move, choice):
    """
    Evaluates a move based on several factors, including capturing pieces, becoming a king,
    and avoiding risky positions in the given circumstance.
    """
    score = 0

    # Factor 1: Capturing opponent's pieces (more captures = higher score)
    if abs(choice[0] - move[0]) > 1:  # This implies a capture
        score += 5
    
    # Factor 2: Becoming a king (reaching the opponent's side)
    if (move[0] == 0 and board.getSquare(move[0], move[1]).squarePiece.color == "GREY") or \
       (move[0] == 7 and board.getSquare(move[0], move[1]).squarePiece.color == "PURPLE"):
        score += 10  # Promote to a king
    
    # Factor 3: Avoiding risky positions (moving into an opponent's potential capture path)
    opponent_color = "PURPLE" if board.getSquare(move[0], move[1]).squarePiece.color == "GREY" else "GREY"
    adjacent_squares = board.getAdjacentSquares(choice[0], choice[1])

    for adj in adjacent_squares:
        # Check if the adjacent square is within bounds
        if 0 <= adj[0] < 8 and 0 <= adj[1] < 8:
            adj_piece = board.getSquare(adj[0], adj[1]).squarePiece
            if adj_piece and adj_piece.color == opponent_color:
                potential_capture_moves = board.get_valid_legal_moves(adj[0], adj[1])
                if potential_capture_moves and choice in potential_capture_moves:
                    score -= 3  # Penalize for being in a risky position
    
    # Factor 4: Blocking opponent's moves
    if len(board.get_valid_legal_moves(choice[0], choice[1])) == 0:
        score += 2  # Block opponent's move
    
    return score  # Return final score after evaluation
