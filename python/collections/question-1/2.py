from collections import defaultdict, Counter

def track_requests(log_entries):
    result = defaultdict(
        lambda: {
            'total_calls': 0,
            'status_counts': Counter()
        }
    )
    for endpoint, status_code in log_entries:
        result[endpoint]['total_calls'] += 1
        result[endpoint]['status_counts'][status_code] = +1
    return result

if __name__ == "__main__":
    log_entries = [
        ("/api/v1/users", 200),
        ("/api/v1/users", 200),
        ("/api/v1/checkout", 500),
        ("/api/v1/users", 404),
        ("/api/v1/checkout", 200),
        ("/api/v1/users", 200)
    ]
    result = track_requests(log_entries)
    print(result)

    normalized = {
        endpoint: {
            **data,
            "status_counts": dict(data["status_counts"])
        }
        for endpoint, data in result.items()
    }
    print(normalized)

