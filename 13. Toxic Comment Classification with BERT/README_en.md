# Project: Toxic Comment Classification with BERT

The online store is launching a new service: users can edit and supplement product descriptions like in wiki communities. To maintain a positive atmosphere, an automatic toxic comment detection tool is required.

## Project Goal

Build a model that classifies user comments as **toxic (1)** or **non-toxic (0)** to enable timely content moderation.

**Target metric:** F1 ≥ 0.75

## Project Stages

1. **Data preprocessing**
   - Import libraries
   - Load data
   - Check for missing values, duplicates, class imbalance

2. **Text cleaning**
   - Lowercasing
   - Removing HTML tags, links, punctuation, and stopwords

3. **Baseline models**
   - Text vectorization with TF-IDF
   - Models: Logistic Regression, Linear SVC
   - Hyperparameter tuning via GridSearchCV
   - Evaluation using F1-score

4. **BERT fine-tuning**
   - Model: `bert-base-multilingual-cased`
   - Custom Dataset and DataLoader
   - Training and validation
   - F1-score evaluation

5. **Model comparison**
   - Compare F1 scores, training and inference time
   - Justify final model selection

6. **Conclusion**
   - Summary and deployment recommendations