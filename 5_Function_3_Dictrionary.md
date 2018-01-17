# Dictionary
- like the map in c++...
- dictionary DO NOT have sequence

```
dic = { key_a : val_a,
        key_b : val_b,
}
```
where key_a/b and val_a/b can be any type, like int,float and string 

In order to add element of dictionary, you can directly add with 
```
dic[key_c] = val_c;
```

Many data on the website is store with dictionary, we can download them and transfer to python dictionary with some APIs.
e.g.
```
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())
```

