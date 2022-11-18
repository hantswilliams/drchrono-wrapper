import os
cwd = os.getcwd()
os.chdir(cwd + '/src')

import drchrono as drc
from dotenv import load_dotenv
load_dotenv()

#############################################

### Create fake datasets 
f_users, f_doctors, f_patients, f_appointments = drc.FAKER.generate(20, 40, 150, 500)

