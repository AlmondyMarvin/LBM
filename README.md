# LBM
A Lattice Boltzmann based code to simulate simple 2-D fluid flow over an obstacle.

## Introduction
Lattice Boltzman is a  method that is based on kinetic theory which is a fairly new model to simulate fluid flow. Lattice Boltzman Method (LBM) a successor of the Lattice Gas Models (LGM) which track the position of particles in a "lattice", particles interact through streaming/collision accounting for continuity and momentum equations to reproduce gas behaviour, LGM's nodes in a lattice have different possible directions where a particle could go after the collision/streaming step. Main drawback of the LGM is that there was statistical noise, meaning that macroscopic quantities like velocity or density fluctuate even for gas at equilibrium. The development of the LBM was to improve upon the LGM to be able to simulate fluids and minimize its deficiencies. An early LGM lattice is shown in Figure 1, developed in 1973.

<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/154354045-f7f14715-4924-464d-999e-b05f8101fed9.png">
    <b></b><br>
  <a href="#">Figure 1: Lattice with 2 particles colliding [1] </a>
  <br><br>
</p>


While the LGM tracked each of the particles in a lattice, the LBM in a similar manner tracks the distribution of particles using a mesoscopic scale. Lattice Boltzmann method, as the name says uses the mesoscopic Maxwell-Boltzmann equation to describe fluid dynamics on a macroscale, the Boltzmann distribution equation describes the probability of molecules to have a certain speed. The discretized Lattice Boltzmann equation in velocity, space and time is as follows:



<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/154356963-737e40bf-95cb-47a6-b039-2e89f8a30855.gif">
    <b></b><br>
  <br><br>
</p>


This code was based on the D2Q9 lattice structure with direction and velocities as shown in Figure 2.

<sub>More information about LBM will be added once more literature review is done.</sub>

<p align="center">
<img src="https://www.researchgate.net/profile/Tobias-Weinzierl/publication/267248395/figure/fig2/AS:667619816378377@1536184376538/The-Lattice-Boltzmann-algorithm-for-the-D2Q9-model-In-the-collide-step-the.png">
    <b></b><br>
  <a href="#">Figure 1: Lattice [2] </a>
  <br><br>
</p>

<p align="center">
<img src="https://www.researchgate.net/publication/335459626/figure/fig1/AS:797057413570561@1567044704340/Diagram-of-D2Q9-Model.ppm" style="width:200px;">
    <b></b><br>
  <a href="#">Figure 1: D2Q9 and its lattice velocities [3] </a>
  <br><br>
</p>

#### Advantages of LBM [4]
* Algorithm is relatively simple.
* Relatively simpler to paralellize when compared to traditional CFD.
* Suitable for multi-phase flow.
* Mesh-free

#### Disadvantages of LBM [4]
* Not suitable for high Reynolds Numbers and consequently not good for compressible flow, particles can only move 1 lattice step per unit time. 
* Cannot handle low viscosities.
* Unproven for high Knudsen numbers.
* Lack Galilean invariance, i.e. Newton's law do not change depending on the inertial frame.

## Algorithm & Code

![Algorithm flowchart example](https://user-images.githubusercontent.com/98285490/152614772-256ca5d6-3105-4328-b0c6-9e742f62f6e3.png)



## Results






  
<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/153093882-861e4ec5-4562-418b-9ff2-6b2ebe463b59.gif">
    <b></b><br>
  <a href="#">Figure 3: Velocity field at Re=72</a>
  <br><br>
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/153099197-0e7e781a-9f94-428b-bfbe-2f97dc157a7b.gif"> 
  <b></b><br>
  <a href="#">Figure 4: Vorticity at Re=72</a>
  <br><br>

</p>



### Future plans to improve the code
* Set up different initial perturbations.
* ~~Reduce memory usage by storing pre-collision and post-collision distribution function in a single variable (F).~~ **Implementd using the pull algorithm with slight computation time improvement of ~2s, from an average of 33.15s to 31.24s.**
* Reduce the lack of Galilean invariance through the use of different collision operators, i.e MRT collision operator. 
* Try different obstacles including streamlined shapes (i.e. airfoils).
* Calculate C<sub>D</sub> & C<sub>L</sub> and compare it to literature value.
* Try having a spinning obstacle.
* Simulate other field variables such as heat.


## References (Need to be updated)

https://www.researchgate.net/figure/The-head-on-collision-rule-for-the-HPP-model_fig3_242162544

[1] T. Krüger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva and E. M. Viggen, The Lattice Boltzmann Method, Springer, 2017. 

[2]	P. Neumann, H.-J. Bungartz, M. Mehl and T. W. T. Neckel, "A Coupled Approach for Fluid Dynamic Problems Using the PDE Framework Peano," Garching, 2012.

[3] https://www.researchgate.net/figure/Diagram-of-D2Q9-Model_fig1_335459626

[4] D. Elsworth, "The Lattice Boltzmann Method (EGEE520)," State College, 2016.


