Faculty: Yiming Yang
Title: DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization
Abstract: Neural network-based Combinatorial Optimization (CO) methods have shown promising results in solving various NP-complete (NPC) problems without relying on hand-crafted domain knowledge. This paper broadens the current scope of neural solvers for NPC problems by introducing a new graph-based diffusion framework, namely DIFUSCO. Our framework casts NPC problems as discrete {0, 1}-vector optimization problems and leverages graph-based denoising diffusion models to generate high-quality solutions. We investigate two types of diffusion models with Gaussian and Bernoulli noise, respectively, and devise an effective inference schedule to enhance the solution quality. We evaluate our methods on two well-studied NPC combinatorial optimization problems: Traveling Salesman Problem (TSP) and Maximal Independent Set (MIS). Experimental results show that DIFUSCO strongly outperforms the previous state-of-the-art neural solvers, improving the performance gap between ground-truth and neural solvers from 1.76% to 0.46% on TSP-500, from 2.46% to 1.17% on TSP-1000, and from 3.19% to 2.58% on TSP10000. For the MIS problem, DIFUSCO outperforms the previous state-of-the-art neural solver on the challenging SATLIB benchmark.
Year: 2023
Authors: Zhiqing Sun, Yiming Yang
Publication ID: d9720b90-d60b-48bc-9df8-87a30b9a60dd
Publication Name: Neural Information Processing Systems
Publication Type: conference
Publication Alternate Names: Neural Inf Process Syst, NeurIPS, NIPS
Publication Url: http://neurips.cc/