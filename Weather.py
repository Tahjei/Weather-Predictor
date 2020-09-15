from sklearn.tree import DecisionTreeClassifier
import requests
import pandas as pd
import csv

# This stores the url this will ask the user to enter city ID and adds to the URL
api_key = "35221e928de70d1425a6dae04b36e346"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
zip_code = input("Enter a zip code: ")
final_url = base_url + "appid=" + api_key + "&zip=" + zip_code + "&units=imperial"

# This variable contains the JSON data which the API returns
weather_data = requests.get(final_url).json()

# Weather variables for testing, wind_speed and temp are the only active ones currently
wind_speed = weather_data['wind']['speed']
temp = weather_data['main']['temp']
pressure = weather_data['main']['pressure']
humidity = weather_data['main']['humidity']


class Prediction:

    def __init__(self, temp, wind_speed):
        self.temp = temp
        self.wind_speed = wind_speed

        # This is the data that will supervise our decision tree
        weather = pd.read_csv("WeatherData.csv", sep=",")
        x = weather.values[:, 0:2]
        y = weather.values[:, 2:].reshape(-1, 1)

        # decision tree classifier
        self.temp_clf = DecisionTreeClassifier(max_depth=3)
        self.temp_clf.fit(x, y)
        self.temp_clf.predict_proba([[temp, wind_speed]])
        print(self.temp_clf.predict([[temp, wind_speed]]))

# This function is meant to update the decision tree based on what the user prefers.
# It needs to be redone. Right now it throws an error
    def predict(self, temp, wind_speed):
        # This is the data that will supervise our decision tree
        weather = pd.read_csv("WeatherData.csv", sep=",")
        x = weather.values[:, 0:2]
        y = weather.values[:, 2:].reshape(-1, 1)

        # decision tree classifier
        self.temp_clf = DecisionTreeClassifier(max_depth=3)
        self.temp_clf.fit(x, y)
        self.temp_clf.predict_proba([[temp, wind_speed]])
        print(self.temp_clf.predict([[temp, wind_speed]]))
        predict = self.temp.predict([[temp, wind_speed]])
        return predict

# The optimization function allows users to comment on how the program did when guessing
# It then saves a new updated guess that is added to a new file to update the decision tree
    def optimization(self):
        rec = input("Was the recommendation good? Y/N ")

# Creates a new file called 'newData' to hold the updated recommendations
        with open('newData.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            if (rec.lower() == 'yes') or (rec.lower() == 'y'):
                # This line writes the 'temperature', 'wind speed', and 'the clothing recommendation' to the new file
                filewriter.writerow([self.temp, wind_speed, self.temp_clf.predict([[self.temp, wind_speed]])])
                filewriter.writerow("\n")
            elif (rec.lower() == 'no') or (rec.lower() == 'n'):
                change = input("Was the weather too hot or too cold? H/C ")
                if (change.lower() == 'hot') or (change.lower() == 'h'):
                    # The temp += 10 is meant to increase the bracket for the recommendation
                    # however in the current form it only changes what temp is written to the file
                    # the actual recommendation stays the same
                    self.temp += 10
                    filewriter.writerow([self.temp, wind_speed, self.temp_clf.predict([[self.temp, wind_speed]])])
                    filewriter.writerow("\n")
                elif (change.lower() == 'cold') or (change.lower() == 'c'):
                    filewriter.writerow([self.temp, wind_speed, self.temp_clf.predict([[self.temp, wind_speed]])])
                    filewriter.writerow("\n")
            else:
                print("Have A Nice Day!")


t = Prediction(temp, wind_speed)
t.optimization()
