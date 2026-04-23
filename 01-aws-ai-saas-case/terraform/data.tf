resource "aws_s3_bucket" "finops_data" {
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