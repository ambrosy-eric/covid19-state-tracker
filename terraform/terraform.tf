provider "aws" {
  region  = "us-east-1"
}

terraform {
  backend "s3" {
    bucket  = "ambrosy-terraform"
    key     = "covid.tfstate"
    encrypt = "true"
    region  = "us-east-1"
  }
}

data "aws_caller_identity" "current" {
}