#Copyright 2021 Google Inc. All rights reserved.

#The use of this software is governed by the Pre-GA Offering 
#Terms section of the the Service Specific Terms set forth at 
#https://cloud.google.com/terms/service-terms#general-service-terms

resource "google_bigquery_dataset" "bq-data-set" {
     dataset_id                      = var.fd_name
     default_partition_expiration_ms = 0
     delete_contents_on_destroy      = false
     description                     = "SCM Dataset"
     friendly_name                   = var.fd_id
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = "EU"
     project                         = var.project_id


     access {
         role          = "OWNER"
         user_by_email = var.owner_email
        }
     access {
         role          = "OWNER"
         special_group = "projectOwners"
        }
     access {
         role          = "READER"
         special_group = "projectReaders"
        }
     access {
         role          = "WRITER"
         special_group = "projectWriters"
        }
}

resource "google_bigquery_dataset" "bq-data-set_dimention" {
     dataset_id                      = var.dd_name
     default_partition_expiration_ms = 0
     delete_contents_on_destroy      = false
     description                     = "SCM Dataset"
     friendly_name                   = var.dd_id
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = "EU"
     project                         = var.project_id

     access {
         role          = "OWNER"
         user_by_email = var.owner_email
        }
     access {
         role          = "OWNER"
         special_group = "projectOwners"
        }
     access {
         role          = "READER"
         special_group = "projectReaders"
        }
     access {
         role          = "WRITER"
         special_group = "projectWriters"
        }
}

resource "google_bigquery_dataset" "bq-data-set_fact" {
     dataset_id                      = var.fact_name
     default_partition_expiration_ms = 0
     delete_contents_on_destroy      = false
     description                     = "SCM Dataset"
     friendly_name                   = var.fact_id
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = "EU"
     project                         = var.project_id

     access {
         role          = "OWNER"
         user_by_email = var.owner_email
        }
     access {
         role          = "OWNER"
         special_group = "projectOwners"
        }
     access {
         role          = "READER"
         special_group = "projectReaders"
        }
     access {
         role          = "WRITER"
         special_group = "projectWriters"
        }
}
