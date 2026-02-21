English 🇬🇧
Hello
In this project, I developed a machine learning model that classifies DNA sequences into specific gene types using natural language processing techniques.
Project Overview:
🔹 Model: Built using the Random Forest Classifier with k-mer counting for biological sequence analysis.
🔹 Objective: To predict the "Gene Type" (e.g., protein-coding, non-coding) from raw nucleotide sequences.
🔹 Dataset: DNA Sequence Dataset.
🔹 Preprocessing & Optimization:
K-mer Transformation: DNA sequences were broken down into overlapping segments (6-mers) to treat genetic data like text.
TfidfVectorizer: Applied TF-IDF with bigrams to convert k-mer sequences into numerical features, emphasizing unique biological patterns.
Label Encoding: Categorical gene types were transformed into numerical format for model compatibility.
🔹 Key Insight: Beyond basic classification, the model provides class-based probability rates, allowing for a confidence-based assessment of each genetic prediction.
Tech Stack: Python, Pandas, Scikit-learn, Seaborn, Matplotlib.
Feel free to review the code and share your feedback!
Author Mustafa Alpergün

Türkçe 🇹🇷
Merhaba 
Bu projede, DNA dizilerini doğal dil işleme tekniklerini kullanarak belirli gen türlerine göre sınıflandıran bir makine öğrenmesi modeli geliştirdim.
Proje Detayları:
🔹 Model: Biyolojik dizi analizi için k-mer yöntemi ve Random Forest Classifier (Rastgele Orman Sınıflandırıcı) algoritması kullanıldı.
🔹 Amaç: Ham nükleotid dizilerinden (NucleotideSequence) ilgili "Gen Türünü" (GeneType) tahmin etmek.
🔹 Veri Seti: DNA Sequence Dataset.
🔹 Ön İşleme ve Optimizasyon:
K-mer Dönüşümü: DNA dizileri, genetik veriyi metin gibi işleyebilmek adına 6'lı örtüşen parçalara (6-mers) bölündü.
TfidfVectorizer: K-mer dizilerini sayısal özelliklere dönüştürmek için TF-IDF ve bigram (ikili kelime grupları) yöntemleri uygulanarak biyolojik örüntüler vurgulandı.
Hata Analizi: Karmaşıklık Matrisi (Confusion Matrix) üzerinden modelin hangi sınıflarda daha başarılı olduğu görselleştirildi.
🔹 Temel Çıkarım: Model sadece sınıf tahmini yapmakla kalmayıp, her tahmin için sınıf bazlı olasılık oranları sunarak genetik analizlerde güven aralığı sağlamaktadır.
Kullanılan Teknolojiler: Python, Pandas, Scikit-learn, Seaborn, Matplotlib.
Kodları incelemek ve geliştirme önerilerinizi paylaşmak isterseniz geri bildirimleriniz benim için çok değerli! 👇
Yazar Mustafa Alpergün
