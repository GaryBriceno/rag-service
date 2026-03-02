# app/rag/retrieve/llm_schemas.py

from pydantic import BaseModel, Field
from typing import List

class LLMOutput(BaseModel):
    answer: str
    citations: List[str]
    confidence: float = Field(ge=0.0, le=1.0)
    abstain: bool

LLM_OUTPUT_SCHEMA = LLMOutput.model_json_schema()