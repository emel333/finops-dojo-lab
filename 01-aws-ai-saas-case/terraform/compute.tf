resource "aws_ecs_cluster" "clarionflow" {
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