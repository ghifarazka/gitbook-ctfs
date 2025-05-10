# Falling Fell (500 pts)

> ![](broken-reference)OpenStreetMap is a great resource for understanding natural features of a landscape, like fells, heaths, and woodlands. There are a number of natural features tagged as ‘fell’ on OpenStreetMap in Norway.
>
> A selection of these fells have extra tags and information, including names – there’s a small group of them relatively close together. What is the name of the **southernmost** of these fells? _Answer is one word, lowercase i.e. oslo_

### Solution

To solve this challenge, I used [OverpassTurbo](https://overpass-turbo.eu/). Following the description, I ran the code attached below. It searches for instances of "fell" in Norway that has an attribute called "name".

```sql
[out:json];

// Limit search to Norway (Norge)
area["name"="Norge"]->.searchArea;
(
  node["natural"="fell"](area.searchArea)["name"];
  way["natural"="fell"](area.searchArea)["name"];
  relation["natural"="fell"](area.searchArea)["name"];
);

// Print results
out body;
>;
out skel qt;
```

<figure><img src="../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

The result notably shows two groups of nodes seemingly packed together. One is more north and the other one is more south. If we zoom in on each, it becomes clear that the group on the south is more closely packed together. Additionally, they have more complete information (just as the challenge described).

| North group                                                                                                     | South group                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| <div><figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure></div> | <div><figure><img src="../../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure></div> |

Now, we just need to click on the southernmost node and take a look at its name.

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

Flag: `kubbekleiv`
