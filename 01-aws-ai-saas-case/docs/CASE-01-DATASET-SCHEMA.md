# Case 01: ClarionFlow AI
## Learner Dataset Schema

This document describes the structure of the synthetic dataset for Case 01.

The dataset is inspired by AWS cost and usage reporting concepts. AWS Cost and Usage Reports provide highly detailed cost and usage line items across services, accounts, time periods, and dimensions, which makes them a useful conceptual model for building a realistic FinOps case dataset.

The purpose of this schema is to support practical analysis of cloud cost behavior, allocation, trends, and operating decisions.

## Primary dataset

Main file:
- `data/billing.csv`

Optional supporting dimension files may be added later if needed.

## Column definitions

### Time and account fields

- `usage_date` — Date of usage at daily granularity
- `account_id` — AWS account identifier
- `account_name` — Human-readable account label
- `region` — AWS region

### Cost and service fields

- `service` — AWS service name
- `service_category` — Higher-level grouping such as compute, storage, database, network, observability, or AI
- `usage_type` — Usage type classification
- `operation` — Operation or API-related label where relevant
- `resource_id` — Resource identifier where available
- `usage_quantity` — Usage amount
- `usage_unit` — Unit of measure
- `blended_cost` — Blended cost in USD
- `unblended_cost` — Unblended cost in USD
- `discount_type` — Pricing/discount category
- `commitment_eligible` — Whether usage may be relevant for commitment analysis

### Environment and ownership fields

- `environment` — dev, staging, prod, or shared
- `team` — Team or owner group
- `product` — Product line or functional area
- `customer_segment` — Segment such as SMB, mid-market, or enterprise
- `cost_center` — Finance cost center or budget owner
- `owner` — Named owner where available
- `is_tagged` — Whether the row meets required tagging criteria
- `allocation_confidence` — Confidence level for assigning cost to a responsible group

### AI and workload fields

- `ai_feature` — AI-related feature or workload type
- `model_tier` — Model category or cost/quality tier
- `request_count` — Number of requests
- `input_tokens` — Input token volume
- `output_tokens` — Output token volume
- `cache_hit_rate` — Cache hit ratio where relevant
- `latency_band` — Latency bucket
- `quality_tier` — Quality expectation tier

### Business context fields

- `monthly_revenue_proxy` — Approximate revenue associated with the relevant business area
- `active_customers` — Estimated active customer count
- `workflows_processed` — Approximate workflow volume
- `enterprise_customer_flag` — Whether the segment includes important enterprise customers
- `sla_tier` — Service level expectation

### Diagnostic support fields

- `anomaly_flag` — Indicator that usage or spend may be unusual
- `waste_flag` — Indicator that a row may reflect inefficient or unnecessary usage
- `political_sensitivity` — Relative sensitivity of the associated recommendation
- `notes` — Optional free-text context

## Analysis expectations

The schema is intended to support analysis such as:

- spend by service
- spend by environment
- spend by team or product
- tagged vs untagged cost
- AI-related cost behavior
- usage-linked unit economics
- potential optimization opportunities
- prioritization of actions under uncertainty

## Working guidance

When using this dataset:

- Treat it as realistic but imperfect.
- Expect ambiguity in ownership and allocation.
- Make assumptions explicit in your analysis.
- Use the data to support business judgment, not just technical reporting.

The goal of the case is not merely to summarize spend, but to move from visibility to decisions and operating action.