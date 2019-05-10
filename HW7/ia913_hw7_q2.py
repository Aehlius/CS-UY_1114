def clean_data(complete_weather_filename, cleaned_weather_filename):
    infile = open(complete_weather_filename, 'r')
    outfile = open(cleaned_weather_filename, 'w')
    for line in infile:
        if line != '/n':
            line = line[:-2]
            weather = line.split(',')
            if weather[8] == 'T':
                weather[8] = '0'
            outfile.write(weather[0] + "," + weather[1] + "," + weather[2] + "," + weather[3] + "," + weather[8] + "\n")
    infile.close()
    outfile.close()


def f_to_c(f_temperature):
    c_temperature=str((float(f_temperature))-32*(5/9))
    return c_temperature


def in_to_cm(inches):
    cm = str((float(inches))*2.54)
    return cm


def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    infile=open(imperial_weather_filename, 'r')
    outfile=open(metric_weather_filename, 'w')
    outfile.write("City,Date,High,Low,Precipitation\n")
    line_count = 0
    infile.readline()
    for line in infile:
        if line != '\n':
            line = line.strip("\n")
            data = line.split(",")
            outfile.write(data[0] + "," + data[1] + "," + f_to_c(data[2]) + "," + f_to_c(data[3]) + "," + in_to_cm(
                data[4]) + "\n")
        line_count += 1
    infile.close()
    outfile.close()

def print_averages_per_month(city, weather_filename, unit_type):
    high_list=[]
    low_list=[]
    for i in range(1, 13):
        infile = open(weather_filename, "r")
        high = 0
        low = 0
        count = 0
        for line in infile:
            line = line.strip("\n")
            weather = line.split(",")
            date = weather[1].split("/")
            month = date[0]
            if city == weather[0]:
                if int(month) == i:
                    high += float(weather[2])
                    low += float(weather[3])
                    count += 1
        high_list.append(round(high / count, 3))
        low_list.append(round(low / count, 3))

    if unit_type == "metric":
        unit = "C"
    else:
        unit = "F"
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print("\nAverage temperatures for "+str(city)+":\n")
    for i in range(0,12):
        print(str(month_list[i]) + ': ' + str(high_list[i]) + unit + " High, " + str(low_list[i]) + unit + " Low")
    infile.close()

def average_precipitation(weather_filename, new_filename, unit_type, city):
    outfile = open(new_filename, "w")
    precip = []
    for i in range(1, 13):
        infile = open(weather_filename, "r")
        precip_total = 0
        count = 0
        for line in infile:
            line = line.strip("\n")
            weather = line.split(",")
            date = weather[1].split("/")
            month = date[0]
            if city == weather[0]:
                if int(month) == i:
                    precip_total += float(weather[4])
                    count += 1
        precip[i] = round(precip_total / count, 4)

    if unit_type == "metric":
        unit = "cm"
    else:
        unit = "in"
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    outfile.write("Precipitation Averages for Each Month in " + str(city) + "\n")
    for i in range(0,12):
        outfile.write(str(month_list[i]) + ': ' + str(precip[i+1]) + unit + "\n")

    infile.close()
    outfile.close()