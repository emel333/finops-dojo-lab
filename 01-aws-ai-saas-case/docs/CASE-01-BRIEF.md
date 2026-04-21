# Case 01: ClarionFlow AI
## 100-Day Post-Acquisition FinOps and Architecture Assessment

## Context

ClarionFlow AI is a mid-market B2B SaaS company that provides AI-assisted workflow automation for operations teams. 

The platform has expanded its AI-enabled features over the past 12 months and has seen growth in customer usage, product complexity, and cloud spend.

The company has recently been acquired.

During the first 100 days, leadership wants a clear understanding of AWS cost drivers, areas of operational inefficiency, and the actions required to improve financial discipline without undermining growth or product delivery.


## Your Role

You are acting as an interim FinOps practitioner embedded in the business during the post-acquisition period.

Your job is to help leadership answer a practical question:

**How should ClarionFlow AI improve cloud cost visibility, operating discipline, and AWS efficiency over the next 100 days while preserving business momentum?**



## Business Situation

Leadership has identified several concerns:
- AWS spend has risen quickly over the past year.
- New AI-related features appear to be changing cost patterns.
- Finance lacks confidence in current cost visibility and allocation.
- Engineering has focused primarily on speed, uptime, and delivery.
- Shared services and environments may not be consistently governed.
- Leadership wants actionable recommendations, not just reporting.

The company needs:
- clearer spend visibility,
- a view of major cost drivers,
- a practical optimization plan,
- and an operating cadence for ongoing FinOps work.




## Stakeholders

You should assume the case involves the following stakeholder perspectives:

- **CEO** — wants clarity, action, and confidence in the operating plan.
- **CFO** — wants improved visibility, better forecasting, and margin discipline.
- **CTO** — wants to maintain reliability and engineering effectiveness.
- **VP Product** — wants AI-enabled features to continue supporting growth.
- **Engineering Managers** — want recommendations that are practical and technically credible.
- **Sales / Customer-facing leadership** — want cost actions that do not harm important customer relationships.




## Your Objectives

Your deliverables should help the company:

1. Understand the current AWS cost structure.
2. Identify likely areas of inefficiency, waste, or poor allocation.
3. Separate technical issues from process and governance issues.
4. Recommend a 30/60/90-day action plan.
5. Define a realistic ongoing FinOps operating cadence.
6. Develop an initial view of unit economics, forecastability, and financial risks relevant to CFO and post-acquisition decision-making.




## Materials You Will Use

You will work from:

- a synthetic AWS cost and usage dataset,
- a provided Terraform v1 configuration for the baseline AWS environment,
- a simplified AWS architecture scope,
- your own analysis in Python / notebooks / SQL,
- CloudWatch dashboards or equivalent analytical views,
- and supporting documentation in the repo.

The dataset is designed to support realistic FinOps analysis and should be treated as a stand-in for cloud billing and usage records.

The Terraform v1 configuration is provided so you can stand up the initial environment, load or connect the dataset, and then treat that environment as the inherited baseline for the rest of the case.




## Required Deliverables

Produce the following:

- A baseline AWS cost analysis
- A view of spending by major dimension (such as service, environment, team, or product)
- A list of prioritized optimization opportunities
- A 30/60/90-day action plan
- A detailed analyst report (`CASE-01-REPORT.md`)
- A short executive brief or presentation (`CASE-01-EXECUTIVE-BRIEF.md` or slides)
- A proposed weekly and monthly FinOps operating cadence
- A CloudWatch dashboard or equivalent visibility layer for key metrics, trends, and findings




## Working Assumptions

As you work the case, make your assumptions explicit.

Where data is incomplete or ambiguous:
- state the limitation,
- explain how it affects your interpretation,
- and avoid false precision.

Your job is not only to identify cost issues, but to demonstrate sound practitioner judgment under realistic business conditions.




## Guiding Questions

As you work the case, consider:

- What appears to be driving AWS spend?
- Which spending patterns are easy to explain, and which require deeper investigation?
- Which findings are primarily technical? Which are organizational?
- What actions would be safe and high-confidence in the first 30 days?
- What actions require more validation, stakeholder buy-in, or architectural review?
- What operating rhythm would help the company improve continuously rather than react occasionally?




## Learning Objectives (Platform + FinOps)

By completing this case, you should be able to:

- Explain the end-to-end AWS architecture (network, app, data, observability) in plain language.
- Walk through each Terraform file and describe what resources it manages and why.
- Describe how cost, performance, and reliability tradeoffs influenced the design.
- Modify the Terraform configuration safely in response to a change request (e.g., new region, new SLO, budget cut).