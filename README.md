# OmniDock E-commerce Product Classification Case Study

## Overview
In this case study, you will build a system that helps e-commerce businesses automatically classify products from one marketplace (e.g., Amazon) into corresponding categories on other marketplaces. This classification is crucial for determining commission rates and optimizing product listings across different platforms.

## Background
OmniDock OS, a e-commerce integration platform, needs to help sellers list their products across multiple marketplaces efficiently. One key challenge is mapping product categories between different platforms, as each marketplace has its own category structure and associated commission rates.

## Task Description
Create a FastAPI-based classification service that:
1. Accepts product data (e.g., title, features, description) from Amazon
2. Uses LLM-based classification to map it to equivalent categories on target marketplaces
3. Returns the predicted category along with confidence scores (if possible)

### Time Allocation: 1-1.5 hours

## Technical Requirements

### Core Requirements
- Implement a FastAPI server with necessary endpoints
- Integrate with an LLM for classification
- Create a basic classification prompt/system that maps categories
- Implement error handling and input validation
- Add basic logging for monitoring

## Sample Data
See `product_data.json` for sample product data along side the target categories for OTTO.de. 
See all categories for OTTO.de in `categories_otto.json`

## Important Notes
- This is an open-ended task - feel free to be creative in your implementation
    - Do you have enough data? Would you rather match different attributes?
- There are many ways to solve this problem - we're interested in seeing your approach
- Consider how you would handle:
  - Env Setup
  - API key management and security
  - Prompt engineering for accurate classification
  - Error cases and edge scenarios
- Document any assumptions you make and why you made certain technical choices
- Focus on creating a working solution that demonstrates your thinking process
- Think about marketplace evolution: Categories aren't static - how would your system adapt to new categories or handle deprecated ones?
- How can this approach be easily transferred to other marketplaces?
