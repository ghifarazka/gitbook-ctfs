# Day 13 - Planespotting

<figure><img src="../../../.gitbook/assets/Airplane.png" alt="" width="375"><figcaption></figcaption></figure>

Question: Which warmer destination is the plane heading for?

### Solution

Looking at the airplane's tail, we can observe the letters "Jt". With some Googling, we can determine that the plane belongs to an airline called "Jettime".

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

We previously know that The Thief left from Oulu airport. From that airport, what are the possible destinations if you fly with Jettime? To answer this question, we can use [FlightRadar24](https://www.flightradar24.com/). Go to the website, search for "Jettime" and then click on "Show fleet". After that, click on "Routes".

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Now, the routes shown above is different from what would have been shown during the challenge day (I'm writing this write-up way after the challenge day). This is because FlightRadar24 only shows you the routes for 7 upcoming days, and currently, it seems that there's no route coming from Oulu airport.&#x20;

Regardless, on the challenge day, you're supposed to see a route from Oulu airport to the islands west of Morocco (also visible in the above image), more specifically the Gran Canaria island. And that would be the only route. The only possible flight that The Thief could've taken using Jettime during that time is from Oulu, Finland to Gran Canaria, Canary Islands, Spain.

Flag: `Gran Canaria`
