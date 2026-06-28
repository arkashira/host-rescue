```markdown
# Breakeven Analysis: Host-Rescue

## Cost per Active User (CAU)

| Resource     | Cost per User (USD) |
|--------------|---------------------|
| Compute      | $0.15               |
| Storage      | $0.05               |
| Bandwidth    | $0.02               |
| **Total CAU**| **$0.22**           |

*Assumptions:*
- Compute: $0.05/hour × 30 days × 24 hours ÷ 100 users = $0.15/user
- Storage: $0.01/GB × 5GB ÷ 100 users = $0.05/user
- Bandwidth: $0.01/GB × 2GB ÷ 100 users = $0.02/user

## Pricing Tiers

| Tier        | Price/Month | Features                                                                 |
|-------------|-------------|--------------------------------------------------------------------------|
| Starter     | $9.99       | 10GB storage, 100GB bandwidth, basic support, 1 project                   |
| Professional| $29.99      | 50GB storage, 500GB bandwidth, priority support, 5 projects                |
| Enterprise  | $99.99      | 200GB storage, unlimited bandwidth, 24/7 support, 20 projects, custom domains|

## CAC Range
- **Low End**: $250
- **High End**: $1,200
- **Average**: $650

## LTV Estimate
- **Starter**: $9.99 × 12 months = $119.88
- **Professional**: $29.99 × 12 months = $359.88
- **Enterprise**: $99.99 × 12 months = $1,199.88

## Break-even Users Count
- **Per Tier**:
  - Starter: 1,198 users
  - Professional: 400 users
  - Enterprise: 120 users

- **Overall Break-even**: 1,600 users (assuming 60% Starter, 30% Professional, 10% Enterprise mix)

## Path to $10K MRR

| Tier         | Users | Monthly Revenue |
|--------------|-------|-----------------|
| Professional | 334   | $9,997          |
| Starter      | 1,000 | $10,000         |
| Enterprise   | 101   | $10,099         |

**Recommended Path**: 
- Start with Professional tier (334 users) to reach $10K MRR quickly
- Scale to Starter tier (1,000 users) for maximum revenue potential
- Maintain 10% Enterprise tier for premium revenue stream
```
