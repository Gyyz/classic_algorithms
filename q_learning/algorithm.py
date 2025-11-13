import random

class TinyChainEnv:
    """A tiny MDP with 4 states, 2 actions, terminal at state 3."""
    def __init__(self):
        self.n_states = 4
        self.n_actions = 2  # 0: left, 1: right
        self.reset()

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        s = self.state
        if action == 1:  # right
            ns = min(3, s + 1)
        else:  # left
            ns = max(0, s - 1)
        reward = 1.0 if ns == 3 else -0.01
        done = ns == 3
        self.state = ns
        return ns, reward, done

def q_learning(env, episodes=200, alpha=0.5, gamma=0.95, epsilon=0.1):
    Q = [[0.0 for _ in range(env.n_actions)] for _ in range(env.n_states)]
    for _ in range(episodes):
        s = env.reset()
        done = False
        while not done:
            if random.random() < epsilon:
                a = random.randrange(env.n_actions)
            else:
                a = max(range(env.n_actions), key=lambda k: Q[s][k])
            ns, r, done = env.step(a)
            best_next = max(Q[ns])
            Q[s][a] += alpha * (r + gamma * best_next - Q[s][a])
            s = ns
    return Q

if __name__ == "__main__":
    env = TinyChainEnv()
    Q = q_learning(env)
    print("Learned Q-table:")
    for s in range(env.n_states):
        print(s, Q[s])