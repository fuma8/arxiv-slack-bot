# arxiv-slack-bot
[Updated] 2024-10-31: You can collect papers you are interested in using [jina-embeddings-v3](https://huggingface.co/jinaai/jina-embeddings-v3).


## Installation
### 0. Install Poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```
### 1. Clone this repository
```
git clone git@github.com:fuma8/arxiv-slack-bot.git
cd arxiv-slack-bot
```
### 2. Install dependencies with poetry
```
poetry install
```

## Quick start
### 1. Specify the parameter.

You need to specify two parameters as bellow.
- Prompt: The target area can be specified by text in line 13 of main.py. Please note that you can specify it with **English only**.
- max papers: This is the number of papers that jina-embeddings-v3 will extract from arxiv for the papers you are interested in. The default is 10.
### 2. Run the script

You can run this function with following command.
```
poetry run python src/main.py
```
If you can run correctly, the following results would appear in your terminal (This is an example when the prompt is "Diffusion model" and the max papers is 10).
```Top relevant papers:
Title: Blurring Diffusion Models
Link: http://arxiv.org/abs/2209.05557v3
Similarity: 0.5487

Title: Diffusion on dynamic contact networks with indirect transmission links
Link: http://arxiv.org/abs/1906.02856v1
Similarity: 0.5443

Title: Where to Diffuse, How to Diffuse, and How to Get Back: Automated
  Learning for Multivariate Diffusions
Link: http://arxiv.org/abs/2302.07261v2
Similarity: 0.5372

Title: An Overview of Diffusion Models: Applications, Guided Generation,
  Statistical Rates and Optimization
Link: http://arxiv.org/abs/2404.07771v1
Similarity: 0.5323

Title: Diffusion Models are Evolutionary Algorithms
Link: http://arxiv.org/abs/2410.02543v2
Similarity: 0.5157

Title: Well-posedness of a cross-diffusion population model with nonlocal
  diffusion
Link: http://arxiv.org/abs/1905.04004v2
Similarity: 0.4938

Title: On diffusion approximation with discontinuous coefficients
Link: http://arxiv.org/abs/math/0204289v1
Similarity: 0.4907

Title: Diffusion Models for Non-autoregressive Text Generation: A Survey
Link: http://arxiv.org/abs/2303.06574v2
Similarity: 0.4396

Title: Diffuse or Confuse: A Diffusion Deepfake Speech Dataset
Link: http://arxiv.org/abs/2410.06796v1
Similarity: 0.4009

Title: Analyzing PFG anisotropic anomalous diffusions by instantaneous signal
  attenuation method
Link: http://arxiv.org/abs/1701.00257v2
Similarity: 0.3732
```