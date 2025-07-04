import frappe

def get_context(context):
    # static_ids = ["8a707kjkb3", "s7sm2692ue", "sijstsri3b"]
    
    # Fetch matching records from TFrenzy DocType
    docs = frappe.get_all(
        "TFrenzy DocType",
        filters={},
        fields=["name", "image", "spare_name"]
    )

    # Optional: add placeholder image/spare_name if missing
    for doc in docs:
        doc["image"] = doc.get("image") or "https://via.placeholder.com/150"
        doc["spare_name"] = doc.get("spare_name") or f"Spare Part - {doc['name']}"

    context.products = docs
