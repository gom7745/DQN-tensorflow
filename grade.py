


"""
### NOTICE ###
You DO NOT need to upload this file.
"""
import sys, random
import tensorflow as tf

from agent import Agent
from environment import ALE

#tf.set_random_seed(123)
#random.seed(123)

seed = int(sys.argv[1])

f = open('log','a')

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3, allow_growth=4)

with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:

    # Init env
    env = ALE(seed)


    # Init agent
    agent = Agent(sess, env.ale.getMinimalActionSet())
    action_repeat, random_init_step, screen_type = agent.getSetting()

    # Set env setting
    env.setSetting(action_repeat, random_init_step, screen_type)

    # Get a new game
    screen = env.new_game()

    print('start playing...')
    # Start playing
    current_reward = 0
    for _ in range(5000):
        action = agent.play(screen)
        reward, screen, terminal = env.act(action)
        current_reward += reward
        if terminal:
            break

    print("seed %d, current_reward %d" % (seed, current_reward))
    f.write("%d,%d\n" % (seed, current_reward))

f.close()
