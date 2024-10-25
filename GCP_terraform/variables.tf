variable "credentials" {
  description = "The path to the service account key file"
  type        = string  
  
}

variable "project" {
  description = "The GCP project ID"
  type        = string 
  
}

variable "region" {
  description = "The GCP region"
  type        = string  
  
}

variable "location" {
  description = "The GCP location"
  type        = string  
  
}

variable "bucket_name" {
  description = "The GCS bucket name"
  type        = string
  
}
