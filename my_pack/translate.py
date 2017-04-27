# -- coding: utf-8 --
import csv
import json


def translate_csv(path):
    input_file = open(path, 'r')
    lines = input_file.readlines()
    input_file.close()
    path_out = path.replace(".txt", ".csv")
    out_file = open(path_out, "w", newline='')
    writer = csv.writer(out_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    tmp = []
    for line in lines:
        linelist = line.split()
        tmp.append(linelist)
    writer.writerows(tmp)
    out_file.close()


def translate_json(path):
    in_file = open(path, 'r')
    lines = in_file.readlines()
    in_file.close()
    path_out = path.replace(".txt", ".json")
    out_file = open(path_out, "w", newline='')
    tmp = []
    for line in lines:
        linelist = line.split()
        tmp.append(linelist)
    json_var = json.dumps(tmp)
    out_file.write(json_var)
    out_file.close()


def translate_csv_json(path):
    reader = csv.reader(open(path, 'r'))
    json_var = json.dumps(list(reader))
    path_out = path.replace(".csv", ".json")
    out_file = open(path_out, 'w')
    out_file.write(json_var)
    out_file.close()


def translate_json_csv(path):
    in_file = open(path, 'r')
    reader = in_file.read()
    in_file.close()
    out = json.loads(reader)
    path_out = path.replace(".json", ".csv")
    out_file = open(path_out, "w", newline='')
    writer = csv.writer(out_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(out)
    out_file.close()

