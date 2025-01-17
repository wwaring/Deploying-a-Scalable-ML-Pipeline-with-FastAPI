# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is an academic attempt at deploying a scalable Machine Learning pipeline with fastAPI.

## Intended Use

Based on the census data provided, this model attempts to predict the annual income of an individual.
The intended task is to predict whether a person makes over or under 50K a year.
 
## Training Data

The training data used is from the 1994 Census and the extraction was done by Barry Becker.
The dataset is multivariate with 48,842 instances and 14 features.
Additional details about the data used can be found here: https://archive.ics.uci.edu/dataset/20/census+income
 
## Evaluation Data

The data was split for training and testing where 80% of the data was dedicated for training and 20% for testing. 

## Metrics

The key performance metrics include: Precision: 0.7471 | Recall: 0.6091 | F1: 0.6711
- Precision which measures how accurate the positive predictions are. In this case, out of all people the model predicted as earning over 50K, a ratio of 0.7471 actually do.
- Recall focuses on avoiding missing true positives so in this case, out of all the people who truly earn over 50K, the model identifies a ratio of 0.6091. 
- The F1 score attempts to find the balance between precision and recall by finding the harmonic mean. This approach gives more weight to smaller values, reflecting the overall performance and here this value was 0.6711

## Ethical Considerations

A misconception that the model might be used to infer is that "education _causes_ higher income.
The data and the results reflect correlation but not causation.

## Caveats and Recommendation

The United States census is carried out after every decade and this type of data can be considered outdated over time and this can impact the relevance of the model itself.
A recommendation is to include additional data sources that will have more frequent updates so as to keep the model relevant.
