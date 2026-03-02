
from pydantic import BaseModel, ConfigDict, Field

# -------------------------
# Tenant / Request context
# -------------------------
class TenantContext(BaseModel):

    model_config = ConfigDict(frozen=True) # Vuelve el modelo inmutable despues de su creación
    tenant_id: str = Field(..., min_length=3, max_length=64)
    workspace_id: str = Field(default=None, max_length=64)

class ActorContext(BaseModel):

    model_config = ConfigDict(frozen=True) # Vuelve el modelo inmutable despues de su creación
    user_id: str = Field(..., min_length=3, max_length=128)
    roles: list[str] = Field(default_factory=list)

