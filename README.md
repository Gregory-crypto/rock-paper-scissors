# Rock Paper Scissors

In the file `RPS.py` you are provided with a function called `player`. The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). The function will return a string representing the next move for it to play ("R", "P", or "S").

A player function receives an empty string as an argument for the first game in a match since there is no previous play.

The example function in `RPS.py` is defined with five arguments (`player(prev_play`, `prob_matr = [{}]`, `key = [""]`, `guess = [""]`, `counter = [0]`). The function is never called with a 2-5 argumentы so those ones are completely optional. The reason why the examplse function contains a second argument (`prob_matr = [{}]`) is because that is the only way to save state between consecutive calls of the `player` function. You only need the `prob_matr = [{}]` argument if you want to keep track of the opponent_history.

To defeat all four opponents, this program have multiple strategies that change depending on the plays of the opponent.

### Development

`main.py` imports the game function and bots from `RPS_game.py`.

To test your code, play a game with the play function. The play function takes four arguments:

- two players to play against each other (the players are actually functions)
- the number of games to play in the match
- an optional argument to see a log of each game. Set it to `True` to see these messages.
```py
play(player1, player2, num_games, verbose)
```
For example, here is how you would call the function if you want `player` and `quincy` to play 1000 games against each other and you want to see the results of each game:

```py
play(player, quincy, 1000, verbose=True)
```

Click the "run" button and `main.py` will run.

### Testing

The unit tests for this project are in `test_module.py`. We imported the tests from test_module.py to main.py for your convenience. If you uncomment the last line in main.py, the tests will run automatically whenever you hit the "run" button.
