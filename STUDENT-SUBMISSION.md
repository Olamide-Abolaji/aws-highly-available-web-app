# 🎓 CloudNova Student Submission

## Required Evidence
Provide screenshots of:
- VPC and four subnets
- Route-table associations
- ALB and application security groups
- Launch Template
- Auto Scaling Group configuration
- EC2 instances across the intended AZs
- Target Group showing healthy targets
- Application Load Balancer
- Running CloudNova website
- Live Infrastructure panel
- Route 53 record
- ACM certificate showing `Issued`
- HTTPS website
- ASG Activity after a simulated instance failure

Remove or obscure sensitive/account-specific information before publishing screenshots.

## Reflection Questions
1. What makes a subnet public?
2. Why are application EC2 instances private?
3. Why does the App SG reference the ALB SG?
4. Target Group vs Auto Scaling Group: what is the difference?
5. What happens when an ASG-managed instance is terminated?
6. Why use multiple Availability Zones?
7. Why create a Golden AMI?
8. Where does TLS terminate?
9. Why should the Launch Template not hard-code one subnet?
10. Explain the complete request path from browser to CloudNova.

## GitHub Deliverables
Your repository should contain the source code, architecture diagram, README, deployment notes, sanitized screenshots and a short **What I Learned** section.
