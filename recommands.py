import pandas as pd

data = {
    'Movie':['Inception','Titanic','Avengers','Interstellar','Notebook'],
    'Genre':['Sci-Fi','Romance','Action','Sci-Fi','Romance']
}

df = pd.DataFrame(data)

choice = input("Enter genre (Sci-Fi / Action / Romance): ")

result = df[df['Genre'] == choice]

print("Recommended movies:")
print(result['Movie'])
