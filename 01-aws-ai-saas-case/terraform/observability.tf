resource "aws_cloudwatch_dashboard" "finops_overview" {
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