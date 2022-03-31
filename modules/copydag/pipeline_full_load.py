import os

from airflow import models
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.datafusion import (CloudDataFusionStartPipelineOperator)
from airflow.utils import dates
from airflow.utils.state import State
from airflow.utils.dates import days_ago
from random import randint

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 20),
    'email': ['paragkapoor@google.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1
    #'retry_delay': timedelta(seconds=5),
}

with models.DAG(

    "full_load_demo_pk_cdf-odp-looker-dev-6-4-basic",

    schedule_interval=None,

    start_date=dates.days_ago(1),

    catchup=False

) as dag:

    Pipeline1 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0ASSET_ATTR_TEXT_asset_subnumber_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline1"
    )

    Pipeline2 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0BP_DEF_ADDRESS_ATTR_business_partner_address_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline2"
    )
    Pipeline3 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUST_COMPC_ATTR_customer_company_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline3"
    )
    Pipeline4 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUST_SALES_ATTR_customer_sales_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline4"
    )
    Pipeline5 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUSTOMER_ATTR_customer_master_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline5"
    )
    Pipeline6 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0FI_GL_4_general_ledger_line_items_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline6"
    )
    Pipeline7 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MAT_PLANT_ATTR_material_plant_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline7"
    )
    Pipeline8 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MAT_ST_LOC_ATTR_material_storage_location_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline8"
    )
    Pipeline9 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MATERIAL_ATTR_material_master_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline9"
    )
    Pipeline10 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MATERIAL_TEXT_material_description_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline10"
    )
    Pipeline11 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PLANT_ATTR_plant_master_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline11"
    )
    Pipeline12 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PP_MD_MATERIAL_material_data_source_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline12"
    )
    Pipeline13 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PRODORDER_ATTR_production_orders_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline13"
    )
    Pipeline14 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0VEN_PURORG_ATTR_supplier_purchasing_organization_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="sPipeline14"
    )
    Pipeline15 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0VENDOR_ATTR_supply_master_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline15"
    )
    Pipeline16 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_02_HDR_purchasing_header_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline16"
    )
    Pipeline17 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_02_ITM_purchasing_item_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline17"
    )
    Pipeline18 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_03_BF_material_movements_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline18"
    )
    Pipeline19 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_03_BX_stock_initialization_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline19"
    )
    Pipeline20 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_04_P_MATNR_material_production_planning_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline20"
    )
    Pipeline21 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_06_INV_invoice_verification_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline21"
    )
    Pipeline22 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VAHDR_sales_document_header_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline22"
    )
    Pipeline23 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VAITM_sales_document_item_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline23"
    )
    Pipeline24 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VASCL_sales_document_schedule_line_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline24"
    )
    Pipeline25 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VASTH_order_header_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline25"
    )
    Pipeline26 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VASTI_order_item_data_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline26"
    )
    Pipeline27 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCHDR_delivery_header_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline27"
    )
    Pipeline28 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCITM_delivery_item_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline28"
    )
    Pipeline29 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCSCL_schedule_line_delivery_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline29"
    )
    Pipeline30 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_13_VDHDR_billing_document_header_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline30"
    )
    Pipeline31 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_13_VDITM_billing_document_item_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100', 'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Pipeline31"
    )

    Pipeline1 >> Pipeline2 >> Pipeline3 >> Pipeline4 >> Pipeline5 >> Pipeline6 >> Pipeline7 >> Pipeline8 >> Pipeline9 >> Pipeline10
    Pipeline11 >> Pipeline12 >> Pipeline13 >> Pipeline14 >> Pipeline15 >> Pipeline16 >> Pipeline17 >> Pipeline18 >> Pipeline19 >> Pipeline20
    Pipeline21 >> Pipeline22 >> Pipeline23 >> Pipeline24 >> Pipeline25 >> Pipeline26 >> Pipeline27 >> Pipeline28 >> Pipeline29 >> Pipeline30 >> Pipeline31
