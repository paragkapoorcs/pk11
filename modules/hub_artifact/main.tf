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

data "google_client_config" "current" {}
terraform {
  required_providers {
    cdap = {
      source = "GoogleCloudPlatform/cdap"
      version = "0.9.0"
    }
  }
}

provider "cdap" {
  host  = "https://t1-sap-cdf-comp-sap-adapter-dot-euw1.datafusion.googleusercontent.com/api/"
  token = data.google_client_config.current.access_token
}

resource "cdap_local_artifact" "sap-odp-plugins" {
  name             = "sap-odp-plugins"
  version          = "0.0.12-SNAPSHOT"
  json_config_path = "/Users/paragkapoor/Downloads/sap-odp-plugins-0.0.12-SNAPSHOT.json"
  jar_binary_path  = "/Users/paragkapoor/Downloads/sap-odp-plugins-0.0.12-SNAPSHOT.jar"
}
