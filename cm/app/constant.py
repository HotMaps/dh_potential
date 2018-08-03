
#CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL = 'amqp://localhost/'


#CELERY_BROKER_URL = 'amqp://admin:mypass@localhost:5672/'


CM_NAME = 'District Heating Potential'

RPC_Q = 'rpc_queue_CM' # Do no change this value
CM_ID = 1
PORT = 5000 + CM_ID


INPUTS_CALCULATION_MODULE = [
    {'input_name': 'pix_threshold',
     'input_type': 'input',
     'input_parameter_name': 'pix_threshold',
     'input_value': 10,
     'input_unit': 'GWh/km2',
     'input_min': 1,
     'input_max': 100, 'cm_id': CM_ID
     },
    {'input_name': 'DH_threshold',
     'input_type': 'input',
     'input_parameter_name': 'DH_threshold',
     'input_value': 30,
     'input_unit': 'GWh/year',
     'input_min': 10,
     'input_max': 500,
     'cm_id': CM_ID
     }
]


SIGNATURE = {
    "category": "Buildings",
    "cm_name": CM_NAME,
    "layers_needed": [
        "heat_density_tot"
    ],
    "cm_url": "Do not add something",
    "cm_description": "this computation module calculates district heating potential within the selected region",
    "cm_id": CM_ID,
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE
}
