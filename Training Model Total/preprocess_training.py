import pandas as pd
import config
from dateutil import parser

data = pd.read_excel("R33 - Wed Feb 19 2020 00_00_00 GMT+0700 (Western Indonesia Time) - Fri Feb 28 2020 23_30_00 GMT+0700 (Western Indonesia Time).xlsx")
#print(data['indoor_time'][1])
#Cek kelengkapan data, kalau ada yang kosong, buang baris itu
#data_filtered = data[data['indoor_time'].notna()]

#Ambil sensor indoor yang ada nilainya aja
indoor_sensor = ["indoor_field%i" %a for a in range(1,13)]

#Buang kolom yang kosong semua
data.dropna(how='all', axis='columns', inplace=True)

#Buang baris untuk data yang ga lengkap
data.dropna(how='any', axis='rows', inplace=True)

data=data.reset_index(drop=True)
#print(indoor_sensor)
#print(data)
#print(list(data_filtered))

#Untuk filter : kelamin, asal, ac, sama koefisien pakaian
#Kelamin
print(data["kelamin"])
data["kelamin"]=[config.KELAMIN[str(i)] for i in data["kelamin"]]

#AC
data["ac"]= [config.AC[str(j)] for j in data["ac"]]


#Konstanta termal
LAKI_LAKI = config.CLO['laki-laki']
PEREMPUAN_TANPAJILBAB = config.CLO['perempuan_tanpajilbab']
PEREMPUAN_BERJILBAB = config.CLO['perempuan_berjilbab']

KONSTANTA_TERMAL = 0

datetime = data['waktu']  # clo berdasar hari
no_hari = [int(parser.parse(k).strftime("%w")) for k in datetime]
#print(no_hari)



data["konstanta_termal"] = [LAKI_LAKI[no_hari[idx]] if kel==1 else PEREMPUAN_BERJILBAB[no_hari[idx]] if data["jilbab"][idx]=='ya' else PEREMPUAN_TANPAJILBAB[no_hari[idx]] for idx,kel in enumerate(data["kelamin"])]

print(data["konstanta_termal"])
print(data)
#daerah


