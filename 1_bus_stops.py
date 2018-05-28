# encoding=UTF-8

# Остановки
# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.

import csv
import operator

if __name__ == '__main__':
    with open('input/data-398-2018-05-25.csv', 'r', encoding = 'cp1251') as csv_file:
        fields = ['ID','Name','Longitude_WGS84','Latitude_WGS84','Street','AdmArea','District','RouteNumbers','StationName','Direction','Pavilion','OperatingOrgName','EntryState','global_id','geoData',]
        reader = csv.DictReader(csv_file, fields, delimiter=';')
        bus_stops_cnt_cur = 0
        bus_stops_cnt_max = 0
        stop_max_stops = ''

        dict_distinct_stops = {}



        # print(row['Name'].encode('cp1251').decode('cp866'))

        for rownum, row in enumerate(reader):
            stop_count = dict_distinct_stops.get(row['Street'])
            if stop_count != None:
                dict_distinct_stops{row['Street']} = stop_count + 1
            else:
                dict_distinct_stops{row['Street']}

            if rownum >= 10:
                break
