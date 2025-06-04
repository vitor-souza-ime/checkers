import numpy as np
import random
import pickle
from copy import deepcopy
import matplotlib.pyplot as plt

# Classe para o tabuleiro de damas
class Checkers:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'b'  # Começa com pretas
        self.winner = None

    def initialize_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'w'
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'b'
        return board

    def get_valid_moves(self, player):
        moves = []
        captures = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col].lower() == player:
                    is_king = self.board[row][col].isupper()
                    moves_pos, captures_pos = self.get_moves_for_piece(row, col, is_king, player)
                    moves.extend(moves_pos)
                    captures.extend(captures_pos)
        return captures if captures else moves

    def get_moves_for_piece(self, row, col, is_king, player):
        moves = []
        captures = []
        directions = [(-1, -1), (-1, 1)] if player == 'b' else [(1, -1), (1, 1)]
        if is_king:
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8 and self.board[new_row][new_col] == ' ':
                moves.append((row, col, new_row, new_col))
            jump_row, jump_col = row + 2*dr, col + 2*dc
            if (0 <= jump_row < 8 and 0 <= jump_col < 8 and
                self.board[jump_row][jump_col] == ' ' and
                self.board[row + dr][col + dc].lower() != player and
                self.board[row + dr][col + dc] != ' '):
                captures.append((row, col, jump_row, jump_col))

        return moves, captures

    def make_move(self, move):
        row, col, new_row, new_col = move
        piece = self.board[row][col]
        self.board[new_row][new_col] = piece
        self.board[row][col] = ' '
        if abs(new_row - row) == 2:
            captured_row = (row + new_row) // 2
            captured_col = (col + new_col) // 2
            self.board[captured_row][captured_col] = ' '
        if piece == 'b' and new_row == 0:
            self.board[new_row][new_col] = 'B'
        elif piece == 'w' and new_row == 7:
            self.board[new_row][new_col] = 'W'
        self.current_player = 'w' if self.current_player == 'b' else 'b'

    def is_game_over(self):
        opponent = 'w' if self.current_player == 'b' else 'b'
        if not any(self.board[row][col].lower() == opponent for row in range(8) for col in range(8)):
            self.winner = self.current_player
            return True
        if not self.get_valid_moves(opponent):
            self.winner = self.current_player
            return True
        return False

    def get_state(self):
        return ''.join([''.join(row) for row in self.board])

    def display_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")
        print()

# Classe para o agente Q-Learning
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_action(self, state, valid_moves):
        if random.random() < self.epsilon:
            return random.choice(valid_moves) if valid_moves else None
        state_q = self.q_table.get(state, {})
        if not state_q:
            return random.choice(valid_moves) if valid_moves else None
        return max(state_q.items(), key=lambda x: x[1], default=(None, 0))[0]

    def update(self, state, action, reward, next_state, next_valid_moves):
        state_q = self.q_table.get(state, {})
        next_state_q = self.q_table.get(next_state, {})
        max_next_q = max(next_state_q.values(), default=0)
        state_q[action] = state_q.get(action, 0) + self.alpha * (
            reward + self.gamma * max_next_q - state_q.get(action, 0)
        )
        self.q_table[state] = state_q

# Função para jogar uma partida (usada no treinamento)
def play_game(agent, opponent='random'):
    game = Checkers()
    rewards = []
    while not game.is_game_over():
        state = game.get_state()
        valid_moves = game.get_valid_moves(game.current_player)
        if not valid_moves:
            game.current_player = 'w' if game.current_player == 'b' else 'b'
            continue

        if game.current_player == 'b':
            action = agent.get_action(state, valid_moves)
            if action:
                game.make_move(action)
                reward = 1 if abs(action[2] - action[0]) == 2 else 0
                if game.is_game_over() and game.winner == 'b':
                    reward += 10
                next_state = game.get_state()
                next_valid_moves = game.get_valid_moves('b')
                agent.update(state, action, reward, next_state, next_valid_moves)
                rewards.append(reward)
        else:
            action = random.choice(valid_moves)
            game.make_move(action)
            if game.is_game_over() and game.winner == 'w':
                rewards.append(-10)
    return sum(rewards)

# Função para simular e exibir uma partida pós-treinamento
def play_and_show_game(agent):
    game = Checkers()
    moves = []
    print("Partida de Demonstração:")
    game.display_board()
    i=1

    while not game.is_game_over():
        state = game.get_state()
        valid_moves = game.get_valid_moves(game.current_player)
        print("Partida: "+str(i))
        i=i+1

        if not valid_moves:
            game.current_player = 'w' if game.current_player == 'b' else 'b'
            continue

        if game.current_player == 'b':
            action = agent.get_action(state, valid_moves)
            if action:
                moves.append((state, action))
                game.make_move(action)
                print(f"Jogador Pretas moveu: {action}")
                game.display_board()
        else:
            action = random.choice(valid_moves)
            game.make_move(action)
            print(f"Jogador Brancas moveu: {action}")
            game.display_board()

    print(f"Partida terminou! Vencedor: {game.winner}")
    return moves

# Treinamento do agente
agent = QLearningAgent()
num_episodes = 1000
rewards = []

for episode in range(num_episodes):
    total_reward = play_game(agent)
    rewards.append(total_reward)
    if episode % 100 == 0:
        print(f"Episódio {episode}, Recompensa Total: {total_reward}")

# Plotar o progresso do aprendizado
plt.figure(figsize=(10, 6))
plt.plot(rewards, label='Total Reward Per Episode')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Q-Learning Agent Training Progress')
plt.legend()
plt.show()

# Simular e exibir uma partida após o treinamento
moves = play_and_show_game(agent)

# Salvar a Q-table
with open('q_table.pkl', 'wb') as f:
    pickle.dump(agent.q_table, f)
