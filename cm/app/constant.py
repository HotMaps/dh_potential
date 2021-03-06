
CELERY_BROKER_URL_DOCKER = 'amqp://admin:mypass@rabbit:5672/'
CELERY_BROKER_URL_LOCAL = 'amqp://localhost/'



CM_REGISTER_Q = 'rpc_queue_CM_register' # Do no change this value
CM_NAME = 'CM - District heating potential areas: user-defined thresholds'
RPC_CM_ALIVE= 'rpc_queue_CM_ALIVE' # Do no change this value
RPC_Q = 'rpc_queue_CM_compute' # Do no change this value
CM_ID = 2
PORT_LOCAL = int('500' + str(CM_ID))
PORT_DOCKER = 80
#TODO ********************setup this URL depending on which version you are running***************************

CELERY_BROKER_URL = CELERY_BROKER_URL_DOCKER
PORT = PORT_DOCKER

#TODO ********************setup this URL depending on which version you are running***************************

TRANFER_PROTOCOLE ='http://'

#TODO ********************setup this URL depending on which version you are running***************************

TRANFER_PROTOCOLE ='http://'
INPUTS_CALCULATION_MODULE = [
    {'input_name': 'Min. heat demand in hectare',
     'input_type': 'input',
     'input_parameter_name': 'pix_threshold',
     'input_value': 333,
     'input_unit': 'MWh/(ha*yr)',
     'input_min': 0.1,
     'input_max': 10000000,
     'cm_id': CM_ID
     },
    {'input_name': 'Min. heat demand in a DH area',
     'input_type': 'input',
     'input_parameter_name': 'DH_threshold',
     'input_value': 30,
     'input_unit': 'GWh/yr',
     'input_min': 0.1,
     'input_max': 10000000,
     'cm_id': CM_ID
     }
]


SIGNATURE = {

    "category": "Demand",
    "authorized_scale":["NUTS 0", "NUTS 1", "NUTS 2", "NUTS 3", "LAU 2", "Hectare"],
    "cm_name": CM_NAME,
    "layers_needed": [
        "heat_tot_curr_density_tif",
    ],
    "type_layer_needed": [
        {"type": "heat", "description": "Select heat demand density layer."},
    ],
    "cm_url": "Do not add something",
    "cm_description": "This calculation module calculates district heating " \
    "potential within the selected region. As output, a layer for the " \
    "potential areas are shown. Click on the regions to get their " \
    "corresponding potential. Within the indicator/graph window, relevant " \
    "indicators and charts regarding DH potential within the selected zone " \
    "and potentials in sub-zones are illustrated.",
    "cm_id": CM_ID,
    "wiki_url":"https://wiki.hotmaps.eu/en/CM-District-heating-potential-areas-user-defined-thresholds",
    'inputs_calculation_module': INPUTS_CALCULATION_MODULE
}
