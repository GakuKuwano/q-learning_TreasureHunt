import numpy as np
import matplotlib.pyplot as plt
from maze_env import MazeEnv

#q_table = np.zeros((10, 10, 4))

def update_q_table(_q_table, _action, _state, _next_state, _reward, _episode):
    #Q(s, a) ←  Q(s, a) + α(R(s, a) + γmaxQ(s', a') - Q(s, a))
    alpha = 0.2
    gamma = 0.99

    #行動後の状態で得られる最大行動価値Q(s', a')
    next_position_x, next_position_y = _next_state
    next_max_q_value = max(_q_table[next_position_x][next_position_y])

    #行動前の状態の行動価値Q(s, a)
    position_x, position_y = _state
    q_value = q_table[position_x][position_y][_action]

    #行動価値関数の更新
    _q_table[position_x][position_y][_action] = q_value + alpha * (_reward + gamma * next_max_q_value - q_value)
    
    return _q_table

def get_action(_env, _q_table, _state, _episode):
    #ε-greedy法
    epsilon = 0.002
    if np.random.uniform(0, 1) > epsilon:
        position_x, position_y = state
        _action = np.argmax(_q_table[position_x][position_y])
    else:
        _action = np.random.choice([0, 1, 2, 3])
    return _action

if __name__ == '__main__':
    env = MazeEnv()

    q_table = np.zeros((env.map.shape[1], env.map.shape[0], 4))

    state = env.reset()
    total_episode = 500
    max_step = 200
    time_interval = 100
    rewards = []
    x = []
    y = []

    print("{}episode Learning ...\n".format(total_episode))
    for episode in range(total_episode):
        total_reward = 0
        state = env.reset()

        for time_step in range(max_step):
            if (episode+1)%time_interval == 0 or episode == 0:
                print('\repisode: %d  %dstep  '%(episode+1, time_step+1), end='')
                env.render()
            action = get_action(env, q_table, state, episode)
            next_state, reward, done, _ = env.step(action)

            q_table = update_q_table(q_table, action, state, next_state, reward, episode)
            total_reward += reward

            state = next_state

            if done:
                break
        
        if (episode+1)%time_interval == 0 or episode == 0:
            print('\ntotal_reward: {}'.format(total_reward))
            rewards.append(total_reward)
        x.append(episode)
        y.append(total_reward)

    print('\nFinished!')
    plt.plot(x, y)
    plt.show()

