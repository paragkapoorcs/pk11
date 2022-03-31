#Copyright 2021 Google Inc. All rights reserved.

#The use of this software is governed by the Pre-GA Offering 
#Terms section of the the Service Specific Terms set forth at 
#https://cloud.google.com/terms/service-terms#general-service-terms


#variable "project_id" {
#  description = "Project where the dataset and table are created."
#}

variable "delete_contents_on_destroy" {
  description = "(Optional) If set to true, delete all the tables in the dataset when destroying the resource; otherwise, destroying the resource will fail if tables are present."
  type        = bool
  default     = null
}


variable "project_id" {
  description = "Google Cloud Project ID"
}

variable "datasetmain" {
  description = "Dataset Name"
  default = "scm_twin_full_dataset"
}


variable "fd_name" {
  description = "BQ_Dataset L0 Full Load Dataset Name."
  type        = string
}

variable "fd_id" {
  description = "BQ_Dataset L0 Full Load Dataset ID."
  type        = string
}

variable "dd_name" {
  description = "BQ_Dataset L1 Dimension Dataset Name."
  type        = string
}

variable "dd_id" {
  description = "BQ_Dataset L1 Dimension Dataset ID."
  type        = string
}

variable "fact_name" {
  description = "BQ_Dataset L1 Fact Dataset Name."
  type        = string
}

variable "fact_id" {
  description = "BQ_Dataset L1 fact Dataset ID."
  type        = string
}


variable "owner_email" {
  description = "Google BQ Dataset Owner Email ID"
}

