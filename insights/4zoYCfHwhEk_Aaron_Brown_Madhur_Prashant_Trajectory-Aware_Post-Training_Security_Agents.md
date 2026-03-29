# Aaron Brown & Madhur Prashant - Trajectory-Aware Post-Training Security Agents

**Video ID:** 4zoYCfHwhEk

**YouTube Link:** https://www.youtube.com/watch?v=4zoYCfHwhEk

**Transcript:** [View Transcript](../transcripts/4zoYCfHwhEk_Aaron%20Brown%20%26%20Madhur%20Prashant%20-%20Trajectory-Aware%20Post-Training%20Security%20Agents%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Aaron Brown presents trajectory-aware post-training for security agents, releasing open-source framework Open Trajectory Gym for reinforcement learning-based agent training.

## Key Takeaway
Model post-training enables smaller models to outperform base models on complex security tasks through trajectory learning.

# Insights

## Post-Training Fundamentals
- Base models optimize for general tasks; post-training aligns models to specific security domains like penetration testing.
- Instruction tuning teaches tool-calling format; reinforcement learning trains tactical decision-making through environmental interaction.
- Three-stage pipeline: supervised fine-tuning for format, online RL for trajectory alignment, genetic algorithm for prompts.

## Model Performance Gaps
- Frontier models excel at atomic security tasks like identifying LFI or XSS vulnerabilities individually.
- Multi-stage exploitation requiring vulnerability chaining remains challenging for general models without specialized training.
- Security domain lacks established benchmarks and training frameworks compared to coding or mathematics domains.

## Reinforcement Learning Architecture
- Online RL uses distributed GPU infrastructure: separate nodes for inference, model loading, training, and environment execution.
- Eight parallel agents execute tasks simultaneously, selecting best traces via group mean of composite rewards.
- Progressive difficulty scaling from easy to expert challenges mirrors human learning and improves generalization performance.

## Reward Function Design
- Binary rewards alone insufficient; composite rewards incorporate temporal decay, information sparsity, and uniqueness to differentiate trajectories.
- Every RL environment requires verifiable rewards at completion; CTF flags or CVE numbers provide clear signals.
- Reward functions score exploration quality and noise levels, not just final objective completion, to optimize production behavior.

## Open Trajectory Gym Framework
- Brings together 36+ libraries into single loop for practitioners to apply trajectory-based post-training techniques.
- Supports bring-your-own benchmark, model, and agent frameworks including LangChain, Autogen, and custom scaffolding.
- Synthetic trace generation from teacher models enables distillation from stronger models to smaller, specialized agents.

## Performance Results
- Qwen 3.5 27B improved from 12.5% to 35% solve rate on Cybench after supervised fine-tuning plus RL.
- Trained model solved complex crypto challenge requiring cipher reverse-engineering and oracle interaction in fewer turns.
- Dense models recommended over mixture-of-experts due to open-source weight synchronization limitations in RL training.

## Implementation Lessons
- Long-horizon tasks require large key-value caches; 128K context models need 2-3x VRAM beyond base model size.
- 285 training traces insufficient for robust generalization; 20,000-30,000 traces typically needed for supervised fine-tuning stage.
- Genetic algorithm prompt evolution at test time enables multi-stage objective adaptation without retraining model weights.

## Security Domain Challenges
- Generalization from CTF environments to real-world bug discovery remains unsolved; verifiable rewards in production unclear.
- Better evaluation frameworks and RL environments crucial for security agents to match coding domain maturity level.
- Skillful RL environment design that transfers beyond training scenarios represents current bottleneck for practical deployment.
