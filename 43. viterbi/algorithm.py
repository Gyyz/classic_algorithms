def viterbi(obs, states, start_prob, trans_prob, emit_prob):
    """Compute Viterbi path.
    obs: list of observations
    states: list of states
    start_prob: dict[state]
    trans_prob: dict[state][state]
    emit_prob: dict[state][observation]
    """
    dp = []  # list of dict state->(prob, prev_state)
    first = {}
    for s in states:
        first[s] = (start_prob.get(s, 0.0) * emit_prob[s].get(obs[0], 0.0), None)
    dp.append(first)

    for t in range(1, len(obs)):
        cur = {}
        for s in states:
            best = (0.0, None)
            for ps in states:
                prob = dp[t-1][ps][0] * trans_prob[ps].get(s, 0.0) * emit_prob[s].get(obs[t], 0.0)
                if prob > best[0]:
                    best = (prob, ps)
            cur[s] = best
        dp.append(cur)

    # backtrack
    last_state = max(states, key=lambda s: dp[-1][s][0])
    path = [last_state]
    for t in range(len(obs)-1, 0, -1):
        _, prev = dp[t][path[-1]]
        path.append(prev)
    path.reverse()
    return path

if __name__ == "__main__":
    states = ['H', 'C']  # Hot/Cold
    obs = ['1', '2', '3']
    start_prob = {'H': 0.6, 'C': 0.4}
    trans_prob = {'H': {'H': 0.7, 'C': 0.3}, 'C': {'H': 0.4, 'C': 0.6}}
    emit_prob = {'H': {'1': 0.2, '2': 0.4, '3': 0.4}, 'C': {'1': 0.5, '2': 0.4, '3': 0.1}}
    path = viterbi(obs, states, start_prob, trans_prob, emit_prob)
    print("Viterbi path:", path)