from scourgify import normalize_address_record


def normalize_address(addr: str):
    # Copied from database/engels/address.py
    try:
        record = normalize_address_record(addr)
    except Exception:
        return None

    components = [
        record["address_line_1"],
        record["address_line_2"],
        record["postal_code"],
    ]

    return " ".join([piece for piece in components if piece])
