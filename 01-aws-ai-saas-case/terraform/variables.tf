variable "aws_region" {
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