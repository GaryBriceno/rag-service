# Define puertos para no casarte con un proveedor
# OpenAI vs Anthropic , pgvector vs pinecone.
# Interfaces

from __future__ import annotations

from typing import Protocol, Any, Iterable, Optional

from app.domain.models import (
    TenantContext,
    DocumentIn,
    DocumentRef,
    ChunkIn,
    RetrievedChunk,
    QueryRequest,
    QueryResponse,
)

class DocumentStore(Protocol):
    async def put_raw(self, tenant: TenantContext, doc: DocumentIn, raw_bytes: bytes) -> DocumentRef: ...
    async def get_raw(self, tenant: TenantContext, doc_id: str) -> bytes: ...

class VectorStore(Protocol):
    async def upsert_chunks(self, tenant: TenantContext, chunks: list[ChunkIn]) -> None: ...
    async def similarity_search(
        self,
        tenant: TenantContext,
        query_embedding: list[float],
        top_k: int,
        filters: dict[str, Any] | None = None,
    ) -> list[RetrievedChunk]: ...

class EmbeddingModel(Protocol):
    async def embed_query(self, text: str) -> list[float]: ...
    async def embed_documents(self, texts: list[str]) -> list[list[float]]: ...

class Reranker(Protocol):
    async def rerank(self, query: str, chunks: list[RetrievedChunk], top_k: int) -> list[RetrievedChunk]: ...

class LLMClient(Protocol):
    async def generate(self, *, system: str, user: str, json_schema: dict[str, Any] | None = None) -> dict[str, Any]: ...

class AuthorizationService(Protocol):
    async def assert_can_read_doc(self, tenant: TenantContext, user_id: str, doc_id: str) -> None: ...
    async def filter_doc_ids(self, tenant: TenantContext, user_id: str, doc_ids: list[str]) -> list[str]: ...