output "assessment_scope" {
  value = {
    project_name = var.project_name
    environment  = var.environment
    accounts     = [for v in local.accounts : v.account_name]
    region       = var.aws_region
  }
}