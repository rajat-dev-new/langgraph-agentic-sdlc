# Request For Proposal (RFP) — Global Corporate Banking Portal

## 1. Executive Context
The client requires a next-generation corporate loan origination and Treasury management portal.

## 2. Mandatory Technical Requirements
- 1. The portal must enforce multi-tenant enterprise SSO via Okta OIDC Authorization Code Flow with PKCE.
- 2. System must persist transactions to high-availability multi-AZ relational databases with automated snapshots.
- 3. Real-time token and session management shall utilize high-speed in-memory caching.
- 4. Container workloads must pass automated vulnerability scans and comply with zero high/critical CVEs.
- 5. Application services must provide RESTful APIs with Pydantic validation contracts.
