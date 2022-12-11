# Engineering thesis notepad #

This document will contain all of my sketches etc...

Each chapter consists of:
- Quick introduction:
  Introduction aims to summarize the general topic of this chapter
  
- Bullet-points of the most important topics
  Each bullet needs to be later expanded into a paragraph
  
- Additional information about this topic
  Important notes specific to this chapter and/or topic


## Chapter 1: Introduction

The first chapter aims to introduce the reader to the concept of the
CPU and platform simulation. How it can be used in the fast growing Internet of Things
industry. What benefits it brigs, and why should anybody even care.

__Contents__
1. Introduction
2. Motivation and goal of the thesis
3. Aim of the thesis
4. Thesis organization

### Idea bullet point list ###

#### 1. Introduction ####
- Platform simulation is an essential task in various embedded system design steps (especially for multi node scale)
- In particular interactions with an outside peripherals such as serial protocol devices,i2c,spi....
- This helps embedded developers to develop apps quicker, without a need to have the device nearby
- Detaching from hardware, and moving into software allows us to integrate embedded systems into the CI pipelines
- Using simulators instead of hardware introduces additional complexity

#### 2. Motivation and goals of the thesis ####
- Translation based CPU simulators translate code to a host architecture, and __EXECUTES IT__!
  - A possible solution to this to use __INTERPRETER__ simulator
  - This greatly increases the complexity
  
- Growing complexity of translation based simulators
  TCG... Caching... hard to maintain and develop on
  
- The state of the art CPU simulation is locked behind a restrictive license
  Analyze how easy it will be to create an API to an established CPU simulator to use it
  in the whole system simulation platform

#### 3. Aim of the thesis ####

Describe the main goal of the thesis: 

Analyze performance differences of the translation based CPU simulation and interpreter based CPU simulators on a
various workloads
- Control devices
- Multi-node internet of things systems
- Higher complexity binaries (TensorFlow Lite...)

All this while providing execution analysis, debugging, tracing, etc...


Intermediate goals:
- Familiarize themselves with existing embedded system emulation solutions
- Describe the process of simulation based on machine code translation or interpretation
- Implement test software, e.g. PID controller, and higher complexity embedded applications for measurement purposes
- Analyze the correctness of emulation based on different approaches

#### 4. Thesis organization ####

How will the document will be divided:
- Chapter 2: Translation CPU simulation
- Chapter 3: Interpretation CPU simulation
- Chapter 4: Implementation of Interpretation based simulator in the place of the Translation based one (renode)
- Chapter 5: Benchmarks, graphs etc...
- Chapter 6: Future works / summary / etc...