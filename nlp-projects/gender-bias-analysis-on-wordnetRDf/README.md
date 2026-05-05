# Gender Bias in Open English WordNet (RDF)
### Quantitative and Qualitative Analysis

## Overview
This project investigates whether gender bias is embedded in the semantic structure of Open English WordNet, using its RDF representation.

The analysis combines quantitative structural metrics with semantic classification techniques to explore how masculine and feminine terms differ in their representation within the lexical network.

---

## Research Question
Do masculine and feminine terms exhibit differences in:
- semantic richness (number of relations)
- hierarchical structure (hypernyms and hyponyms)
- types of associated concepts

---

## Theoretical Background
The project is inspired by:

**McCrae et al. – “Remedying Gender Bias in Open English WordNet”**

This work identifies multiple types of bias:
- structural bias
- contextual bias
- definitional bias
- distributional bias

The key idea is that bias is not only in definitions, but also in how concepts are connected in the network. :contentReference[oaicite:0]{index=0}  

---

## Data

The analysis is based on the **RDF version of WordNet**, structured as a semantic graph.

Main components:
- **Word** → lexical form  
- **WordSense** → specific meaning  
- **Synset** → conceptual unit  

Relations include:
- hypernyms (is-a)
- hyponyms
- other semantic links

This structure allows querying the network systematically and analyzing concept connectivity. :contentReference[oaicite:1]{index=1}  

---

## Methodology

### 1. Quantitative Analysis

- Manual selection of gendered pairs:
  - *king / queen*
  - *actor / actress*
  - *father / mother*
- Each term mapped to a specific synset
- SPARQL queries used to extract:
  - total number of relations
  - hypernyms and hyponyms
- Definition of a **hierarchical connectivity score**

Data processed in Python and analyzed in R.

---

### 2. Semantic Analysis

- Extraction of related terms (from hypernyms and hyponyms)
- Text preprocessing:
  - lowercasing
  - punctuation removal
  - normalization of multi-word expressions
- Use of **GloVe embeddings** for semantic representation
- Definition of semantic categories:
  - authority / power
  - social status
  - family / relation
  - profession / role
  - gender-marked

Each term is assigned to the closest category using cosine similarity, followed by manual validation. :contentReference[oaicite:2]{index=2}  

---

## Results

### Quantitative Findings

- Masculine terms show:
  - higher average number of relations
  - greater variability
  - more central positions in the network

- Feminine terms:
  - lower connectivity on average
  - more limited structural distribution

- Differences are especially visible in **hyponyms**, indicating broader expansion for masculine terms. :contentReference[oaicite:3]{index=3}  

---

### Semantic Findings

After normalization:

- Feminine terms are more associated with:
  - family / relation
  - gender-marked categories

- Masculine terms are more associated with:
  - authority / power
  - profession / role

This suggests different semantic tendencies across genders. :contentReference[oaicite:4]{index=4}  

---

## Limitations

- Uneven number of relations per term (outliers)
- Partial normalization of structural imbalance
- Subjectivity in category definition
- Need for manual validation of embeddings
- Influence of culturally loaded expressions (e.g., *trophy wife*)

Results should be interpreted as **exploratory**, not definitive. :contentReference[oaicite:5]{index=5}  

---

## Conclusions

The analysis suggests that:

- Gender asymmetries exist in WordNet
- They affect both:
  - structure (connectivity)
  - semantic associations
- Masculine terms tend to be more central and widely connected
- Feminine terms are more often linked to relational contexts

These patterns reflect biases embedded in the lexical resource itself, rather than introduced by the analysis.

---

## Tools & Technologies

- Python (SPARQL, RDF processing)
- R (statistical analysis and visualization)
- GloVe embeddings
- WordNet RDF dataset

---

## Repository Structure
