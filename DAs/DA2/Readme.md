#  ROS - Inverse Kinematics of DDMWR/Assigment 2 - Angelo Nolasco
# Description of the problem and Solution
* The goal of the was to implement a inverse differential driver kinematics of a robot to determine the pose.
* First we need a file that got the robot pose and then publish it. The other file would get those input and the input from the pose2d it publish and current pose, and also publish the cmd_vel. Then calculated the pose using the inverse kinematic equations.
# Brief description of code
* The first python file was the driver, it would publish the pose. Which got its value using a random number generator. The second python file was the controller, where it had a publish. The pushblisher would publish the pose2d values, and the cmd_vel. Then the controller would calcalute the pose of the robot.
# Instruction to excute the assignment
* To excute the assigment we need two file one that was driver and an controller. Where the driver would pusblish the pose. The controller would publish the current pose and pusblish the cmd_vel, and also calculate the differential driver inverse kinematics. 
# Screenshot
https://github.com/AngeloNol/DAs_Submission/tree/main/DAs/DA1/images
* without launch

* with launch
  
# Student Info
* Student Name: Angelo Nolasco
* Student Email: Nolasco@unlv.nevada.edu
* youtube link DAs:


