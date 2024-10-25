provider "google" {
  credentials = file()
  project     = var.project
  region      = var.region
}
resource "google_storage_bucket" "terraform_state" {
  name     = var.bucket_name
  location = var.region

  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  force_destroy               = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  project    = var.project
  location   = var.location
  delete_contents_on_destroy=true
}