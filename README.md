# Parameter-Efficient Fine-Tuning of a Language Model for Detecting Threats of Physical Violence in Text

The aim of this work is to explore how Natural Language Processing (NLP) models based on modern methods such as transformers and attention mechanisms - can help identify "violent speech". Specifically, it combines parameter-efficient fine-tuning techniques such as LoRA (Low-Rank Adaptation of Large Language Models) and QLoRA (Quantized Low-Rank Adaptation).

The model is designed to detect:

- Threats of physical violence
- Threats of murder
- Physical violence persuasions
- Suicide persuasions
- Self-harm persuasions

Exceptions that the model should classify as "normal speech":

- Suicide threats – these are interpreted more as a cry for help than as genuine threats of violence; this category also includes please for help regarding suicide, etc.
- Self-harm threats

More challenging examples for classification include cases related to:

- **Gaming context:** This was added to increase the difficulty of the task, requiring the model to recognize that threats are directed at players in a game.
- Other specific contexts such as religious, legal, etc.

## Project Structure

**Text-Classification-Death-Threats/**<br>
├── [**DatasetManagment/**](./DatasetManagment/) # datasets and scripts for loading and augmentation<br>
│ ├── [DatasetResources/](./DatasetManagment/DatasetResources) # datasets<br>
│ ├── [dataset_loader.py](./DatasetManagment/dataset_loader.py) # loading datasets<br>
│ ├── [keyboard_neighborhood.py](./DatasetManagment/keyboard_neighborhood.py) # simulating typos<br>
│ ├── [**augmentation.py**](./DatasetManagment/augmentation.py) # augmentation class<br>
│ └── [dataset_const.py](./DatasetManagment/dataset_const.py) # constants <br>
├── [Tests/](./Tests/) # Tests<br>
│ └── [test_api_key.py](./Tests/test_api_key.py) - # Testing OpenAI API requests<br>
├── [BertAnalysis.ipynb](./BertAnalysis.ipynb) # Comparing Vocabularies of different Bert models<br>
├── [CreatingDatasetsExample.ipynb](./CreatingDatasetsExample.ipynb) # Augmentation notebook <br>
├── [**FineTunningBertic.ipynb**](./FineTunningBertic.ipynb) # main notebook, fine-tuning of BERT model <br>
├── [BiasCheck.ipynb](./BiasCheck.ipynb) # Hate speech analysis notebook <br>
├── PresentationResources/ # Project presentation materials<br>
├── [.gitignore](./.gitignore) # Git exclusions<br>
├── [requirements.txt](./requirements.txt) # Project dependencies<br>
├── [.env.example](./.env) # example of .env file<br>
├── [GraduationThesis.pdf](./GraduationThesis.pdf) # Graduation Thesis (Serbian)<br>
└── README.md # Project documentation<br>

## Model Selection and Tokenization

- By comparing the tokenizers of various models, I chose Bertic (checkpoint_name = "classla/bcms-bertic").

🐍[ComparingVocabularies notebook](BertAnalysis.ipynb)

## Overview

### Creating the Dataset

- Manually crated data
- paraphrasing using the GPT-4 model via the OPEN API for different response temperature values
- noise injection by adding common typographical errors.

🐍[Creating the Dataset notebook](CreatingDatasetsExample.ipynb)

### **Fine-Tuning**

To save computational resources, quantization and LoRA matrices were used for fine-tuning. The positions where the LoRA matrices are added, as well as their rank, were carefully adjusted to achieve additional resource savings with minimal performance loss:

🐍[Fine-Tuning notebook](FineTunningBertic.ipynb)

- Investigating quantization as a regularization method
- Explored optimal configurations by experimenting with the balance between LoRA rank
  and LoRA scaling factor, and determined the best transformer layers and positions for integrating LoRA matrices.
- Explored the balance between resource utilization and
  performance by varying the size and number of LoRA matrices

### Hate speech analysis

Exploring Political Bias related to Hate Speech Detection Models

🐍[Hate Speech Analysis noteboook](BiasCheck.ipynb)

<br><br><br>

### **Thank you for exploring my project!**

If you'd like to learn more about my background and qualifications, please visit my [LinkedIn profile](https://www.linkedin.com/in/jankomitrovic)
