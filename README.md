# Robot Ecommerce Homepage

This repository contains a minimal Vue 3 application that demonstrates a single-page ecommerce homepage for a robot company. Components are loaded asynchronously and styled using Tailwind CSS via CDN. Open `index.html` in a modern browser to view the page.

## AI Cognitive Core

The `aiya_core` directory contains a lightweight prototype of the
AIYA (中文名：AI芽) emotional companion robot backend. It is composed of the
following modules:

- `PersonalityGrowthEngine` – tracks OCEAN personality traits and updates
  them with user feedback.
- `SemanticMemorySystem` – stores conversation fragments and retrieves
  recent events.
- `MultiModalEmotionRecognizer` – placeholder class for analyzing audio
  and video to detect emotions.
- `GrowthDialogueSystem` – generates responses based on personality and
  stored memories.
- `ModuleScheduler` – orchestrates all modules and exposes a `process`
  method to handle user input.

These modules are intended as a starting point for building a more
sophisticated AI companion backend.

Run the demo with:

```bash
python -m aiya_core.example_usage
```
