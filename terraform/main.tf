terraform {
  required_version = ">= 1.5.0"

  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = var.github_owner
}

resource "github_actions_secret" "kite_api_key" {
  repository      = var.github_repository
  secret_name     = "KITE_API_KEY"
  plaintext_value = var.kite_api_key
}
