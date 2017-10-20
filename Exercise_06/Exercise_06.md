# Problem 2.18

## Question
Calculate the effect of backspin on a fastball. How much does an angular velocity of 1000 rpm (typical for a fastball) affect the trajectory?

## Analysis
We can again use Eular Method to solve:

$$x(i+1)=x(i)+v_x\Delta t$$

$$y(i+1)=y(i)+v_y\Delta t$$

$$v_x(i+1)=v_x(i)-\frac{B_2}{m}vv_x\Delta t$$

The axis of rotation of backspin ball is now horizontal, so that the Magnus force is straight up:

$$v_y(i+1)=v_y(i)+(-g+\frac{S_0}{m}v_x\omega)\Delta t$$

The equations of motion include the effects of atmospheric drag on the largest component of the velocity x, with a velocity dependent coefficient.

$$\frac{B2}{m}=0.0039+\frac{0.0058}{1+exp[(v-v_d)/\Delta]}$$

The ball was thrown with an intial velocity of 70mph in the x direction and was spinning at 1000 rpm.
The green and red curve shows the trajectory of backspin and no spin, and the blue curve shows that of a 95-mph fastball for comparison.


[Codes](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_06/spin.py)

![picture result](https://github.com/Monotone1997/computationalphysics_N2015301020041/blob/master/Exercise_06/backspin.jpg)
