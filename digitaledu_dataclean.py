import pandas as pd 

# Paso 1. Cargar y limpiar los datos
df = pd.read_csv('data/digitaledu.csv')
df.info()

df.drop(["id","bdate", "has_photo", "relation", "career_start", "career_end", "graduation", "has_mobile","followers_count","education_form","occupation_name", "life_main","people_main", "last_seen","city"], axis=1, inplace= True)

def count_langs(row):
    return 1 if len(row.split(";")) > 1 else 0 

def is_student(row):
    return 1 if "student" in row else 0


df["is_polyglot"]= df["langs"].apply(lambda x: 1 if len(x.split(";")) > 1 else 0)
df.drop(["langs"],axis=1, inplace= True)

df["sex"]= df["sex"].apply(lambda x: 1 if x == 2 else 0)
df["is_student"] = df["education_status"].apply(lambda x: 1 if "student" in x else 0)
df = pd.get_dummies(df, columns=["occupation_type"], prefix="occ", dtype=int, dummy_na=True)

df.drop(["education_status"], axis=1, inplace=True)

print("-"*40)
print("\nRESULTADOS")

df.info()
# Exportando para usar el csv limpio
df.to_csv("cleaned/digitaledu_cleaned.csv")