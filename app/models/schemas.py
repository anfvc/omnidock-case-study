from pydantic import BaseModel
from typing import Optional

class ProductInput(BaseModel):
  title: str
  description: str
  features: Optional[str] = None
