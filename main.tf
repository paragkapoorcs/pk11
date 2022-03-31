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
####################################################################################
# Data Fusion Instance
####################################################################################
module "data_fusion_network" {
  source                      = "./modules/private_network"
  project_id                  = var.project
  tenant_project              = module.instance.tenant_project
  instance                    = module.instance.instance.name
  network                     = var.network
  region                      = var.region
}

module "instance" {
  source = "./modules/instance"

  name        = var.name
  project     = var.project
  description = var.description
  region      = var.region
  type        = var.type
  labels      = var.labels
  options     = var.options
  network       = var.network
  ip_allocation = var.ip_allocation
  
}
####################################################################################
# Composer Instance
####################################################################################

module "composer-environment" {
  source = "./modules/create_environment"

  project_id        = var.project
  composer_env_name = var.composer_env_name
  region            = var.region
  network           = var.network
  subnetwork        = var.subnetwork
}

module "copydag" {
  source = "./modules/copydag"

  bucket = module.composer-environment.gcs_bucket
#  bucket = "gs://europe-west1-pktestfin1-9a3e9e20-bucket/dags"
}
####################################################################################
# BQ Dataset L0 Staging  
####################################################################################

resource "google_bigquery_dataset" "bq-data-set" {
     dataset_id                      = var.fd_name
     friendly_name                   = var.fd_id
     default_table_expiration_ms = 3600000
     description                     = "SCM Dataset"
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = var.location
     project                         = var.project
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

####################################################################################
# BQ Dataset L0 Staging Tables
####################################################################################

resource "google_bigquery_table" "bq-data-set" {
  dataset_id = google_bigquery_dataset.bq-data-set.dataset_id
  table_id   = "layer1_audit_table"
  project = google_bigquery_dataset.bq-data-set.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L0_Scripts/layer1_audit_table.json")
}

####################################################################################
# BQ Dataset L1 Dimension 
####################################################################################

resource "google_bigquery_dataset" "dimention" {
     dataset_id                      = var.dd_name
     friendly_name                   = var.dd_id
     default_table_expiration_ms = 3600000
     description                     = "SCM Dataset"
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = var.location
     project                         = var.project
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

####################################################################################
# BQ Dataset L1 Dimension Tables
####################################################################################

resource "google_bigquery_table" "dimention" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "company_code_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/company_code_dimension.json")
}

resource "google_bigquery_table" "dimention1" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "customer_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/customer_dimension.json")
}

resource "google_bigquery_table" "dimention2" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "customer_sales_org_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/customer_sales_org_dimension.json")
}

resource "google_bigquery_table" "dimention3" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "material_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/material_dimension.json")
}

resource "google_bigquery_table" "dimention4" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "plant_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/plant_dimension.json")
}

resource "google_bigquery_table" "dimention5" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "supplier_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/supplier_dimension.json")
}

resource "google_bigquery_table" "dimention6" {
  dataset_id = google_bigquery_dataset.dimention.dataset_id
  table_id   = "supplier_purchase_org_dimension"
  project = google_bigquery_dataset.dimention.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/dimension/supplier_purchase_org_dimension.json")
}

####################################################################################
# BQ Dataset L1 Fact
####################################################################################

resource "google_bigquery_dataset" "fact" {
     dataset_id                      = var.fact_name
     friendly_name                   = var.fact_id
     default_table_expiration_ms = 3600000
     description                     = "SCM Dataset"
     labels                          = {
         "env" = "scl-twin"
        }
     location                        = var.location
     project                         = var.project
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

####################################################################################
# BQ Dataset L1 Fact  Tables
####################################################################################

resource "google_bigquery_table" "fact" {
  dataset_id = google_bigquery_dataset.fact.dataset_id
  table_id   = "layer1_audit_table"
  project = google_bigquery_dataset.fact.project
  time_partitioning {
    type = "DAY"
  }

  labels = {	
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/fact/delivery_fact.json")
}

resource "google_bigquery_table" "fact1" {
  dataset_id = google_bigquery_dataset.fact.dataset_id
  table_id   = "inventory_fact"
  project = google_bigquery_dataset.fact.project
  time_partitioning {
    type = "DAY"
  }

  labels = {   
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/fact/inventory_fact.json")
}

resource "google_bigquery_table" "fact2" {
  dataset_id = google_bigquery_dataset.fact.dataset_id
  table_id   = "production_order_fact"
  project = google_bigquery_dataset.fact.project
  time_partitioning {
    type = "DAY"
  }

  labels = {   
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/fact/production_order_fact.json")
}

resource "google_bigquery_table" "fact3" {
  dataset_id = google_bigquery_dataset.fact.dataset_id
  table_id   = "purchase_order_fact"
  project = google_bigquery_dataset.fact.project
  time_partitioning {
    type = "DAY"
  }

  labels = {   
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/fact/purchase_order_fact.json")
}

resource "google_bigquery_table" "fact4" {
  dataset_id = google_bigquery_dataset.fact.dataset_id
  table_id   = "sales_order_fact"
  project = google_bigquery_dataset.fact.project
  time_partitioning {
    type = "DAY"
  }

  labels = {   
    env = "scl-twin"
  }

  schema = file("./L1_Scripts/fact/sales_order_fact.json")
}

####################################################################################
# BQ Dataset L2 Canonical
####################################################################################

resource "google_bigquery_dataset" "canonical" {
     dataset_id                      = var.canonical_dataset
     default_partition_expiration_ms = 0
     delete_contents_on_destroy      = false
     description                     = "SCM Dataset"
     friendly_name                   = var.canonical_id
     labels                          = {
         "env" = "default"
        }
     location                        = var.location
     project                         = var.project

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
####################################################################################
# BQ Dataset L2 Canonical Tables
####################################################################################
resource "google_bigquery_table" "canonical" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "asset"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/asset.json")
}

resource "google_bigquery_table" "canonical1" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "forcast"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/forecast.json")
}

resource "google_bigquery_table" "canonical2" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "inventory"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/inventory.json")
}

resource "google_bigquery_table" "canonical3" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "legal_entity"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/legal_entity.json")
}

resource "google_bigquery_table" "canonical4" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "location"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/location.json")
}

resource "google_bigquery_table" "canonical5" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "order"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/order.json")
}

resource "google_bigquery_table" "canonical6" {
  dataset_id = google_bigquery_dataset.canonical.dataset_id
  table_id   = "product"
  project = google_bigquery_dataset.canonical.project
  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = "scl-twin"
  }

  schema = file("./L2_Scripts/product.json")
}

