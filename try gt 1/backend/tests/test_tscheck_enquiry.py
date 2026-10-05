import re


def test_create_enquiry_returns_reference_and_echoes_payload(client):
    payload = {
        "full_name": "tscheck-enquiry-test",
        "company": "tscheck-enquiry-co",
        "email": "tscheck-enquiry@example.com",
        "phone": "+1 555 010 2400",
        "service_required": "Cloud Engineering",
        "message": "tscheck enquiry happy path with enough detail.",
    }
    response = client.post("/enquiries", json=payload)
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["full_name"] == payload["full_name"]
    assert body["company"] == payload["company"]
    assert re.fullmatch(r"ZZZOR-[A-F0-9]{4}", body["reference_number"])
    assert body["id"]


def test_create_enquiry_rejects_short_message(client):
    payload = {
        "full_name": "tscheck-invalid",
        "company": "tscheck-invalid-co",
        "email": "tscheck-invalid@example.com",
        "phone": "+1 555 010 2401",
        "service_required": "AI",
        "message": "too short",
    }
    response = client.post("/enquiries", json=payload)
    assert response.status_code == 422, response.text
