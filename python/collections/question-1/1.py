def track_requests(log_entries):
    result = {}
    for endpoint, status_code in log_entries:
        if endpoint not in result:
            result[endpoint] = {
                'total_calls': 0,
                'status_counts': {}
            }
        result[endpoint]['total_calls'] += 1
        if status_code not in result[endpoint]['status_counts']:
            result[endpoint]['status_counts'][status_code] = 0
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
