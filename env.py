import numpy as np
import gym
import pybullet as p
import pybullet_envs
#import pybullet_envs.bullet.minitaur_gym_env as minitaur_gym_env
#import pybullet_envs.bullet.racecarGymEnv as racecarGymEnv
#import pybullet_envs.bullet.kukaGymEnv as kukaGymEnv
#from custom_envs.minitaur_duck import MinitaurDuckBulletEnv
#from custom_envs.minitaur_ball import MinitaurBallBulletEnv
from human_following_robot.env.hfr_env_base import HumanFollowingRobotBaseEnv
import os
import yaml


def make_env(env_name, seed=-1, render_mode=False):
  if (env_name.startswith("RacecarBulletEnv")):
    print("bullet_racecar_started")
    env = racecarGymEnv.RacecarGymEnv(isDiscrete=False, renders=render_mode)
  elif (env_name.startswith("RocketLander")):
    from box2d.rocket import RocketLander
    env = RocketLander()
  elif (env_name.startswith("BipedalWalker")):
    if (env_name.startswith("BipedalWalkerHardcore")):
      from box2d.biped import BipedalWalkerHardcore
      env = BipedalWalkerHardcore()
    else:
      from box2d.biped import BipedalWalker
      env = BipedalWalker()
  elif (env_name.startswith("MinitaurBulletEnv")):
    print("bullet_minitaur_started")
    env = minitaur_gym_env.MinitaurBulletEnv(render=render_mode)
  elif (env_name.startswith("MinitaurDuckBulletEnv")):
    print("bullet_minitaur_duck_started")
    env = MinitaurDuckBulletEnv(render=render_mode)
  elif (env_name.startswith("MinitaurBallBulletEnv")):
    print("bullet_minitaur_ball_started")
    env = MinitaurBallBulletEnv(render=render_mode)
  elif (env_name.startswith("CartPoleSwingUp")):
    print("cartpole_swingup_started")
    from custom_envs.cartpole_swingup import CartPoleSwingUpEnv
    hard = env_name.startswith("CartPoleSwingUpHard")
    env = CartPoleSwingUpEnv(hard=hard)
  elif (env_name.startswith("KukaBulletEnv")):
    print("bullet_kuka_grasping started")
    env = kukaGymEnv.KukaGymEnv(renders=render_mode,isDiscrete=False)
  elif (env_name.startswith('HFR')):
    hfr_config_file = os.path.join('log', 'hfr_config.yaml')
    with open(hfr_config_file, 'r') as f:
      hfr_config = yaml.load(f)
      print(hfr_config)
    env = HumanFollowingRobotBaseEnv(
      target_distance_min=hfr_config['target_distance_min'],
      target_distance_max=hfr_config['target_distance_max'],
      target_angle_max=hfr_config['target_angle_max'],
      keep_distance=hfr_config['keep_distance'],
      max_steps=hfr_config['max_steps'],
      time_step=hfr_config['time_step'],
      action_repeat=hfr_config['action_repeat'],
      traj_deviation_penalty=hfr_config['traj_deviation_penalty'],
      jnt_accelerate_penalty=hfr_config['jnt_accelerate_penalty'],
      hip_traj_deviation_weight=hfr_config['hip_traj_deviation_weight'],
      base_height_weight=hfr_config['base_height_weight'],
      use_traj=hfr_config['use_traj'],
      use_ref_pose=hfr_config['use_ref_pose'],
      max_allowed_deviation=hfr_config['max_allowed_deviation'],
      smooth_k_action=hfr_config['smooth_k_action'],
      rand_flip_obs=hfr_config['rand_flip_obs'],
      symmetric_action_weight=hfr_config['symmetric_action_weight'],
      torque_control=hfr_config['torque_control'],
      render=False)
    print('human following robot started')
  else:
    if env_name.startswith("Roboschool"):
      import roboschool
    env = gym.make(env_name)
    if render_mode and not env_name.startswith("Roboschool"):
      env.render("human")
  if (seed >= 0):
    env.seed(seed)
  '''
  print("environment details")
  print("env.action_space", env.action_space)
  print("high, low", env.action_space.high, env.action_space.low)
  print("environment details")
  print("env.observation_space", env.observation_space)
  print("high, low", env.observation_space.high, env.observation_space.low)
  assert False
  '''
  return env
