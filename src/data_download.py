#!/usr/bin/env python

# Autores:
#  Edgar Perez Blanco
#  Bartomeu Perello Comas

import urllib.request
import os

os.mkdir("dataset")

# Download File
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
urllib.request.urlretrieve(url, './dataset/automobile.csv')

# Read File
f = open("./dataset/automobile.csv", 'r')
file_source = f.read()

# Replace '-' by '_'
final_file = file_source.replace('alfa-romero', 'alfa_romero').replace('mercedes-benz', 'mercedes_benz')

# Add data headers
header = "symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,price\n"
final_file = header + final_file

# Write File
w = open("./dataset/automobile.csv", 'w')
w.write(final_file)
