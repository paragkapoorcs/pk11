import os

from airflow import models
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.datafusion import (CloudDataFusionStartPipelineOperator)
from airflow.providers.google.cloud.sensors.datafusion import CloudDataFusionPipelineStateSensor
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

    "delta_load_demo_pk_cdf-odp-looker-dev-6-4-basic",

    schedule_interval=None,

    start_date=dates.days_ago(1),

    catchup=False

) as dag:
    run_this_first = DummyOperator(
        task_id='Start',
    )

    run1 = DummyOperator(
        task_id='R1',
    )

    run2 = DummyOperator(
        task_id='R2',
    )

    run3 = DummyOperator(
        task_id='R3',
    )

    run4 = DummyOperator(
        task_id='R4',
    )

    run5 = DummyOperator(
        task_id='R5',
    )

    run6 = DummyOperator(
        task_id='R6',
    )

    run7 = DummyOperator(
        task_id='R7',
    )

    run8 = DummyOperator(
        task_id='R8',
    )

    run9 = DummyOperator(
        task_id='R9',
    )

    run_this_last = DummyOperator(
        task_id='End',
    )

    Pipeline1 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0ASSET_ATTR_TEXT_asset_subnumber_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="asset_subnumber"
    )

    Pipechk1 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk1",
        pipeline_name='0ASSET_ATTR_TEXT_asset_subnumber_delta_demo_pk',
        pipeline_id=Pipeline1.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline2 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUST_COMPC_ATTR_customer_company_data_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="customer_company_data"
    )

    Pipechk2 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk2",
        pipeline_name='0CUST_COMPC_ATTR_customer_company_data_delta_demo_pk',
        pipeline_id=Pipeline2.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline3 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUST_SALES_ATTR_customer_sales_data_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="customer_sales_data"
    )

    Pipechk3 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk3",
        pipeline_name='0CUST_SALES_ATTR_customer_sales_data_delta_demo_pk',
        pipeline_id=Pipeline3.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline4 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0CUSTOMER_ATTR_customer_master_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="customer_master_delta"
    )

    Pipechk4 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk4",
        pipeline_name='0CUSTOMER_ATTR_customer_master_delta_demo_pk',
        pipeline_id=Pipeline4.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline5 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MAT_ST_LOC_ATTR_material_storage_location_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_storage_location"
    )

    Pipechk5 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk5",
        pipeline_name='0MAT_ST_LOC_ATTR_material_storage_location_delta_demo_pk',
        pipeline_id=Pipeline5.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline6 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MAT_PLANT_ATTR_material_plant_data_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_plant_data"
    )

    Pipechk6 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk6",
        pipeline_name='0MAT_PLANT_ATTR_material_plant_data_delta_demo_pk',
        pipeline_id=Pipeline6.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline7 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MATERIAL_ATTR_material_master_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_master_delta"
    )

    Pipechk7 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk7",
        pipeline_name='0MATERIAL_ATTR_material_master_delta_demo_pk',
        pipeline_id=Pipeline7.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline8 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0MATERIAL_TEXT_material_description_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_description"
    )

    Pipechk8 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk8",
        pipeline_name='0MATERIAL_TEXT_material_description_delta_demo_pk',
        pipeline_id=Pipeline8.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline9 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PP_MD_MATERIAL_material_data_source_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_data_source"
    )

    Pipechk9 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk9",
        pipeline_name='0PP_MD_MATERIAL_material_data_source_delta_demo_pk',
        pipeline_id=Pipeline9.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline10 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PLANT_ATTR_plant_master_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="plant_master"
    )

    Pipechk10 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk10",
        pipeline_name='0PLANT_ATTR_plant_master_delta_demo_pk',
        pipeline_id=Pipeline10.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline11 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0VENDOR_ATTR_supply_master_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="supply_master"
    )

    Pipechk11 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk11",
        pipeline_name='0VENDOR_ATTR_supply_master_delta_demo_pk',
        pipeline_id=Pipeline11.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline12 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0BP_DEF_ADDRESS_ATTR_business_partner_address_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="business_partner_address"
    )

    Pipechk12 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk12",
        pipeline_name='0BP_DEF_ADDRESS_ATTR_business_partner_address_delta_demo_pk',
        pipeline_id=Pipeline12.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline13 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0PRODORDER_ATTR_production_orders_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="production_orders"
    )

    Pipechk13 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk13",
        pipeline_name='0PRODORDER_ATTR_production_orders_delta_demo_pk',
        pipeline_id=Pipeline13.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline14 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0VEN_PURORG_ATTR_supplier_purchasing_organization_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="supplier_purchasing_organization"
    )

    Pipechk14 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk14",
        pipeline_name='0VEN_PURORG_ATTR_supplier_purchasing_organization_delta_demo_pk',
        pipeline_id=Pipeline14.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline15 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_03_BF_material_movements_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_movements"
    )

    Pipechk15 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk15",
        pipeline_name='2LIS_03_BF_material_movements_delta_demo_pk',
        pipeline_id=Pipeline15.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline16 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_03_BX_stock_initialization_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="Stock_initialization"
    )

    Pipechk16 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk16",
        pipeline_name='2LIS_03_BX_stock_initialization_delta_demo_pk',
        pipeline_id=Pipeline16.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline17 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_02_HDR_purchasing_header_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="purchasing_header"
    )

    Pipechk17 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk17",
        pipeline_name='2LIS_02_HDR_purchasing_header_delta_demo_pk',
        pipeline_id=Pipeline17.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline18 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_02_ITM_purchasing_item_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="purchasing_item"
    )

    Pipechk18 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk18",
        pipeline_name='2LIS_02_ITM_purchasing_item_delta_demo_pk',
        pipeline_id=Pipeline18.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline19 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VAHDR_sales_document_header_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="sales_document_header"
    )

    Pipechk19 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk19",
        pipeline_name='2LIS_11_VAHDR_sales_document_header_delta_demo_pk',
        pipeline_id=Pipeline19.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline20 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VAITM_sales_document_item_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="sales_document_item"
    )

    Pipechk20 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk20",
        pipeline_name='2LIS_11_VAITM_sales_document_item_delta_demo_pk',
        pipeline_id=Pipeline20.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline22 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_11_VASCL_sales_document_schedule_line_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="sales_document_schedule_line"
    )

    Pipechk22 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk22",
        pipeline_name='2LIS_11_VASCL_sales_document_schedule_line_delta_demo_pk',
        pipeline_id=Pipeline22.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline23 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCSCL_schedule_line_delivery_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="schedule_line_delivery"
    )

    Pipechk23 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk23",
        pipeline_name='2LIS_12_VCSCL_schedule_line_delivery_delta_demo_pk',
        pipeline_id=Pipeline23.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline24 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_13_VDHDR_billing_document_header_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="billing_document_header"
    )

    Pipechk24 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk24",
        pipeline_name='2LIS_13_VDHDR_billing_document_header_delta_demo_pk',
        pipeline_id=Pipeline24.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline25 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_13_VDITM_billing_document_item_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="billing_document_item"
    )

    Pipechk25 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk25",
        pipeline_name='2LIS_13_VDITM_billing_document_item_delta_demo_pk',
        pipeline_id=Pipeline25.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline26 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='0FI_GL_4_general_ledger_line_items_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="general_ledger_line_items"
    )

    Pipechk26 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk26",
        pipeline_name='0FI_GL_4_general_ledger_line_items_demo_pk',
        pipeline_id=Pipeline26.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline27 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_06_INV_invoice_verification_data_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="invoice_verification_data"
    )

    Pipechk27 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk27",
        pipeline_name='2LIS_06_INV_invoice_verification_data_delta_demo_pk',
        pipeline_id=Pipeline27.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline28 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_04_P_MATNR_material_production_planning_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="material_production_planning"
    )

    Pipechk28 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk28",
        pipeline_name='2LIS_04_P_MATNR_material_production_planning_delta_demo_pk',
        pipeline_id=Pipeline28.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline29 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCHDR_delivery_header_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="delivery_header"
    )

    Pipechk29 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk29",
        pipeline_name='2LIS_12_VCHDR_delivery_header_delta_demo_pk',
        pipeline_id=Pipeline29.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )

    Pipeline30 = CloudDataFusionStartPipelineOperator(
        location='europe-west1',
        pipeline_name='2LIS_12_VCITM_delivery_item_delta_demo_pk',
        instance_name="cdf-odp-looker-dev-6-4-basic",
        runtime_args={'SAPSystemNumber': '00', 'SAPLanguage': 'EN', 'SAPClient': '100',
                      'SAPApplicationServerHost': '10.132.0.114', 'Dataset': 'scmtwin_script_Demo'},
        namespace='default',
        pipeline_timeout='10 * 60',
        api_version='v1beta1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
        task_id="delivery_item"
    )

    Pipechk30 = CloudDataFusionPipelineStateSensor(
        task_id="Pipe-Chk30",
        pipeline_name='2LIS_12_VCITM_delivery_item_delta_demo_pk',
        pipeline_id=Pipeline30.output,
        expected_statuses=set(["COMPLETED"]),
        instance_name='cdf-odp-looker-dev-6-4-basic',
        location='europe-west1',
        gcp_conn_id='google_cloud_default',
        dag=dag,
    )


    Pipeline1 >> Pipechk1 >> Pipeline2 >> Pipechk2 >> Pipeline3 >> Pipechk3 >> Pipeline4 >> Pipechk4 >> run1
    Pipeline5 >> Pipechk5 >> Pipeline6 >> Pipechk6 >> Pipeline7 >> Pipechk7 >> Pipeline8 >> Pipechk8 >> Pipeline9 >> Pipechk9 >> run2
    Pipeline10 >> Pipechk10 >> Pipeline11 >> Pipechk11 >> Pipeline12 >> Pipechk12 >> Pipeline13 >> Pipechk13 >> Pipeline14 >> Pipechk14 >> run3
    #
    [run1, run2, run3] >> Pipeline15 >> Pipechk15 >> Pipeline16 >> Pipechk16 >> [run4, run5, run6]
    #
    run4 >> Pipeline17 >> Pipechk17 >> Pipeline18 >> Pipechk18 >> Pipeline19 >> Pipechk19 >> Pipeline20 >> Pipechk20 >> run7
    run5 >> Pipeline22 >> Pipechk22 >> Pipeline23 >> Pipechk23 >> Pipeline24 >> Pipechk24 >> Pipeline25 >> Pipechk25 >> run8
    run6 >> Pipeline26 >> Pipechk26 >> Pipeline27 >> Pipechk27 >> Pipeline28 >> Pipechk28 >> Pipeline29 >> Pipechk29 >> Pipeline30 >> Pipechk30 >> run9
    #
    run_this_first >> [Pipeline1, Pipeline5, Pipeline10]
    #
    [run7, run8, run9] >> run_this_last
