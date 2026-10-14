# Dev server for pricing-suggestor
$env:LLM_MODE = "mock"
uvicorn backend.main:app --reload --port 8000
