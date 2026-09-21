# Deployment Guide

## Phase 1 — VPC
Create `CloudNova-VPC` (`10.0.0.0/16`) and four subnets across two AZs:
- Public-A: `10.0.1.0/24`
- Public-B: `10.0.2.0/24`
- Private-A: `10.0.11.0/24`
- Private-B: `10.0.12.0/24`

Attach an Internet Gateway. Associate both public subnets with a route table containing `0.0.0.0/0 → Internet Gateway`. Keep the private route table without a direct IGW default route.

## Phase 2 — Security
Create `CloudNova-ALB-SG` allowing HTTP 80 and HTTPS 443 from the internet. Create `CloudNova-App-SG` allowing TCP 8080 **from CloudNova-ALB-SG only**.

## Phase 3 — Golden AMI
Launch a temporary Amazon Linux builder, copy CloudNova to `/opt/cloudnova`, install the supplied systemd unit, and verify:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/api/server-info
sudo systemctl is-enabled cloudnova
```

Reboot and retest. Create `CloudNova-AMI-v1` and wait until it is Available.

## Phase 4 — Target Group + Launch Template + ASG
Create `CloudNova-TG`: Instances, HTTP, port 8080, health path `/health`, success code 200.

Create `CloudNova-LT` from the Golden AMI with `CloudNova-App-SG`. Do not hard-code a subnet.

Create `CloudNova-ASG` across both private subnets. Suggested lab capacity: minimum 2, desired 2, maximum 4. Attach the Target Group.

## Phase 5 — ALB
Create an internet-facing `CloudNova-ALB` in both public subnets. Attach `CloudNova-ALB-SG`. Create an HTTP listener forwarding to `CloudNova-TG`.

## Phase 6 — Route 53 + ACM + HTTPS
Request an ACM public certificate in the **same Region as the ALB** and validate it using DNS. Add an HTTPS 443 listener using the certificate and forward to `CloudNova-TG`. Change HTTP 80 to a 301 redirect to HTTPS. Create a Route 53 Alias A record pointing the chosen hostname to the ALB.

> AWS console wording/defaults can change. Understand the architecture rather than memorizing button positions.
