resource "aws_lambda_function" "lambda_covid" {
  function_name = "covid-scraper"
  description   = "Scraps IDPH & ODH for covid-19 spread information"
  role          = aws_iam_role.lambda.arn
  handler       = "handler.entry"
  memory_size   = 256
  runtime       = "python3.7"
  timeout       = var.timeout
  tags          = var.tags
  s3_bucket     = "ambrosy-lambda-source-bucket"
  s3_key        = "covid-scraper/branch/master.zip"
}
