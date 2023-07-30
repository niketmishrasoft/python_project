import requests
city=input("Enter the city name:-")

appid="d3317d7bd75681f63bdb9775d2b0968d"
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}"
r=requests.get(url)

ans=r.json()
# print(ans)

respons=ans["main"]["temp"]
print("The current",city,"Temperature is🌡️",respons,"°c")