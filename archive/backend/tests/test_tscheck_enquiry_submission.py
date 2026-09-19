"""API coverage for the enquiry submission criterion (POST /api/enquiries)."""

import uuid


def test_enquiry_submission_creates_reference(client):
    unique = uuid.uuid4().hex[:8]
    payload = {
        "full_name": f"tscheck-enquiry-{unique}",
        "company": "Ganesh Tech Expanded QA",
        "email": f"tscheck.{unique}@example.com",
        "phone": "+91 8111111111",
        "service_required": "Managed IT Services",
        "message": f"tscheck-{unique} would like to discuss managed IT services coverage.",
    }
    response = client.post("/enquiries", json=payload)
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["full_name"] == payload["full_name"]
    assert body["service_required"] == "Managed IT Services"
    assert body["reference_number"].startswith("ZZZOR-")
    assert len(body["reference_number"]) == len("ZZZOR-") + 4

    # created row must actually be retrievable, not just echoed back
    listing = client.get("/enquiries")
    assert listing.status_code == 200
    ids = [row["id"] for row in listing.json()]
    assert body["id"] in ids


def test_enquiry_submission_rejects_short_message(client):
    unique = uuid.uuid4().hex[:8]
    payload = {
        "full_name": f"tscheck-enquiry-bad-{unique}",
        "company": "Ganesh Tech Expanded QA",
        "email": f"tscheck.bad.{unique}@example.com",
        "phone": "+91 8111111112",
        "service_required": "Data & Analytics",
        "message": "short",
    }
    response = client.post("/enquiries", json=payload)
    assert response.status_code == 422, response.text
