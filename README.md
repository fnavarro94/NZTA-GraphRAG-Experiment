# NZTA-GraphRAG-Experiment

**Code to run the experiment that evaluate the RAG at node retrieval level and answer level. This code contains the data to load the Neo4j data bases and the code required for the evaluation.**


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

### Install Dependencies

First, install the required dependencies:

```{bash}
pip install -r requirements.txt
```

## Filling the Neo4j Databases

Before proceeding, ensure that you have Neo4j installed and a database set up and running. For detailed setup instructions, please refer to the [Neo4j Setup Guide](https://github.com/fnavarro94/NZTA-GraphRAG/tree/main).

### Loading Data into Neo4j

This project requires **two separate Neo4j databases**: one for the **OIA** data and another for the **SP-CoT** data. You should load the data into each database **one at a time** using the provided Jupyter notebooks:

- To upload the **OIA data**, run the notebook:

  |||
  kg_loader_oia.ipynb
  |||

- To upload the **SP-CoT data**, run the notebook:

  |||
  kg_loader_sp_cot.ipynb
  |||

Make sure your Neo4j instance is running and your `.env` file is correctly configured before executing these notebooks.





