---
layout: default
title: Searching map keys and values
parent: Medium
grand_parent: Guides
---

# Searching map keys and values

The main data structure in OpenAF is, of course, javascript maps. We already cover how to easily search on arrays using [$from](https://openafs.blogspot.com/2019/07/making-it-easy-to-read-with-from.html). But what about maps?

Let's take an example:

````javascript
> var weather = { woeid: 742676, latt_long: "38.725670,-9.150370", parent: { latt_long: "39.557919,-7.844810" }, sun_rise: "2019-08-27T07:00:52.671773+01:00", sun_set: "2019-08-27T20:14:52.385796+01:00", consolidated_weather: [{ min_temp: 17.98, max_temp: 23.674999999999997, the_temp: 24.23 }, { min_temp: 17.405, max_temp: 23.05, the_temp: 23.39 }] };
````

The `weather` variable is a fixed sample with nested maps and an array of two forecasts.

## Searching keys

If you know the exact path it's easy to build the map "path" to get the values that you want but the OpenAF function _searchKeys_ will actually help you find those paths. Let's try to find those sun rise and sun set entries:

````javascript
> searchKeys(weather, "sun")
{
  ".sun_rise": "2019-08-27T07:00:52.671773+01:00",
  ".sun_set": "2019-08-27T20:14:52.385796+01:00"
}
````

The string search parameter (e.g. sun) is actually a case insensitive regular expression. And it just found you all map entries with the word "sun" anywhere. Now you know that _weather.sun_rise_ and _weather.sun_set_ will get you the info you need. Let's try to find now temperatures:

````javascript
> searchKeys(weather, "temp")
{
  ".consolidated_weather[0].min_temp": 17.98,
  ".consolidated_weather[0].max_temp": 23.674999999999997,
  ".consolidated_weather[0].the_temp": 24.23,
  ".consolidated_weather[1].min_temp": 17.405,
  ".consolidated_weather[1].max_temp": 23.05,
  ".consolidated_weather[1].the_temp": 23.39
}
````

Now the temperatures are found within the _consolidate_weather_ array. So you now have a list of all the paths to get the temperatures even within an array.

## Searching values

Searching keys of a map wouldn't be complete without being able to search for values. The sample contains the location code `742676`. Let's search for that:

````javascript
> searchValues(weather, "742676")
{
  ".woeid": 742676
}
````

As expected the result is the path on where that value was found. Let's now use a regular expression to try to find if there are any lat/log coordinates:

````javascript
> searchValues(weather, "-?\\d+\\.\\d+,-?\\d+\\.\\d+");
{
  ".parent.latt_long": "39.557919,-7.844810",
  ".latt_long": "38.725670,-9.150370"
}
````

## Other advanced uses

Where these two functions _searchKeys_ and _searchValues_ really shine when you are using the openaf-console to investigate a big and/or complex javascript map. They will quickly filter and find you the data that you need to help you write your scripts.

The previous examples show you the basic use of these functions. There are other options (check, in the openaf-console, "help searchKeys" and "help searchValues") to make the search case sensitive and even to execute a callback function whenever keys or values are found (for example: search & replace).
