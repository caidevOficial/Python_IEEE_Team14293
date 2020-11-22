import pandas as pd 
import random as n 

data = {
    "usuario": ["pato","nato","gatp"],
    "password": ["abc123","abs234","abc345"],
    "random" : []
}

for i in range(3):
    data["random"].append(n.randint(1,30))

# Dict normal
print(data)

# Dict visto en dataFrame
df = pd.DataFrame(data)
print(df)