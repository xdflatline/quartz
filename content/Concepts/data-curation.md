---
title: Data Curation
detail: Data curation is the process of selecting, organizing, and maintaining datasets used for training and evaluating machine learning models. Poor data...
details: Data curation is the process of selecting, organizing, and maintaining datasets used for training and evaluating machine learning models. Poor data...
tags:
  - concepts
created: 2026-05-19
updated: 2026-05-19
type: concept
sources:
  - Raw/see-log.md
---
## Overview

Data curation is the process of selecting, organizing, and maintaining datasets used for training and evaluating machine learning models. Poor data quality leads to unreliable models and potentially harmful outcomes.

## Quality Concerns

### Clinical Dataset Issues (2026-05)
- Kaggle-hosted datasets for clinical models (stroke, diabetes) found to be "comically bad"
- Issues include: data leakage, label errors, unrealistic distributions
- Models trained on these datasets produce misleading clinical predictions
- Highlights the gap between benchmark performance and real-world applicability

### Common Data Quality Problems
1. **Data leakage**: Test data inadvertently included in training
2. **Label noise**: Incorrect or inconsistent annotations
3. **Distribution shift**: Training data not representative of deployment scenarios
4. **Missing metadata**: Lack of provenance, collection methodology documentation

## Best Practices

- Version datasets with clear provenance tracking
- Implement automated data quality checks
- Use data cards/datasheets for documentation
- Separate benchmark data from training data rigorously
- Cross-validate across multiple data sources

## Related

- [[Concepts/llm-architecture|llm-architecture]]
- [[Concepts/ai-agents|ai-agents]]
- [[Concepts/ai-content-provenance|AI Content Provenance]] — questions about training data provenance raised by shadow library takedowns
