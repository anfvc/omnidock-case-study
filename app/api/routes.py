from fastapi import APIRouter, HTTPException
from app.models.schemas import ProductInput
from app.core.classifier import classify_with_openai

router = APIRouter()

@router.post("/classify")
def classify_produc(product: ProductInput):
  #Classifies an amazon product into an OTTO category:

  matched_category = classify_with_openai(product.title, product.description)

  if not matched_category or matched_category == "Unkown Category":
    raise HTTPException(status_code=404, detail="No matching category found.")

  return {"matched_category": matched_category}



