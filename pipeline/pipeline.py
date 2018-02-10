#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

import json

# Stage 0 - Create data
stage_0_data = dict([('Chris', 80000),('Freddie', 50000), ('Jami', 10000), ('Heckie', 1000000)])
stage_0_json = json.dumps(stage_0_data)
print("Stage 0 data: " + stage_0_json)
print('Stage 0 objective: Create data' + '\n')


# Stage 1 - Transform keys to lowercase
stage_1_data = {k.lower(): v for k,v in stage_0_data.items()}
stage_1_json = json.dumps(stage_1_data)
print('Stage 1 data: '+ stage_1_json)
print('Stage 1 objectives: Keys are transformed to lowercase'+ '\n')


# Stage 2 - Multiply values by 12
stage_2_data = {k: v*12 for k,v in stage_1_data.items()}
stage_2_json = json.dumps(stage_2_data)
print('Stage 2 data: '+ stage_2_json)
print('Stage 2 objectives: values are multiplied by 12'+ '\n')


# Stage 3 - Summary statistics for values
stage_3_data = {}

