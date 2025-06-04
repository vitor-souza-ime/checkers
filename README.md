# Checkers Game with Q-Learning Agent

## Overview
This project implements a Checkers (Draughts) game in Python, featuring a Q-Learning agent that learns to play against a random opponent. The game is developed using object-oriented programming and includes a graphical visualization of the training progress. The Q-Learning algorithm enables the agent to improve its gameplay over time by learning optimal moves based on rewards.

## Files
- **main.py**: The main script containing the implementation of the Checkers game and the Q-Learning agent. It includes classes for the game board (`Checkers`) and the agent (`QLearningAgent`), along with functions to train the agent and simulate a game.
- **q_table.pkl**: A file generated after training to store the Q-table, which contains the learned state-action values.

## Requirements
To run this project, you need the following Python libraries:
- `numpy`
- `matplotlib`
- `pickle`

Install the dependencies using:
```bash
pip install numpy matplotlib

How It Works

Game Mechanics:

The Checkers class initializes an 8x8 board with black ('b') and white ('w') pieces, following standard American Checkers rules.
Pieces move diagonally, with captures by jumping over opponent pieces. Regular pieces can become kings ('B' or 'W') upon reaching the opponent's end.
The game alternates between players, with black ('b') starting. The game ends when one player has no pieces or valid moves, declaring the other as the winner.


Q-Learning Agent:

The QLearningAgent class implements a Q-Learning algorithm with parameters:
alpha (learning rate): 0.1
gamma (discount factor): 0.9
epsilon (exploration rate): 0.1


The agent learns by playing against a random opponent, updating its Q-table based on rewards:
+1 for a capture move
+10 for winning
-10 for the opponent winning


The Q-table maps states (board configurations) to actions (valid moves) and their expected rewards.


Training:

The agent is trained over 1000 episodes using the play_game function, where it plays against a random opponent.
Training progress is visualized using a plot of total rewards per episode.


Demonstration:

After training, the play_and_show_game function simulates a game, displaying the board and moves for both players.
The Q-table is saved to q_table.pkl for future use.



Usage

Clone the repository:
git clone <repository-url>
cd <repository-directory>


Run the main script:
python main.py


The script will:

Train the Q-Learning agent for 1000 episodes.
Display training progress every 100 episodes.
Plot the total rewards per episode.
Simulate and display a demonstration game.
Save the Q-table to q_table.pkl.



Example Output
During training, you will see:
Episódio 0, Recompensa Total: -10
Episódio 100, Recompensa Total: 3
...

After training, a plot shows the agent's learning progress. During the demonstration game, the board is printed after each move, e.g.:
  0 1 2 3 4 5 6 7
0   w   w   w   w
1 w   w   w   w
...
Jogador Pretas moveu: (5, 1, 4, 2)
Partida terminou! Vencedor: b

Notes

The Q-Learning agent uses an epsilon-greedy strategy to balance exploration and exploitation.
The board state is represented as a string concatenation of the 8x8 grid for simplicity, which may lead to a large Q-table for complex games. Future improvements could include state compression or neural network-based Q-value approximation (e.g., Deep Q-Learning).
The random opponent makes moves uniformly from valid moves, providing a baseline for training. For better performance, consider training against a stronger opponent, such as a Minimax-based agent.
The project is inspired by reinforcement learning concepts from sources like the UC Berkeley Pacman AI projects and checkers reinforcement learning implementations.

Future Improvements

Implement a graphical user interface (e.g., using Pygame) for interactive gameplay.
Enhance the Q-Learning agent with Deep Q-Learning or Monte Carlo Tree Search for better scalability.
Add support for playing against a human or a stronger AI opponent (e.g., Minimax with alpha-beta pruning).
Optimize the Q-table storage to handle the large state space of checkers.

License
This project is licensed under the MIT License. See the LICENSE file for details.




