# Testing Guide

## Application
```bash
curl -i http://localhost:8080/health
curl http://localhost:8080/api/server-info
```

## Load Balancing
Open the ALB/custom domain and refresh repeatedly. The Live Infrastructure panel can show different backend instances. ALB routing is not guaranteed to alternate perfectly.

## Failure Recovery
1. Confirm at least two healthy targets.
2. Terminate one ASG-managed instance.
3. Continue accessing the application through the ALB.
4. Inspect Target Group health and ASG Activity.
5. Verify replacement capacity eventually becomes healthy.

## Success Criteria
- Two application instances can run across two AZs.
- EC2 application port is reachable from the ALB SG, not the public internet.
- `/health` returns HTTP 200.
- ASG maintains desired capacity.
- ALB uses healthy registered targets.
- Custom domain resolves to ALB.
- HTTPS works with the ACM certificate.
