# NZTA-GraphRAG-Experiment

**Code to run the experiment that evaluates the RAG at the node retrieval level and answer level. This code contains the data to load the Neo4j databases and the code required for the evaluation.**

## Table of Contents

1. Introduction
2. Setup
3. Data Loading
4. Evaluation

## Introduction

This project aims to build a Retrieval-Augmented Generation (RAG) system using a knowledge graph created from NZTA OIA documents and SP-CoT data. The experiments evaluate the RAG's performance in node retrieval and answer generation.

## Setup

### Python Version

This project requires **Python 3.11**. Ensure that you have Python 3.11 installed on your system before proceeding with the setup.

You can verify your Python version by running:

```bash
python --version
```

### 1. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/fnavarro94/NZTA-GraphRAG-Experiment.git
```

Navigate to the `NZTA-GraphRAG-Experiment` directory:

```bash
cd NZTA-GraphRAG-Experiment
```

Copy the example environment file:

```bash
cp .env.example .env
```

Fill in the entries with your actual API keys. For example:

```dotenv
# .env
GROQ_API_KEY=gsk_mxIlbadQCwoILqI9wHk3dW3ddG3bzdP4lrXGubHj8
OPEN_AI_API_KEY=sk-proj-UUWWdf-T6DGoX12dBoep6sKAtOrKyX9qJ8k7TsU1Xg11QtuV6zWb0nM6V3s74yCE3-dURUNqSttL4A
REPLICATE_API_KEY=r8_IUhhBdITsdfogG6fdsWCirp0PWpsVs
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=nzta_neo4j
NEO4J_URL=bolt://localhost:7687
NEO4J_DATABASE=neo4j
VIRTUAL_ENV_NAME=nzta_experiment_env
```

### Install Dependencies

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Apply the Patch

Before loading the data into Neo4j, you need to patch the llamaindex files.

1. Ensure that your `.env` file contains the name of your virtual environment:
   - Add the line `VIRTUAL_ENV_NAME=<your_virtual_env_name>` to your `.env` file.

2. Run the patch script:

```bash
python patch.py
```

This script will backup the original `base.py` file and replace it with your patched version.

## Filling the Neo4j Databases

Before proceeding, ensure that you have Neo4j installed and a database set up and running. For detailed setup instructions, please refer to the [NZTA GraphRAG Instructions section 3](https://github.com/fnavarro94/NZTA-GraphRAG/tree/main).

### Loading Data into Neo4j

This project requires **two separate Neo4j databases**: one for the **OIA** data and another for the **SP-CoT** data. You should load the data into each database **one at a time** using the provided Jupyter notebooks:

- To upload the **OIA data**, use:

  ```bash
  kg_loader_oia.ipynb
  ```

- To upload the **SP-CoT data**, use:

  ```bash
  kg_loader_sp_cot.ipynb
  ```

Make sure your Neo4j instance is running and your `.env` file is correctly configured before executing these notebooks. Also, ensure you stop the current database and start the next when switching from uploading one dataset to another.
