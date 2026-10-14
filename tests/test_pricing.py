import pytest
@pytest.mark.asyncio
async def test_quote(client):
    r = await client.post("/api/quotes", json={"package": "Pro", "features": "SSO\nAudit", "anchor": 100})
    assert r.status_code == 200
    assert r.json()["suggested"] > 0
