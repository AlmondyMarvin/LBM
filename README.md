# LBM
A Lattice Boltzmann based code to simulate simple 2-D fluid flow over an obstacle.


## Introduction
Lattice Boltzman is a  method that is based on kinetic theory

#### Advantages of LBM
*Algorithm is relatively simple.
*Relatively simpler to paralellize when compared to traditional CFD.
*Suitable for multi-phase flow.

#### Disadvantages of LBM
*Not suitable for high Reynolds Numbers and consequently not good for compressible flow.

## Algorithm & Code

## Results


<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/152075478-80b5f972-3c27-4340-8027-6ac7b1d5b143.png"> 
  <b></b><br>
  <a href="#">Figure 1: Vorticity at Re=72</a>
  <br><br>

</p>


  
<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/152075152-bbf5ab45-2c9f-4ffb-9f26-073cbb094fc6.png">
    <b></b><br>
  <a href="#">Figure 2: Velocity field at Re=72</a>
  <br><br>
</p>


### Future plans to improve the code
* Set up different initial perturbations.
* Reduce memory usage by storing pre-collision and post-collision distribution function in a single variable (F).
* Try different obstacles including streamlined shapes (i.e. airfoils).
* Calculate C<sub>D</sub> & C<sub>L</sub> and compare it to literature value.
* Try having a spinning obstacle.
* Simulate other field variables such as heat.

## References
[1] T. Krüger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva and E. M. Viggen, The Lattice Boltzmann Method, Springer, 2017. 


