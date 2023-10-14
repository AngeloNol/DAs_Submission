#  ROS - Forward Kinematics of a DDMWR/Assigment 1 - Angelo Nolasco
# Description of the problem and Solution
* The goal of the was to implement a differential driver forward kinematics of a robot to determine the pose.
* First we need a file that got the robot left and right velocity and then publish it. The other file would get those input and the input from the pose2d it publish. Then calculated the pose using the forward kinematic equations.
# Brief description of code
* The first python file was the driver, it would publish the cmd_vel for the left and right. Which got its value using a random number generator. The second python file was the simulator, where it had a publisher and subscriber. The pushblisher would publish the pose2d values, and subscriber got the left and right values from the driver. Then the simulator would calcalute the pose of the robot.
# Instruction to excute the assignment
* To excute the assigment we need two file one that was driver and the other simulator. Where the driver would get the input for the left and right velocity. The simulator would calculate the pose of the robot
# Screenshot
./images
* without launch
  ![Screenshot from 2023-10-13 17-16-12](https://github.com/AngeloNol/DAs_Submission/assets/98061732/3b533566-c81b-4130-bd3f-56bdd0062b47)
  * with launch
    ![Screenshot from 2023-10-13 17-21-58](https://github.com/AngeloNol/DAs_Submission/assets/98061732/35183342-8633-471a-b029-e687dfcfdc66)
# Student Info
* Student Name: Angelo Nolasco
* Student Email: Nolasco@unlv.nevada.edu
* youtube link DAs: https://youtu.be/pbceOYqwSmo


