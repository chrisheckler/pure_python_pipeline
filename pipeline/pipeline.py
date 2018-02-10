#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

import json

# Stage 0
stage_0_data = dict([('Chris', 80000),('Freddie', 50000), ('Jami', 10000), ('Heckie', 1000000)])
stage_0_json = json.dumps(stage_0_data)
print("Stage 0 data: " + stage_0_json)


# Stage 1
stage_1_data = {k.lower(): v for k,v in stage_0_data.items()}
stage_1_json = json.dumps(stage_1_data)
print('Stage 1 data: '+ stage_1_json)
