def classify_text_query(query):
    query = query.lower()

    if any(word in query for word in ["leaf", "spot", "yellow", "disease"]):
        return "disease"

    if any(word in query for word in ["insect", "worm", "pest", "bug"]):
        return "pest"

    if any(word in query for word in ["water", "irrigation", "dry", "wet"]):
        return "irrigation"

    return "unknown"
