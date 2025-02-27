import pandas as pd
import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# calling env from .env
load_dotenv()

api_key = os.getenv("OPENAI_KEY")

# print(api_key)

if not api_key:
  raise ValueError("API KEY is missing, please check!")

client = OpenAI(api_key=api_key) # loading key from .env

# Loading the otto categories from CSV:
categories_otto = pd.read_csv("data/categories_otto.csv")
otto_categories = categories_otto["Category"].dropna().astype(str).tolist() # Converting to strings and ensuring no NaN are part of the filter

def classify_with_openai(title: str, description: str) -> str: #return type of the function must be a string
  """
   Uses OPEANI GPT to classify a product based on its title and description
     """

  title = str(title) if pd.notna(title) else ""
  description = str(description) if pd.notna(description) else ""


  # I'm exceeding the max length content, I need to filter:

  relevant_categories = [
    category for category in otto_categories
    if any (word.lower() in category.lower() for word in title.split() + description.split())
  ]

  relevant_categories = relevant_categories[:5] if len(relevant_categories) > 5 else relevant_categories

  prompt = f"""
    You are an AI trained for product classification.

    Match the following product to the MOST ACCURATE category from the given list.
    **Only return one category** from the list—do not make up categories.

    ### Categories:
    {', '.join(relevant_categories)}

    ### Product Details:
    - **Title**: {title}
    - **Description**: {description}

    **Instructions:**
    - Do NOT return unrelated or broad categories.
    - If the product is a smartphone, return **Smartphones**, not **Smartphone-Akku** or accessories.
    - Respond with ONLY the category name.
    """

  print(prompt)

  response = client.chat.completions.create(
      model="gpt-4",
      messages=[{"role": "system", "content": prompt}],
      max_tokens=20
    )

  return response.choices[0].message.content.strip()

