```markdown
# Checkers Q-Learning Agent (main.py)

This Python script implements a Checkers (Draughts) game with an AI agent trained using Q-Learning reinforcement learning.

## Overview

- **Game Logic:** The `Checkers` class manages the board, piece movements, captures, king promotion, turn switching, and game-over conditions.
- **AI Agent:** The `QLearningAgent` class implements a Q-table-based agent using ε-greedy policy for action selection and Q-value updates.
- **Training:** The script runs 1,000 training episodes where the agent plays against a random-move opponent.
- **Visualization:** Training progress is plotted using matplotlib, showing total rewards per episode.
- **Demonstration:** After training, the script simulates and prints a full game with step-by-step board states.

## How to Run

1. Ensure dependencies are installed:
   ```
   pip install numpy matplotlib
   ```
2. Run the script:
   ```
   python main.py
   ```
3. The training progress graph will be displayed.
4. A demonstration game will be played and printed to the console.

## File Structure Context

- This script is intended as the main entry point of the project, typically named `main.py`.
- It contains all core functionality: game rules, agent logic, training loop, and demonstration.
- For larger projects, consider splitting classes into separate modules and importing them here.

## Key Points

- The script uses the standard Python idiom for executable scripts:
  ```
  if __name__ == "__main__":
      # training and demonstration code
  ```
- The Q-table is saved to `q_table.pkl` after training for reuse or analysis.
- The agent learns by receiving positive rewards for capturing moves and winning, and negative rewards if the opponent wins.

## Dependencies

- Python 3.6+
- numpy
- matplotlib
- pickle (standard library)

## Summary

`main.py` serves as the centralized script to train and demonstrate a reinforcement learning agent playing Checkers, combining game mechanics and AI in a single executable file.
```

[1] https://docs.python.org/3/library/__main__.html
[2] https://docs.python-guide.org/writing/structure/
[3] https://discuss.python.org/t/describe-python-project-structure/28959
[4] https://www.reddit.com/r/learnpython/comments/seu5l6/what_is_the_correct_way_to_structure_your_files/
[5] https://docs.industrial-operations-x.siemens.cloud/r/en-us/technology-module-tm-npu-manual/programming/sequence-and-procedures/main.py-structure-and-setup/structure-of-the-main.py-script-file
[6] https://retailtechinnovationhub.com/home/2024/2/29/the-ultimate-guide-to-structuring-a-python-package
[7] https://www.geeksforgeeks.org/usage-of-__main__-py-in-python/
[8] https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
