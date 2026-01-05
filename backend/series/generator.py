def generate_series(payload):
    return {
        "status": "success",
        "series": [
            f"Short video idea #{i+1} about {payload.get('topic','AI')}"
            for i in range(payload.get("count", 5))
        ]
    }
