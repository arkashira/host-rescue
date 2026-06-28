# partner‑targets.md – Host‑Rescue Integration Roadmap  

| # | SaaS / API | Free‑Tier Limits (as of 2024‑06) | Integration Effort* | Core User Job Solved (value‑add) | Affiliate / Rev‑Share Potential |
|---|------------|----------------------------------|----------------------|----------------------------------|---------------------------------|
| 1 | **GitHub (Repos + Actions)** | Unlimited public repos; 2 000 CI min/mo for private repos; 500 MB artifact storage | **S** – OAuth + webhook + simple Action template | Detect source code, pull CI pipeline, trigger automated “rescue” migration scripts | GitHub Marketplace revenue‑share (10 % on paid extensions) |
| 2 | **Vercel** | 100 GB bandwidth, 12 serverless functions, 1 team member | **M** – Vercel API + project import wizard + environment variable mapping | Migrate Next.js / static sites with zero‑downtime preview URLs | Vercel Partner Program (up‑to 15 % referral bonus on paid plans) |
| 3 | **Netlify** | 100 GB bandwidth, 300 build minutes, 1 team member | **M** – Netlify API + site import flow + build‑hook integration | Move static JAMstack sites, preserve redirects & Netlify Functions | Netlify Partner tier (15 % revenue share on enterprise upgrades) |
| 4 | **Fly.io** | 3 VMs (1 CPU, 256 MiB RAM each), 160 GB storage, 3 GB outbound traffic | **M** – Flyctl SDK + SSH‑based container upload + DNS automation | Relocate containerised apps (Docker) when original host disappears | Fly.io Referral (5 % of first‑year spend) + future partner‑program revenue split |
| 5 | **DigitalOcean App Platform** | 3 apps, 1 GB RAM, 1 vCPU each, 5 GB storage, 1 TB outbound | **M** – DO API + OAuth + auto‑provision of App resources | Shift Node/Python/Go apps to a managed PaaS with built‑in DB add‑on | DO Affiliate (10 % of referred spend) + co‑marketing credits |
| 6 | **Cloudflare Pages + Workers** | 500 builds/mo, 100 k requests/day for Workers, 1 GB KV storage | **S‑M** – Cloudflare API + DNS‑only zone transfer + Workers KV migration | Export static sites + edge‑function logic; keep DNS continuity | Cloudflare Partner Program (up to 20 % on paid Workers bundles) |
| 7 | **Supabase** | 500 MB database, 200 k auth requests, 2 GB file storage | **S** – Supabase REST + Realtime SDK + auth migration script | Port PostgreSQL DB + Auth + Storage layers; keep app data intact | Supabase Partner (15 % revenue share on paid tier upgrades) |
| 8 | **Terraform Cloud (Free tier)** | 5 users, 30 runs/mo, remote state storage | **L** – Generate Terraform modules for target provider, run plan/apply via Cloud API | Produce IaC that can be re‑run on any supported cloud (future‑proofing) | HashiCorp Partner (tiered rebate on Terraform Cloud usage) |

\* **Effort rating** – *S*: ≤ 2 weeks (single engineer), *M*: 2‑4 weeks (2‑3 engineers, external SDK), *L*: > 4 weeks (cross‑team, complex state handling).

---

## Integration Roadmap (Quarterly Milestones)

| Phase | Timeline | Target Integrations | Primary Outcomes |
|-------|----------|---------------------|------------------|
| **Phase 1 – MVP Core** | Q1 2026 (12 weeks) | GitHub, Vercel, Netlify | • One‑click “Rescue” button inside Host‑Rescue UI.<br>• Automatic repo import, build‑pipeline recreation, and preview URL generation.<br>• Affiliate links displayed on checkout for Vercel/Netlify upgrades. |
| **Phase 2 – Container & Managed‑PaaS** | Q2 2026 (8 weeks) | Fly.io, DigitalOcean App Platform | • Docker image extraction from source host, push to Fly.io/DigitalOcean.<br>• DNS hand‑off automation (CNAME → new endpoint).<br>• Revenue‑share hooks for Fly.io & DO referrals. |
| **Phase 3 – Edge & Data Layer** | Q3 2026 (6 weeks) | Cloudflare Pages + Workers, Supabase | • Migrate static assets + edge functions to Cloudflare.<br>• Export PostgreSQL + auth to Supabase, update env vars.<br>• Joint marketing campaigns (e.g., “Rescue your site to the edge”). |
| **Phase 4 – Future‑Proof IaC** | Q4 2026 (8 weeks) | Terraform Cloud (any provider) | • Auto‑generate Terraform modules for the chosen target host.<br>• Enable customers to re‑apply migrations later or to other clouds.<br>• Unlock HashiCorp partner rebates and position Host‑Rescue as an IaC‑first tool. |

**Prioritisation Logic**

1. **Revenue‑share density** – GitHub, Vercel, Netlify, Fly.io, DO, Cloudflare, Supabase all expose affiliate programs; they are placed early to start cash‑flow.
2. **User‑impact** – 80 % of developers host static or Jamstack sites (GitHub+Vercel/Netlify). Capturing them first maximises adoption.
3. **Technical dependency** – Container migration (Fly.io) builds on GitHub source import, so it follows Phase 1.
4. **Risk mitigation** – Small‑effort integrations (GitHub, Cloudflare) are low‑risk pilots; larger‑effort (Terraform) deferred to Phase 4 after core flows are validated.

---  

### Next Steps for Product & Engineering

1. **Create integration spec docs** for each API (OAuth scopes, webhook payloads, rate limits).  
2. **Set up affiliate accounts** (apply to partner programs, embed tracking IDs).  
3. **Prototype GitHub‑Action “host‑rescue”** to validate end‑to‑end migration flow.  
4. **Allocate sprint capacity**: 2 engineers (S) for Phase 1, add 1‑2 engineers (M) for Phase 2.  

*End of partner‑targets.md*