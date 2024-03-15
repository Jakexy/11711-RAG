Faculty: Louis-Philippe Morency
Title: Continual Learning for Personalized Co-Speech Gesture Generation
Abstract: Co-speech gestures are a key channel of human communication, making them important for personalized chat agents to generate. In the past, gesture generation models assumed that data for each speaker is available all at once, and in large amounts. However in practical scenarios, speaker data comes sequentially and in small amounts as the agent personalizes with more speakers, akin to a continual learning paradigm. While more recent works have shown progress in adapting to low-resource data, they catastrophically forget the gesture styles of initial speakers they were trained on. Also, prior generative continual learning works are not multimodal, making this space less studied. In this paper, we explore this new paradigm and propose C-DiffGAN: an approach that continually learns new speaker gesture styles with only a few minutes of per-speaker data, while retaining previously learnt styles. Inspired by prior continual learning works, C-DiffGAN encourages knowledge retention by 1) generating reminiscences of previous low-resource speaker data, then 2) crossmodally aligning to them to mitigate catastrophic forgetting. We quantitatively demonstrate improved performance and reduced forgetting over strong baselines through standard continual learning measures, reinforced by a qualitative user study that shows that our method produces more natural, style-preserving gestures. Code and videos can be found at https://chahuja.com/cdiffgan
Year: 2023
Authors: Chaitanya Ahuja, Pratik Joshi, Ryo Ishii, Louis-Philippe Morency
Publication ID: 7654260e-79f9-45c5-9663-d72027cf88f3
Publication Name: IEEE International Conference on Computer Vision
Publication Type: conference
Publication Alternate Names: ICCV, IEEE Int Conf Comput Vis, ICCV Workshops, ICCV Work
Publication Url: https://ieeexplore.ieee.org/xpl/conhome/1000149/all-proceedings
