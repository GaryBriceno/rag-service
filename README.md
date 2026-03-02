rag-service/
  pyproject.toml
  README.md
  .env.example
  docker/
    Dockerfile
    docker-compose.yml
  migrations/                # Alembic
  app/
    __init__.py
    main.py                  # FastAPI app factory
    config.py                # settings (pydantic-settings)
    deps.py                  # DI: db, vectorstore, llm, auth, tenant
    api/
      v1/
        routes_health.py
        routes_ingest.py
        routes_query.py
    domain/
      models.py              # entidades (Document, Chunk, QueryResult)
      ports.py               # interfaces: VectorStore, DocStore, Reranker, LLM, AuthZ
    rag/
      ingest/
        loaders.py           # pdf/docx/html/txt
        normalize.py
        chunking.py
        pipeline.py
      retrieve/
        retriever.py
        rerank.py
        prompt.py
        answer.py
      eval/
        datasets.py
        metrics.py
        runner.py
    infra/
      db/
        session.py           # SQLAlchemy session
        models.py            # tablas: documents, chunks
        repo.py              # repos (DocumentRepo)
      vector/
        pgvector_store.py    # implementación VectorStore
      llm/
        openai_client.py
        anthropic_client.py
      queue/
        worker.py            # RQ/Celery/Arq
    observability/
      logging.py
      tracing.py
      metrics.py
    security/
      authn.py               # authn (token/JWT)
      authz.py               # policies (tenant ACL)
      pii.py
      injection.py
    utils/
      ids.py
      time.py
      hashing.py
  tests/
    unit/
    integration/


De esta forma separamos dominio/puertos (contratos estables) de infra(implementaciones), y el RAG queda modular.

rag-service/
  pyproject.toml
  README.md
  .env.example
  docker/
    Dockerfile
    docker-compose.yml
  migrations/                # Alembic
  app/
    __init__.py
    main.py                  # FastAPI app factory
    config.py                # settings (pydantic-settings)
    deps.py                  # DI: db, vectorstore, llm, auth, tenant
    api/
      v1/
        routes_health.py
        routes_ingest.py
        routes_query.py
    domain/
      models.py              # entidades (Document, Chunk, QueryResult)
      ports.py               # interfaces: VectorStore, DocStore, Reranker, LLM, AuthZ
    rag/
      ingest/
        loaders.py           # pdf/docx/html/txt
        normalize.py
        chunking.py
        pipeline.py
      retrieve/
        retriever.py
        rerank.py
        prompt.py
        answer.py
      eval/
        datasets.py
        metrics.py
        runner.py
    infra/
      db/
        session.py           # SQLAlchemy session
        models.py            # tablas: documents, chunks
        repo.py              # repos (DocumentRepo)
      vector/
        pgvector_store.py    # implementación VectorStore
      llm/
        openai_client.py
        anthropic_client.py
      queue/
        worker.py            # RQ/Celery/Arq
    observability/
      logging.py
      tracing.py
      metrics.py
    security/
      authn.py               # authn (token/JWT)
      authz.py               # policies (tenant ACL)
      pii.py
      injection.py
    utils/
      ids.py
      time.py
      hashing.py
  tests/
    unit/
    integration/


