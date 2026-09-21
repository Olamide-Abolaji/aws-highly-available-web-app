# Troubleshooting

## No CSS when opened locally
Extract the repository first; do not open `index.html` from inside a ZIP. Prefer `python3 server.py` and visit `http://localhost:8080`.

## Target unhealthy
```bash
sudo systemctl status cloudnova
sudo journalctl -u cloudnova --no-pager -n 100
curl -i http://localhost:8080/health
ss -lntp
```
Confirm Target Group uses HTTP:8080 and `CloudNova-App-SG` allows 8080 from `CloudNova-ALB-SG`.

## `local-demo` appears
Expected outside EC2. On EC2, verify IMDSv2 access is enabled.

## ALB unreachable
Verify it is internet-facing, uses both public subnets, those subnets route `0.0.0.0/0` to the IGW, and the ALB SG permits the listener port.

## Private instance cannot download packages
That is expected without an outbound design. Use a deliberate approach such as NAT, suitable VPC endpoints, or a prebuilt image rather than making production instances public.
