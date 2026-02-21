import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# 1. Dosya Yolları
yollar = {
    'train': r"C:\Users\muham\Downloads\archive (14)\train.csv",
    'test': r"C:\Users\muham\Downloads\archive (14)\test.csv",
    'val': r"C:\Users\muham\Downloads\archive (14)\validation.csv"
}

try:
    df_train = pd.read_csv(yollar['train'])
    df_val = pd.read_csv(yollar['val'])
    
    df_train.columns = df_train.columns.str.strip()
    df_val.columns = df_val.columns.str.strip()
    
    dna_sutun = 'NucleotideSequence'
    hedef_sutun = 'GeneType'
except Exception as e:
    print(f"Veri yükleme hatası: {e}")

# K-mer fonksiyonu
def get_kmers(sequence, size=6):
    sequence = str(sequence).replace('<', '').replace('>', '').lower()
    return [sequence[x:x+size] for x in range(len(sequence) - size + 1)]

# 2. Ön İşleme
df_train['kelimeler'] = df_train[dna_sutun].apply(lambda x: ' '.join(get_kmers(x)))
df_val['kelimeler'] = df_val[dna_sutun].apply(lambda x: ' '.join(get_kmers(x)))

# 3. Vektörizasyon
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=10000) 
X_train = vectorizer.fit_transform(df_train['kelimeler'])
X_val = vectorizer.transform(df_val['kelimeler'])

le = LabelEncoder()
y_train = le.fit_transform(df_train[hedef_sutun])
y_val = le.transform(df_val[hedef_sutun])

# 4. Eğitim
model = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

# 5. Sonuçlar
y_pred = model.predict(X_val)
print(f"\nRandom Forest Doğruluk Oranı (Accuracy): {accuracy_score(y_val, y_pred)}")

# Görselleştirme
cm = confusion_matrix(y_val, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title('Random Forest Hata Analizi Matrisi')
plt.show()

# 6. Tahmin Denemesi ve Olasılıklar (İstediğin Bölüm)
yeni_dna = "AGCTTAGCACAGTGGCAGTATCATAGGCAGTGAGGTTTATCCGAGGCGTGATTATTGCCA"
yeni_kelimeler = ' '.join(get_kmers(yeni_dna))
yeni_vektor = vectorizer.transform([yeni_kelimeler])



tahmin = le.inverse_transform(model.predict(yeni_vektor))[0]
olasiliklar = model.predict_proba(yeni_vektor)[0]

print(f"\nTest DNA Tahmini: {tahmin}")
print("-" * 30)
print("Sınıf Bazlı Olasılık Oranları:")
for i, sinif in enumerate(le.classes_):
    print(f"{sinif}: %{olasiliklar[i] * 100:.2f}")