import pandas as pd
import numpy as np

data = {
    "nama": ["Andi", "Budi", "Cici", "Dedi", "Eka"],
    "nilai_uts": [75, 82, 90, 65, 78],
    "nilai_uas": [80, 85, 88, 70, 92],
    "kehadiran": [90, 85, 95, 70, 80]  # dalam persen
}

df=pd.DataFrame(data)
# Menambahkan kolom nilai_akhir dengan perhitungan sederhana
df["nilai_akhir"] = (df["nilai_uts"] * 0.3) + (df["nilai_uas"] * 0.5) + (df["kehadiran"] * 0.2)         
df["lulus"] = df["nilai_akhir"] >= 75
print(df)   

#filtering data
lulus_df = df[df["lulus"] == True]
kehadiran_bagus=df[df['kehadiran'] >=85]
print(lulus_df)
print(kehadiran_bagus)

#sorting data
df_sorted = df.sort_values(by="nama", ascending=True)
print(df_sorted)

#grouping data
grouped = df.groupby("lulus")["nilai_akhir"].mean()
print(f'grouped = {grouped}')

df["jurusan"] = ["TI", "TI", "SI", "SI", "TI"]
rata_jurusan = df.groupby("jurusan")["nilai_akhir"].mean()
print(f'rata_jurusan = {rata_jurusan}')

#statistics
print(f'stat = {df["nilai_akhir"].describe()}')
print(df.isnull().sum())
print(df)
dfDenganNull = df.copy()
dfDenganNull.loc[2, "nilai_uts"] = np.nan
print(f'satu = {dfDenganNull}')
print(dfDenganNull.isnull().sum())
dfDenganNull["nilai_uts"] = dfDenganNull["nilai_uts"].fillna(dfDenganNull["nilai_uts"].mean())
print(dfDenganNull)