"""
MODULO A
    Description: main module, run other modules

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

import os
# Library for logging
# log levels: debug(lowest), info, warning, error, critical(highest)
import logging
import datetime
# import for sending mail ok
from A_Email_ok import enviar_mail_ok

# Get actual date and hour
start_time = datetime.datetime.now()
day = start_time.day
month = start_time.month
year = start_time.year
hour = start_time.hour
minute = start_time.minute
second = start_time.second

today = str(day)+str(month)+str(year)
hour_aux = str(hour)+':'+str(minute)+':'+str(second)
# folder direction
direction = os.path.dirname(os.path.abspath(__file__))+'/'
# image saving direction
direction_save = os.path.dirname(os.path.abspath(__file__))+'/'

# private key direction
file_keyP8 = ''

logging.basicConfig(filename= direction + 'FondoDePantalla.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.debug)
logging.debug('Start of program')

# Log for the execution
log_name = direction + 'Logs/Registro_' + str(today) + '.log'
# Log the beginning
log_file = open(log_name, 'a')
log_file.write('-------------------------------------\n')
log_file.write('Script FondoDePantalla\n')
log_file.write('Comienzo\t'+ str(hour_aux)+'\n')
log_file.close()
# Print to save the log
print('-------------------------------------')
print('Script - FondoDePantalla')
print('Comienzo\t'+ str(hour_aux))

from B_Snow import b_snow
(amount,days,amount_day) = b_snow(direction,log_name,file_keyP8)

from C_Image import c_image
c_image(direction,log_name,amount,days,amount_day,start_time,direction_save)

# Get date and hour for the end
start_time = datetime.datetime.now()
hour_aux = start_time.hour
minute = start_time.minute
second = start_time.second

hour = str(hour_aux)+':'+str(minute)+':'+str(second)
print('Fin\t\t\t'+ str(hour))
print('-------------------------------------')
# Registro el final
log_file = open(log_name, 'a')
log_file.write('Fin\t\t\t'+ str(hour)+'\n')
log_file.write('-------------------------------------\n')
log_file.close()

logging.debug('End of program')

# Notificacion
#enviar_mail_ok(log_name)
