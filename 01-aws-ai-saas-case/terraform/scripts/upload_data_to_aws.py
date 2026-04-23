import os, textwrap
base = 'output/clarionflow-terraform-split'
os.makedirs(base, exist_ok=True)
files = {
  'main.tf': '''terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = local.default_tags
  }
}

locals {
  default_tags = {
    Project       = var.project_name
    Environment   = var.environment
    ManagedBy     = "terraform"
    Assessment    = "100-day-finops-architecture"
    PortfolioRole = "pe-owned-platform"
    CaseStudy     = "case-01-clarionflow-ai"
  }

  accounts = {
    acquired_ai_platform = {
      account_name  = "acquired-ai-platform"
      workload      = "ai-platform"
      business_unit = "acquired-product"
    }
    legacy_core_prod = {
      account_name  = "legacy-core-prod"
      workload      = "core-saas"
      business_unit = "legacy-platform"
    }
    shared_services = {
      account_name  = "shared-services"
      workload      = "shared"
      business_unit = "central-platform"
    }
  }
}
''',
  'variables.tf': '''variable "aws_region" {
  description = "AWS region for the inherited ClarionFlow AI baseline environment"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Top-level environment label"
  type        = string
  default     = "post-acquisition"
}

variable "project_name" {
  description = "Project identifier for shared tagging"
  type        = string
  default     = "clarionflow-ai"
}

variable "notification_emails" {
  description = "Email addresses for budget alerts"
  type        = list(string)
  default = [
    "finops@clarionflow.example.com",
    "cfo@clarionflow.example.com"
  ]
}

variable "monthly_budget_limit_usd" {
  description = "Default monthly budget limit applied to each logical account budget"
  type        = number
  default     = 5000
}
''',
  'network.tf': '''resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private_a" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.11.0/24"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public_a.id
}
''',
  'compute.tf': '''resource "aws_ecs_cluster" "clarionflow" {
  name = "${var.project_name}-cluster"
}

resource "aws_ecs_task_definition" "fargate_app" {
  family                   = "${var.project_name}-app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = "[]"
}

resource "aws_lambda_function" "worker" {
  function_name = "${var.project_name}-worker"
  role          = "arn:aws:iam::123456789012:role/dummy-role"
  handler       = "index.handler"
  runtime       = "python3.11"
  filename      = "lambda.zip"
}
''',
  'data.tf': '''resource "aws_s3_bucket" "finops_data" {
  bucket = "${var.project_name}-finops-data"
}

resource "aws_rds_instance" "app_db" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  name                 = "clarionflow"
  username             = "appuser"
  password             = "changeme123!"
  skip_final_snapshot  = true
}

resource "aws_glue_catalog_database" "finops" {
  name = "${var.project_name}-finops"
}
''',
  'observability.tf': '''resource "aws_cloudwatch_dashboard" "finops_overview" {
  dashboard_name = "${var.project_name}-finops-overview"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "text",
        x      = 0,
        y      = 0,
        width  = 24,
        height = 4,
        properties = {
          markdown = "# ClarionFlow AI FinOps Overview"
        }
      }
    ]
  })
}
''',
  'budgets.tf': '''resource "aws_sns_topic" "budget_alerts" {
  name = "${var.project_name}-budget-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  for_each  = toset(var.notification_emails)
  topic_arn = aws_sns_topic.budget_alerts.arn
  protocol  = "email"
  endpoint  = each.value
}

resource "aws_budgets_budget" "monthly_cost_budget" {
  for_each = local.accounts

  name              = "${var.project_name}-${each.value.account_name}-monthly-budget"
  budget_type       = "COST"
  limit_amount      = tostring(var.monthly_budget_limit_usd)
  limit_unit        = "USD"
  time_unit         = "MONTHLY"
  time_period_start = "2026-01-01_00:00"

  cost_filter {
    name   = "TagKeyValue"
    values = ["AccountName$${each.value.account_name}"]
  }

  notification {
    comparison_operator       = "GREATER_THAN"
    threshold                 = 80
    threshold_type            = "PERCENTAGE"
    notification_type         = "ACTUAL"
    subscriber_sns_topic_arns = [aws_sns_topic.budget_alerts.arn]
  }
}
''',
  'outputs.tf': '''output "assessment_scope" {
  value = {
    project_name = var.project_name
    environment  = var.environment
    accounts     = [for v in local.accounts : v.account_name]
    region       = var.aws_region
  }
}
''',
  'README.md': '''# ClarionFlow AI Terraform Split Baseline

This layout shows a clean split for the ClarionFlow AI case so the environment, dataset, and architecture context line up.

Files:
- `main.tf` – provider, shared locals, logical accounts
- `variables.tf` – shared inputs
- `network.tf` – minimal VPC, subnets, NAT Gateway
- `compute.tf` – ECS/Fargate and Lambda placeholders
- `data.tf` – S3, RDS, Glue scaffolding for data/analysis
- `observability.tf` – CloudWatch dashboard
- `budgets.tf` – Budgets + SNS alerts
- `outputs.tf` – scope outputs for reports

This is intentionally lightweight and illustrative; you can tighten, parameterize, or expand each area as you refine the case.
'''
}

for name, content in files.items():
    with open(os.path.join(base, name), 'w') as f:
        f.write(textwrap.dedent(content))

print(os.listdir(base))