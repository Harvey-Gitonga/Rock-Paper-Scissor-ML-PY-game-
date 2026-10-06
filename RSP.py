import random

def player(prev_play, opponent_history=[]):
    # Keep track of opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return "R"

    # Counter the opponent's move
    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    # Use pattern recognition after enough moves
    if len(opponent_history) >= 5:
        pattern_length = 3

        # Look at the last 3 moves
        pattern = "".join(opponent_history[-pattern_length:])

        # Find what usually follows this pattern
        next_moves = []

        for i in range(len(opponent_history) - pattern_length):
            current_pattern = "".join(
                opponent_history[i:i + pattern_length]
            )

            if current_pattern == pattern:
                next_moves.append(
                    opponent_history[i + pattern_length]
                )

        if next_moves:
            # Predict the most common next move
            predicted = max(
                set(next_moves),
                key=next_moves.count
            )

            return counter[predicted]

    # Fallback: counter the opponent's most common move
    most_common = max(
        set(opponent_history),
        key=opponent_history.count
    )

    return counter[most_common]