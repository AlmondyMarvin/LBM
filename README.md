# LBM
A Lattice Boltzmann based code to simulate simple 2-D fluid flow over an obstacle.


## Introduction
Lattice Boltzman is a  method that is based on kinetic theory that instead of simulating a continuum flow like in traditional CFD it simulates molecules in a "latice" where particles collide and stream, , as shown in Figure 1.  

<sub>More information about LBM will be added once more literature review is done.</sub>

<p align="center">
<img src="https://www.researchgate.net/profile/Tobias-Weinzierl/publication/267248395/figure/fig2/AS:667619816378377@1536184376538/The-Lattice-Boltzmann-algorithm-for-the-D2Q9-model-In-the-collide-step-the.png">
    <b></b><br>
  <a href="#">Figure 1: Lattice [1] </a>
  <br><br>
</p>

#### Advantages of LBM [3]
* Algorithm is relatively simple.
* Relatively simpler to paralellize when compared to traditional CFD.
* Suitable for multi-phase flow.
* Mesh-free

#### Disadvantages of LBM [3]
* Not suitable for high Reynolds Numbers and consequently not good for compressible flow, particles can only move 1 lattice step per unit time. 
* Cannot handle low viscosities.
* Unproven for high Knudsen numbers.

## Algorithm & Code
[![](https://mermaid.ink/img/pako:eNpVkE1qw0AMha8itEohvoAXhcZOsgmk0Ow8WQiPnBmS-WEsU4Ltu3ccU2i1kt77nhAasQ2ascRbomjgUisPuT6ayiTbi6P-CkXxPh1ZwAXPzwl2m2OA3oQYrb-9rfxugaAaTwvGIMb6-7xa1St_9jxB3ZwoSojXv87lO0ywb-ynyev_OyZxTh2ajsqOipYSVJReCG7RcXJkdT59XBSFYtixwjK3mjsaHqJQ-TmjQ9QkvNdWQsJS0sBbpEHC19O3v_PK1JbyI9wqzj8k-lxH)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpVkE1qw0AMha8itEohvoAXhcZOsgmk0Ow8WQiPnBmS-WEsU4Ltu3ccU2i1kt77nhAasQ2ascRbomjgUisPuT6ayiTbi6P-CkXxPh1ZwAXPzwl2m2OA3oQYrb-9rfxugaAaTwvGIMb6-7xa1St_9jxB3ZwoSojXv87lO0ywb-ynyev_OyZxTh2ajsqOipYSVJReCG7RcXJkdT59XBSFYtixwjK3mjsaHqJQ-TmjQ9QkvNdWQsJS0sBbpEHC19O3v_PK1JbyI9wqzj8k-lxH)

## Results


<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/152075478-80b5f972-3c27-4340-8027-6ac7b1d5b143.png"> 
  <b></b><br>
  <a href="#">Figure 2: Vorticity at Re=72</a>
  <br><br>

</p>


  
<p align="center">
<img src="https://user-images.githubusercontent.com/98285490/152075152-bbf5ab45-2c9f-4ffb-9f26-073cbb094fc6.png">
    <b></b><br>
  <a href="#">Figure 3: Velocity field at Re=72</a>
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
[1]	P. Neumann, H.-J. Bungartz, M. Mehl and T. W. T. Neckel, "A Coupled Approach for Fluid Dynamic Problems Using the PDE Framework Peano," Garching, 2012.

[2] T. Krüger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva and E. M. Viggen, The Lattice Boltzmann Method, Springer, 2017. 

[3] D. Elsworth, "The Lattice Boltzmann Method (EGEE520)," State College, 2016.


