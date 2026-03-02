from __future__ import annotations

from datetime import datetime
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field, ConfigDict

# -------------------------
# Tenant / Request context
# -------------------------
class TenantContext(BaseModel):
    model_config = ConfigDict(frozen=True) # Vuelve el modelo inmutable despues de su creación

    tenant_id: str = Field(..., min_length=3, max_length=64)
    workspace_id: Optional[str] = Field(default=None, max_length=64)

class ActorContext(BaseModel):
    model_config = ConfigDict(frozen=True) # Vuelve el modelo inmutable despues de su creación

    user_id: str = Field(..., min_length=3, max_length=128)
    roles: list[str] = Field(default_factory=list)

# -------------------------
# Ingestion
# -------------------------
class DocumentIn(BaseModel):
    doc_id: Optional[str] = None  # si lo provees tú, si no se genera
    source: str = Field(..., max_length=512)  # "s3://...", "upload://...", etc
    title: Optional[str] = Field(default=None, max_length=512)
    doc_type: Literal["pdf", "docx", "html", "txt", "md"] = "txt"
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

class DocumentRef(BaseModel):
    doc_id: str
    version: int = 1
    content_hash: str
    created_at: datetime

class ChunkIn(BaseModel):
    chunk_id: str
    doc_id: str
    chunk_index: int
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    embedding: list[float]

# -------------------------
# Retrieval / Answering
# -------------------------
class RetrievedChunk(BaseModel):
    chunk_id: str
    doc_id: str
    chunk_index: int
    text: str
    score: float
    metadata: dict[str, Any] = Field(default_factory=dict)

class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    source: Optional[str] = None
    chunk_index: Optional[int] = None
    score: Optional[float] = None

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=4000)
    top_k: int = Field(default=8, ge=1, le=50)
    score_threshold: float = Field(default=0.20, ge=0.0, le=1.0)
    tags: list[str] = Field(default_factory=list)
    doc_ids: list[str] = Field(default_factory=list)  # si quieres limitar a ciertos docs
    debug: bool = False

class QueryResponse(BaseModel):
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    abstained: bool = False
    debug: dict[str, Any] = Field(default_factory=dict)