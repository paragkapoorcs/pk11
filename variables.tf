/**
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

variable "name" {
  description = "Name of the instance."
  type        = string
}

variable "project" {
  description = "The project ID to deploy to."
  type        = string
}

variable "network" {
  description = "Name for VPC to create or reuse to be configured for use with private Data Fusion instance."
  type        = string
}

variable "dataproc_subnet" {
  description = "Name for subnet to create and configure for Dataproc clusters controlled by private Data Fusion instance."
  type        = string
  default     = "dataproc-subnet"
}

variable "description" {
  description = "An optional description of the instance."
  type        = string
  default     = null
}

variable "region" {
  description = "The region of the instance."
  type        = string
}

variable "type" {
  description = "Represents the type of the instance (BASIC or ENTERPRISE)"
  type        = string
  default     = "ENTERPRISE"
}

variable "labels" {
  description = "The resource labels for instance to use to annotate any related underlying resources, such as Compute Engine VMs."
  type        = map(string)
  default     = {}
}

variable "options" {
  description = "Map of additional options used to configure the behavior of Data Fusion instance."
  type        = map(string)
  default     = {}
}

variable "compute_service_account" {
  description = "Google Managed Compute Service Account Email"
}

variable "ip_allocation" {
  type       = string
}

variable "composer_env_name" {
  description = "Name of Cloud Composer Environment"
  type        = string
}

variable "subnetwork" {
  description = "Subetwork where Cloud Composer is created."
  type        = string
}

variable "owner_email" {
  description = "BQ_Dataset Owner Email ID."
  type        = string
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
  description = "BQ_Dataset L1 Fact Dataset ID."
  type        = string
}
variable "canonical_dataset" {
  description = "BQ_Dataset L2 Canonical Dataset Name."
  type        = string
}

variable "canonical_id" {
  description = "BQ_Dataset L2 Canonical Dataset ID."
  type        = string
}

variable "location" {
  description = "BQ_Dataset Locatio Like EU / US."
  type        = string
}
