import pandas as pd
import config
from dateutil import parser
import json



# Cek kelengkapan data, kalau ada yang kosong, buang baris itu

def filterNone(data):
    # Buang kolom yang kosong semua
    data.dropna(how='all', axis='columns', inplace=True)

    # Buang baris untuk data yang ga lengkap
    data.dropna(how='any', axis='rows', inplace=True)

    data = data.reset_index(drop=True)
    return data

def filterPreProcess(data):
    # Untuk filter : kelamin, asal, ac, sama koefisien pakaian
    # Kelamin

    data["kelamin"] = [config.KELAMIN[str(i)] for i in data["kelamin"]]

    # AC
    data["ac"] = [config.AC[str(j)] for j in data["ac"]]

    # Konstanta termal
    LAKI_LAKI = config.CLO['laki-laki']
    PEREMPUAN_TANPAJILBAB = config.CLO['perempuan_tanpajilbab']
    PEREMPUAN_BERJILBAB = config.CLO['perempuan_berjilbab']

    datetime = data['waktu']  # clo berdasar hari
    no_hari = [int(parser.parse(k).strftime("%w")) for k in datetime]
    # print(no_hari)

    data["konstanta_termal"] = [
        LAKI_LAKI[no_hari[idx]] if kel == 1 else PEREMPUAN_BERJILBAB[no_hari[idx]] if data["jilbab"][idx] == 'ya' else
        PEREMPUAN_TANPAJILBAB[no_hari[idx]] for idx, kel in enumerate(data["kelamin"])]

    # Daerah
    # Encode untuk daerah asal, udah ada data dari daerah.json, antara sejuk atau hangat
    # 0 - untuk sejuk
    # 1 - untuk hangat
    # ini masih belom pake data kecamatan terbaru, soalnya inputnya belom format kecamatan jogja.
    asal = data["asal"]
    data["asal"] = [0 if c in data_asal["sejuk"] else 1 for c in asal]
    print("Done!")
    return data

data_asal = json.loads("".join(open('assets/daerah.json').readlines()))
#path="assets/R33 - Wed Feb 19 2020 00_00_00 GMT+0700 (Western Indonesia Time) - Fri Feb 28 2020 23_30_00 GMT+0700 (Western Indonesia Time).xlsx"

data=readdata(path)
data=filterNone(data)
data=filterPreProcess(data)

print(data)