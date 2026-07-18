Analyze the access log located at `/app/access.log` and generate a JSON summary report at `/app/report.json`.

Your JSON output must contain exactly these three keys:
1. `total_requests`: The total number of HTTP requests in the log.
2. `unique_ips`: The count of unique client IP addresses.
3. `top_path`: The exact path of the most frequently requested page.
