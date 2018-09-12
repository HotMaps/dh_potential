
CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'

CELERY_BROKER_URL = CELERY_BROKER_URL_LOCAL
#CELERY_BROKER_URL = 'amqp://admin:mypass@localhost:5672/'
CM_REGISTER_Q = 'rpc_queue_CM_register'
CM_NAME = 'District Heating Potential'
RPC_CM_ALIVE= 'rpc_queue_CM_ALIVE'
RPC_Q = 'rpc_queue_CM_compute' # Do no change this value
CM_ID = 2
PORT = 5002
TRANFER_PROTOCOLE ='http://'

INPUTS_CALCULATION_MODULE = [
    {'input_name': 'Min. heat demand in hectare',
     'input_type': 'input',
     'input_parameter_name': 'pix_threshold',
     'input_value': 10,
     'input_unit': 'GWh/km2',
     'input_min': 1,
     'input_max': 100,
     'cm_id': CM_ID
     },
    {'input_name': 'Min. heat demand in a DH area',
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
        "heat_tot_curr_density",
    ],
    "cm_url": "Do not add something",
    "cm_description": "This computation module calculates district heating potential within the selected region",
    "cm_id": CM_ID,
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE
}
