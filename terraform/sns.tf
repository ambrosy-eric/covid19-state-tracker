resource "aws_sns_topic" "personal_emailer" {
  name              = "personal_emailer"
  kms_master_key_id = "alias/aws/sns"
}
// no subscriptions as email is not a supported subscription type