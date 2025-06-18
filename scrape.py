import bs4
import requests
from datetime import datetime,timedelta
from pytz import timezone
from imd_native_api import native_json


def get_weather_info(city):
    response = requests.get("https://city.imd.gov.in/citywx/menu_test.php")

    soup = bs4.BeautifulSoup(response.text,'html.parser')

    tags = soup.find_all("a")
    seven_days = [
        datetime.now(timezone("Asia/Kolkata")).date(),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=1),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=2),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=3),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=4),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=5),
        datetime.now(timezone("Asia/Kolkata")).date() - timedelta(days=6),
    ]

    a = []


    for i in range(len(tags)):
        if city in tags[i]:
            buffer_response = requests.get(f"https://city.imd.gov.in/citywx/" + tags[i].get("href"))
            new_soup = bs4.BeautifulSoup(buffer_response.text, 'html.parser')

            print(f"https://city.imd.gov.in/citywx/{tags[i].get("href")} \n")

            table_tags = new_soup.find_all("table")

            x_data = table_tags[1].find_all("font")

            buffer_seven_day_data = table_tags[2].find_all("tr")


            seven_day_data = [
                buffer_seven_day_data[1].find_all("td"),
                buffer_seven_day_data[2].find_all("td"),
                buffer_seven_day_data[3].find_all("td"),
                buffer_seven_day_data[4].find_all("td"),
                buffer_seven_day_data[5].find_all("td"),
                buffer_seven_day_data[6].find_all("td"),
                buffer_seven_day_data[7].find_all("td"),
            ]

            imd_native_int = int(tags[i].get("href").split("=")[1])

            imd_api_res = native_json(imd_native_int)


            print("got the the data needed!🤞")

            data = {
                "today" : {
                    "city": city,
                    "day" : seven_day_data[1][0].text
                    .replace("\n", "")
                    .replace("\t", "")
                    .replace("\r", ""),
                    "max_temp" : x_data[2].text
                        .replace("\n","")
                        .replace("\t","")
                        .replace("\r",""),
                    "min_temp": x_data[6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                    "sunset_today": x_data[16].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                    "sunrise_tomorrow": x_data[18].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                    "moon_rise": x_data[22].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                    "moon_set": x_data[20].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                    "rainfall": float(imd_api_res[0]["rainfall"]) * (10 ** -2),
                    "rh0830": imd_api_res[0]["rh0830"] + " %" if imd_api_res[0]["rh0830"] is not None else "--",
                    "rh1730": imd_api_res[0]["rh1730"] + " %" if imd_api_res[0]["rh1730"] is not None else "--",
                },

                "six_day" : {
                    "city": city,
                    "day_1": {
                        "day": seven_day_data[1][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),
                        "min_temp": seven_day_data[1][1].text
                            .replace("\n","")
                            .replace("\t","")
                            .replace("\r",""),
                        "max_temp": seven_day_data[1][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast":seven_day_data[1][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[1][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                    "day_2": {
                        "day": seven_day_data[2][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "min_temp":
                            seven_day_data[2][1].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "max_temp":
                            seven_day_data[1][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast": seven_day_data[2][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[2][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                    "day_3": {
                        "day": seven_day_data[3][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "min_temp":
                            seven_day_data[3][1].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "max_temp":
                            seven_day_data[3][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast": seven_day_data[3][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[3][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                    "day_4": {
                        "day": seven_day_data[4][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "min_temp":
                            seven_day_data[4][1].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "max_temp":
                            seven_day_data[4][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast": seven_day_data[4][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[4][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                    "day_5": {
                        "day":seven_day_data[5][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "min_temp":
                            seven_day_data[5][1].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "max_temp":
                            seven_day_data[5][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast": seven_day_data[5][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[4][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                    "day_6": {
                        "day": seven_day_data[6][0].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "min_temp":
                            seven_day_data[6][1].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "max_temp":
                            seven_day_data[6][2].text
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("\r", "")
                        ,
                        "forecast": seven_day_data[6][4].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                        "warnings": seven_day_data[6][6].text
                        .replace("\n", "")
                        .replace("\t", "")
                        .replace("\r", ""),

                    },
                }
            }

            print("response 👍 \n")
            return data



if __name__ == "__main__":
    print(get_weather_info("Faridabad"))
