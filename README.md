# E-Commerce Feedback Dataset Generation Project

Welcome to the E-Commerce Feedback Dataset Generation Project! This project is all about creating and managing synthetic customer feedback for an e-commerce platform. Whether you’re looking to add new adjectives, manage comment templates, or generate balanced datasets, you’ve come to the right place.

## What’s Inside

### 1. `adjective_form.pyw`

This is your go-to Tkinter-based application for managing adjectives associated with different ratings.

**What You Can Do**:
- **Add Adjectives**: Easily add new adjectives for ratings. The app will check to make sure you're not adding duplicate records.
- **Remove Adjectives**: Remove adjectives from the list when they’re no longer needed.
- **View Records**: See the list of adjectives and their ratings at a glance.
- **Clear Form**: Reset the form so you can start fresh.

**How to Use**:
1. **Pick a Rating**: Select a rating from 1 to 5.
2. **Enter an Adjective**: Type in your adjective, whether it's a single word or a phrase.
3. **Add It**: Click "Add" to save it for the selected rating.
4. **Remove It**: Choose an adjective from the list and hit "Remove Selected" to delete it.
5. **Start Over**: Click "Clear" to reset everything.

**CSV File**:
- `rating_adjectives.csv`: This file keeps track of all the adjectives and their ratings.

### 2. `template_form.pyw`

This Tkinter-based application helps you manage comment templates used for generating feedback.

**What You Can Do**:
- **Add Comment Templates**: Add new comment templates with ratings, ensuring no duplicates.
- **Remove Comment Templates**: Delete templates you no longer need.
- **Submit Comments**: Check and submit your rating and comment template.
- **Add Placeholders**: Insert a `{adjective}` placeholder into your comment template.
- **Clear Form**: Reset the form for new entries.

**How to Use**:
1. **Pick a Rating**: Choose a rating from 1 to 5.
2. **Enter a Comment Template**: Write your comment template and include a `{adjective}` placeholder if you want.
3. **Add Placeholder**: Click "Add Placeholder" to insert `{adjective}` if it’s not already there.
4. **Submit**: Click "Submit" to save your rating and comment template.
5. **Remove It**: Select a template and click "Remove Selected" to delete it.
6. **Start Fresh**: Click "Clear" to reset everything and remove any placeholders.

**CSV File**:
- `rating_comments.csv`: This file stores all your rating and comment templates.

## Data Generation

Creating your synthetic dataset is straightforward and fun! Here’s the process:

1. **Load Data**:
   - **Adjectives**: Pull in adjectives from `rating_adjectives.csv`.
   - **Comment Templates**: Load your comment templates from `rating_comments.csv`.

2. **Generate Records**:
   - We’ll create exactly 10,000 records with a good mix of positive, negative, and neutral sentiments.
   - For each record, we randomly pick a rating and a comment template. We’ll replace `{adjective}` placeholders with real adjectives.
   - The result will be a diverse set of comments that represent different sentiments.

3. **Output**:
   - All the generated data will be saved in a `data` folder.

## Data Analysis

Once your dataset is ready, here’s how we’ll analyze it:

1. **Load the Dataset**:
   - Get the dataset into a Python environment for analysis.

2. **Analyze Sentiments**:
   - Check if the sentiments are balanced—positive, negative, and neutral.
   - Look out for any biases or imbalances.

3. **Evaluate Comment Templates**:
   - Review the comment templates for diversity and quality.
   - Make sure placeholders are correctly replaced and comments reflect the intended sentiments.

4. **Report**:
   - Create a summary of findings, including sentiment distribution and observations about the comment templates.

## Installation

Before you get started, make sure you have Python installed. You can install all the necessary Python packages with this command:

```bash
pip install numpy pandas textblob matplotlib seaborn jupyter humanize
