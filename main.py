from microbit import *

# Game State Constants
STATE_MENU = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2

# Initialize Game State
game_state = STATE_MENU

while True:
    if button_a.is_pressed():
        game_state = STATE_PLAYING
    elif button_b.is_pressed():
        game_state = STATE_GAME_OVER
        # Check if the player has won
        if player_score >= WINNING_SCORE:
            game_state = STATE_GAME_OVER
            game_won = True
            # Initialize Player Score
            player_score = 0
            # Display Game Over Message
            if game_state == STATE_GAME_OVER:
                if game_won:
                    display.scroll("You won!")
                else:
                    display.scroll("Game Over")
                    # Create a custom sprite for a character
                    player_sprite = Image("05050:"
                                          "05050:"
                                          "05050:"
                                          "99999:"
                                          "09990:")
