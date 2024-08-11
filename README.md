# E-Commerce Feedback Dataset Generation Project

Welcome to the E-Commerce Feedback Dataset Generation Project! This project is focused on generating and managing synthetic customer feedback datasets for an e-commerce platform. The project includes tools for managing adjectives and comment templates and generating balanced datasets to ensure a diversified representation of sentiment.

## Contents

### 1. `adjective_form.pyw`

This is your go-to Tkinter-based application for managing adjectives associated with different ratings.

**Features**:
- **Add Adjectives**: Add new adjectives for ratings. The app will ensure that no duplicate entries are permitted.
- **Remove Adjectives**: Remove adjectives that are no longer needed.
- **View Records**: View the list of adjectives and their associated ratings.
- **Clear Form**: Reset the form to enter a new entry.

**Usage**:
1. **Pick a Rating**: Select a rating from 1 to 5.
2. **Enter an Adjective**: Type in your adjective.
3. **Add It**: Click "Add" to save the adjective for the selected rating.
4. **Remove It**: Choose an adjective from the list and click "Remove Selected" to delete it.
5. **Start Over**: Click "Clear" to reset the form.

**CSV File**:
- `rating_adjectives.csv`: This file stores all the adjectives and their associated ratings.

### 2. `template_form.pyw`

This Tkinter-based application helps you manage comment templates used for generating feedback.

**Features**:
- **Add Comment Templates**: Add new comment templates with ratings. The app checks for duplicates to ensure each template is unique.
- **Remove Comment Templates**: Remove templates that are no longer needed.
- **Submit Comments**: Submit and save your rating and comment template.
- **Add Placeholders**: Insert a `{adjective}` placeholder into your comment template.
- **Clear Form**: Reset the form for new entries.

**Usage**:
1. **Pick a Rating**: Choose a rating from 1 to 5.
2. **Enter a Comment Template**: Write your comment template and include `{adjective}` placeholders if needed.
3. **Add Placeholder**: Click "Add Placeholder" to insert `{adjective}` into your template.
4. **Submit**: Click "Submit" to save your rating and comment template.
5. **Remove It**: Select a template and click "Remove Selected" to delete it.
6. **Start Fresh**: Click "Clear" to reset the form.

**CSV File**:
- `rating_comments.csv`: This file stores all your rating and comment templates.

## Data Generation

The following process, conducted in `Synthetic Data Generator.ipynb`, outlines how the dataset will be generated:

1. **Load Data**:
   - Import adjectives from `rating_adjectives.csv`.
   - Import comment templates from `rating_comments.csv`.

2. **Setup Counters**: Track the number of each rating and sentiment.

3. **Define Targets**:
   - Ratings Target: Set the target as `num_records // 5` to achieve an equal number of each rating (1 through 5).
   - Sentiments Target: Set the target as `num_records // 3` to achieve an equal number of each sentiment (positive, negative, neutral).

4. **Adjust Targets**:
   - Calculate leftover records to ensure exactly `num_records` are generated.
   - Adjust the targets for ratings and sentiments as necessary to account for any discrepancy.

5. **Generate Records**:
   - Prepare 10,000 records with balanced positive, negative, and neutral sentiments.
   - Assign ratings and comment templates randomly, replacing `{adjective}` placeholders with actual adjectives.

6. **Output**:
   - Save the dataset in the `data` folder.

## Data Analysis

Once your dataset is ready, the following steps in `Analysis.ipynb` ensure that it fulfills the project requirements:

1. **Load the Dataset**: Import the dataset into a Python environment.

2. **Analyze Sentiments**:
   - Check if sentiments are relatively balanced across positive, negative, and neutral categories.
   - Identify any biases or imbalances.

3. **Evaluate Comment Templates**:
   - Review the comment templates for diversity and quality.
   - Ensure placeholders are correctly replaced and comments reflect the intended sentiments.

4. **Report**: Summarize findings regarding sentiment distribution and observations about the comment templates.

## Installation

Before you get started, make sure you have Python installed. You can install all the necessary Python packages with the following command:

```bash
pip install numpy pandas textblob matplotlib seaborn jupyter humanize
