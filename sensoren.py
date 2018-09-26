import csv
import random
import time
from datetime import datetime



# Aantal records
RECORD_COUNT = 10000

# Minimaal 1 use case
# Ruis voor de testdata x
#

def randomdate(start, end):
    format = '%d-%m-%Y %H:%M'
    starttime  = time.mktime(time.strptime(start, format))
    endtime = time.mktime(time.strptime(end, format))
    ptime = starttime + random.random() * (endtime - starttime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return dt



def Sensor_data():








def Sensor_data_Echt(sensor, start, end):
    sensor = input('kies een van de juiste sensoren')
    start = int(input('geef een startdatum %d-%m-%Y %H:%M'))
    end = int(input('Geef een einddatum %d-%m-%Y %H:%M'))
    with open('C:/Users/Dennis Pieruschka/Dropbox/BM01 - Artificial Intelligence/Casus/Source_Code/Testdata/Sensoren/Sensoren_Indicatoren/timeseries.csv', 'w', newline='') as csvfile:
        # Indicatoren
        Sensoren = ['Bewegingsmelder', 'Infraroodmelder', ]
        Ruimtes = ['Slaapkamer', 'Toilet', 'Eetkamer', 'Keuken']


        # Velden
        fieldnames = ['Timestamp', 'Sensor', 'Ruimte', 'Value']

        # writer functie
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

    def Write():
        for i in range(RECORD_COUNT):
            writer.writerow(
            {
                'Timestamp': randomdate(start, end),
                'Sensor': random.choice(Sensoren),
                'Ruimte': random.choice(Ruimtes),
                'Value': 1
            }
        )



    



def Sensor_data_ruis():
    with open('C:/Users/Dennis Pieruschka/Dropbox/BM01 - Artificial Intelligence/Casus/Source_Code/Testdata/Sensoren/Sensoren_Indicatoren/timeseries.csv', 'w', newline='') as csvfile:
        # Indicatoren
        Sensoren = ['Bewegingsmelder', 'Infraroodmelder', ]
        Ruimtes = ['Slaapkamer', 'Toilet', 'Eetkamer', 'Keuken']


        # Velden
        fieldnames = ['Timestamp', 'Sensor', 'Ruimte', 'Value']

        # writer functie
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
            {
                'Timestamp': randomdate('1-10-2018 9:00', '30-10-2018 22:00'),
                'Sensor': random.choice(Sensoren),
                'Ruimte': random.choice(Ruimtes),
                'Value': 1
            }
        )


if __name__ == '__main__':
    Sensor_data_ruis()
    aantal_zaken = hoeveel
