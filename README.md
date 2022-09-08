# bicycle_model
In This project, we will implement the **Kinematic Bicycle Model** for a forward and backward steering car (each case in separate model). To simulate the model behavior we use turtlesim node in ROS.
The **Kinematic Bicycle Model** equations are:
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

Model Inputs:
  - The time of simulation
  - The car velocity
  - The steering angle(**δ**)

The variable that stored in .yaml file :
  - The distance between CG and front wheel(**lf**)
  - The distance between CG and back wheel(**lr**)
