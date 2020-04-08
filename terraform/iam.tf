data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lambda" {
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
  tags               = var.tags
}

resource "aws_iam_role_policy" "lambda_sns_attachment" {
  role   = aws_iam_role.lambda.name
  policy = data.aws_iam_policy_document.lambda_sns.json
}

data "aws_iam_policy_document" "lambda_sns" {
  statement {
    actions   = ["sns:Publish"]
    resources = ["arn:aws:sns:us-east-1:${data.aws_caller_identity.current.account_id}:personal_emailer"]
    effect    = "Allow"
  }
}

data "aws_iam_policy_document" "logs" {
  statement {
    effect    = "Allow"
    actions   = ["logs:CreateLogGroup"]
    resources = ["*"]
  }
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:*:*:*"]
  }
}

resource "aws_iam_policy" "logs" {
  policy = data.aws_iam_policy_document.logs.json
}

resource "aws_iam_role_policy_attachment" "logs" {
  role       = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.logs.arn
}