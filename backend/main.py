from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SentinelConfig API")

# This is a 'Schema' - it defines what data we expect from the user
class FeatureFlag(BaseModel):
    name: str
    is_enabled: bool
    description: str | None = None

# Mock Database for now (we will move this to Postgres in Week 2)
mock_db = {
    "beta_ui": {"is_enabled": True, "description": "Enables the new React frontend"},
    "maintenance_mode": {"is_enabled": False, "description": "Shuts down traffic for maintenance"}
}

@app.get("/")
def read_root():
    return {"status": "SentinelConfig API is live"}

@app.get("/flags/{flag_name}")
def get_flag(flag_name: str):
    """Fetch the status of a specific feature flag"""
    flag = mock_db.get(flag_name)
    if flag:
        return {"name": flag_name, "enabled": flag["is_enabled"]}
    return {"error": "Flag not found"}, 404

@app.post("/flags/toggle")
def toggle_flag(flag: FeatureFlag):
    """Toggle a flag (This will eventually save to Postgres)"""
    mock_db[flag.name] = {"is_enabled": flag.is_enabled, "description": flag.description}
    return {"message": f"Flag '{flag.name}' updated successfully"}
