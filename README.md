# Codsoft Internship Projects

This repository contains the assignments I completed during my virtual internship at Codsoft. Over the course of one month, I was assigned three projects to develop: a Chatbot, a Tic-Tac-Toe game, and an Image Caption Generator. Each project showcases different AI and algorithmic techniques.

## Projects Overview

### 1. Chatbot

A simple rule-based chatbot developed using `if-else` statements. It responds to predefined inputs, making it easy to demonstrate basic chatbot functionality.

- **Techniques Used:** Rule-based logic (if-else).
- **Languages Used:** Python.
- **Capabilities:** The chatbot can engage in basic conversations by recognizing keywords and responding accordingly.

### 2. Unbeatable Tic-Tac-Toe

An AI-driven Tic-Tac-Toe game built using the Minimax algorithm. This version of the game is unbeatable as the AI always makes optimal moves.

- **Techniques Used:** Minimax algorithm with pruning.
- **Languages Used:** Python.
- **Features:**
  - The game is fully interactive.
  - AI always plays optimally, making it impossible for the player to win.

### 3. Image Caption Generator

A neural network-based model that generates captions for images. The model uses a Convolutional Neural Network (CNN) for feature extraction from the images and a Long Short-Term Memory (LSTM) network for generating the captions based on the extracted features.

- **Techniques Used:**
  - CNN for feature extraction.
  - LSTM for sequence modeling and caption generation.
- **Libraries:** TensorFlow, Keras.
- **Dataset:** Used pre-trained models and a dataset of labeled images (e.g., MS COCO dataset).
- **Workflow:**
  1. CNN extracts features from the input image.
  2. LSTM generates a sequence of words (captions) based on the extracted features.
## Future Improvements
- Expand the Chatbot to include Natural Language Processing (NLP) techniques for more dynamic and context-aware conversations.
- Train the Image Caption Generator on a custom dataset to fine-tune the model and enhance the accuracy of generated captions.
- Explore the use of Transformer-based models for the Image Caption Generator to compare performance with the current CNN-LSTM approach.
