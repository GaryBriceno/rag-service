# /v1/health
#
# readiness: DB + vector index OK
# liveness: proceso OK

from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@router.get("/live")
def live():
    """Liveness check endpoint."""
    return {"status": "live"}