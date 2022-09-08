# bicycle_model
In This project, we will implement the **Kinematic Bicycle Model** for a forward and backward steering car (each case in separate model). To simulate the model behavior we use turtlesim node in ROS.
The **Kinematic Bicycle Model** equations are:

$$ \dot x = \nu \cos(\theta + \beta) $$

$$ \dot y = \nu \sin(\theta + \beta) $$

$$ \dot \theta = {\nu \tan\delta\cos\beta \over L} $$

$$ \beta = \tan^{-1}({l_r \tan\delta \over L}) $$

Model Inputs:
  - The time of simulation
  - The car velocity
  - The steering angle($$ **\delta** $$)

The variable that stored in .yaml file :
  - The distance between CG and front wheel(**lf**)
  - The distance between CG and back wheel(**lr**)
