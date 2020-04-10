# cloudwatch event triggers 
# real infra should have this as a module to consume but meh

resource "aws_cloudwatch_event_rule" "illinois" {
  name                = "ill-run"
  description         = "kicks off the illinois covid-19 case function"
  schedule_expression = "cron(0 23 ? * * *)"
}

resource "aws_cloudwatch_event_target" "illinois" {
  rule  = aws_cloudwatch_event_rule.illinois.name
  arn   = aws_lambda_function.lambda_covid.arn
  input = "{\"illinois\" : \"run\"}"
}

resource "aws_lambda_permission" "illinois" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_covid.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.illinois.arn
}

resource "aws_cloudwatch_event_rule" "ohio" {
  name                = "ohio-run"
  description         = "kicks off the ohio covid-19 case function"
  schedule_expression = "cron(0 21 ? * * *)"
}

resource "aws_cloudwatch_event_target" "ohio" {
  rule  = aws_cloudwatch_event_rule.ohio.name
  arn   = aws_lambda_function.lambda_covid.arn
  input = "{\"ohio\" : \"run\"}"
}

resource "aws_lambda_permission" "ohio" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_covid.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ohio.arn
}

resource "aws_cloudwatch_event_rule" "county" {
  name                = "county-run"
  description         = "kicks off the county covid-19 case function"
  schedule_expression = "cron(15 2 ? * * *)"
}

resource "aws_cloudwatch_event_target" "county" {
  rule  = aws_cloudwatch_event_rule.county.name
  arn   = aws_lambda_function.lambda_covid.arn
  input = "{\"county\" : \"run\"}"
}

resource "aws_lambda_permission" "county" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_covid.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.county.arn
}