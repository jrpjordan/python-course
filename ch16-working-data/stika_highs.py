import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'data/stike_weather_07-2018.csv'
filename = 'data/stike_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # prints the headers of the data file as next function returns next line in the file when passed the reader object.
    print(header_row)
    print('\n')

    # the enumerate() function returns the item in the list and its index
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    print('\n')

    # get high temperatures from this file...
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:x
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    print(highs)
    print('\n')

    # plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # alpha parameter is transparency
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # format plot
    ax.set_title("Daily high and low temperatures, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()