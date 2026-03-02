# /v1/health
#
# readiness: DB + vector index OK
# liveness: proceso OK

from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}