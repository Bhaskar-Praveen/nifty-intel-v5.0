variable "github_token" {
  description = "GitHub Personal Access Token (repo scope)"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub username or organization"
  type        = string
}

variable "github_repository" {
  description = "GitHub repository name (without .git)"
  type        = string
}

variable "kite_api_key" {
  description = "Zerodha Kite API Key"
  type        = string
  sensitive   = true
}
