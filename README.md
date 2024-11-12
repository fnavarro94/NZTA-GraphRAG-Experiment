# NZTA-GraphRAG-Experiment

**Graph Retrieval Augmented Generative Chatbot Prototype**

A prototype chatbot developed for the New Zealand Transport Agency (NZTA), leveraging graph-based retrieval methods to provide intelligent and contextually relevant responses.

## Table of Contents


## Introduction



## Setup

### Python Version

This project requires **Python 3.11**. Ensure that you have Python 3.11 installed on your system before proceeding with the setup.

You can verify your Python version by running:

```bash
python --version
```


### 1. Clone the Repository

Clone the repository using Git:

```{bash}
git clone https://github.com/fnavarro94/NZTA-GraphRAG-Experiment.git
```


Navigate to the `NZTA-GraphRAG-Experiment` directory:

```{bash}
cd NZTA-GraphRAG-Experiment
```

Copy the example environment file:

```{bash}
cp .env.example .env
```

Fill the entries with your actuall api keys. For example:

```{dotenv}
# .env
GROQ_API_KEY=gsk_mxIlbadQCwoILqI9wHk3dW3ddG3bzdP4lrXGubHj8
OPEN_AI_API_KEY=sk-proj-UUWWdf-T6DGoX12dBoep6sKAtOrKyX9qJ8k7TsU1Xg11QtuV6zWb0nM6V3s74yCE3-dURUNqSttL4A
REPLICATE_API_KEY=r8_IUhhBdITsdfogG6fdsWCirp0PWpsVs
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=nzta_neo4j
NEO4J_URL=bolt://localhost:7687
NEO4J_DATABASE=neo4j
```

