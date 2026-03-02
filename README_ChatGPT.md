6) Reglas multi-tenant que debes aplicar SIEMPRE

Esto es “no negociable” en enterprise:
- Tenant isolation por diseño
  - Todas las tablas llevan tenant_id
  - Toda búsqueda vectorial filtra por tenant_id
- AuthZ antes de retrieval
  - Si user no puede ver un doc, nunca debe entrar al contexto.
- Metadata filtering
  - tags/workspace/roles como filtros
- No mezcles caches entre tenants
  - keys incluyen tenant_id


To run the app:
> uvicorn app.main:app --reload 

To view the API docs:
> http://127.0.0.1:8000/docs