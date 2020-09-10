from sklearn.tree import DecisionTreeClassifier
import requests
import pandas as pd

# This stores the url this will ask the user to enter city ID and adds to the URL
api_key = "35221e928de70d1425a6dae04b36e346"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
zip_code = input("Enter a zip code: ")
final_url = base_url + "appid=" + api_key + "&zip=" + zip_code + "&units=imperial"

# This variable contains the JSON data which the API returns
weather_data = requests.get(final_url).json()

# Weather variables for test
wind_speed = weather_data['wind']['speed']
temp = weather_data['main']['temp']
pressure = weather_data['main']['pressure']
humidity = weather_data['main']['humidity']


def main():
    # This is the data that will supervise our decision tree
    weather = pd.read_csv("WeatherData.csv", sep=",")
    X = weather.values[:, 0:2]
    Y = weather.values[:, 2:].reshape(-1, 1)

    # decision tree classifier
    temp_clf = DecisionTreeClassifier(max_depth=3)
    temp_clf.fit(X, Y)
    temp_clf.predict_proba([[temp, wind_speed]])
    print(temp_clf.predict([[temp, wind_speed]]))


if __name__ == '__main__':
    main()
