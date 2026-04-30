# Mapping Italian Expressions for “Now”
### An HGIS Project on Linguistic Variation and Identity

## Overview
This project explores the geographical distribution of three Italian temporal adverbs meaning *“now”*: **mo**, **ora**, and **adesso**.

The aim is to investigate whether these forms represent simple lexical variation or reflect deeper cultural and identity boundaries across Italy.

This is an exploratory project: it does not aim to provide a definitive answer, but to highlight spatial patterns and support interpretative hypotheses.

---

## Research Question
Do the Italian temporal adverbs *mo*, *ora*, and *adesso* — all meaning “now” and deriving from different Latin forms (*modo*, *hora*, *ad ipsum*) — simply mark lexical variation, or do they reflect deeper cultural and identity boundaries?

---

## Data Sources
The primary dataset is based on the **Atlante Italo-Svizzero (AIS)**, one of the most important linguistic atlases documenting dialect variation in Italy and Southern Switzerland.

Key characteristics of the data:
- Collected between **1919 and 1935**
- Based on **fieldwork and structured interviews**
- Informants were typically **older local speakers**
- Strong focus on **dialect preservation**
- Data originally transcribed in **phonetic notation**

The final dataset includes:
- **369 georeferenced points**
- Dialect form (`d_form`)
- Lexical family (`l_family`)

---

## Methodology

### Data Processing
- Manual **georeferencing** of AIS maps in QGIS
- Creation of a **point layer** representing all locations
- Classification of dialect forms into lexical families:
  - **MO**
  - **ORA**
  - **ADESSO**
  - **OTHER** (unclear or ambiguous forms)

The classification is based on **etymology and morphological similarity**.

---

### Mapping Techniques

Two complementary maps were created:

#### 1. Point Map
- Direct representation of the data
- More **accurate and transparent**
- Includes missing or uncertain data

#### 2. Voronoi Map
- Generates continuous spatial areas based on point distribution
- More **intuitive visualization of patterns**
- Clipped using an Italy shapefile (Natural Earth)
- **Dashed boundaries** used to indicate that areas are approximate, not absolute linguistic borders

---

## Results

The maps reveal clear spatial patterns:

- **Northern Italy → “adesso”**
- **Central Italy → “ora”**
- **Southern Italy → “mo”**

Key observations:
- The distribution is **not random**
- “mo” is **widely used and deeply rooted** in Southern Italy
- “adesso” forms a **compact macro-area** in the North
- “ora” appears as an **intermediate form**, both geographically and linguistically

These patterns align, to some extent, with:
- Traditional **dialect regions**
- Historical divisions of Italy (pre-unification)

---

## Interpretation

The findings suggest that variation is not purely lexical.

Instead, it appears to be connected to:
- Broader **linguistic systems**
- **Historical and cultural contexts**
- Possible **regional identity patterns**

However, these interpretations remain exploratory.

---

## Limitations

This project has several limitations:

- Simplification of dialect variation into broad categories
- Partial etymological verification
- Approximate spatial accuracy (manual georeferencing)
- Voronoi polygons based on mathematical proximity, not real linguistic boundaries

More importantly:
- GIS can show **where patterns occur**
- But it cannot explain **why they exist**

---

## Ethical Considerations

- Risk of reinforcing **linguistic stereotypes**
- Non-standard forms should not be perceived as less valid
- Maps are **not neutral representations**
- Every step (data selection, classification, visualization) involves subjective decisions

---

## Tools
- QGIS
- Natural Earth 
- Manual data extraction (AIS)

---

## Repository Structure
