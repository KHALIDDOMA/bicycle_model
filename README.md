# bicycle_model
In This project, we will implement the **Kinematic Bicycle Model** for a forward and backward steering car (each case in separate model). To simulate the model behavior we use turtlesim node in ROS.
The **Kinematic Bicycle Model** equations are:
    "\\begin{align*}\n",
    "\\dot{x}_c &= v \\cos{(\\theta + \\beta)} \\\\\n",
    "\\dot{y}_c &= v \\sin{(\\theta + \\beta)} \\\\\n",
    "\\dot{\\theta} &= \\frac{v \\cos{\\beta} \\tan{\\delta}}{L} \\\\\n",
    "\\dot{\\delta} &= \\omega \\\\\n",
    "\\beta &= \\tan^{-1}(\\frac{l_r \\tan{\\delta}}{L})\n",
    "\\end{align*}\n",

Model Inputs:
  - The time of simulation
  - The car velocity
  - The steering angle(**δ**)

The variable that stored in .yaml file :
  - The distance between CG and front wheel(**lf**)
  - The distance between CG and back wheel(**lr**)
