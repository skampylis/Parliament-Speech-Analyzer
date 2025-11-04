# **ParliamentSpeechAnalyzer**

## **Description**

A **Python/Flask** program that implements a search and analysis system for 1.28 million speeches from the **Hellenic Parliament (1989–2020)**. It integrates **Information Retrieval** techniques such as **TF-IDF**, **Latent Semantic Indexing (LSI)**, and **Apriori**, enabling thematic categorization, keyword extraction, similarity detection among MPs, and association rule mining. It provides an interactive **Web application** with search, filtering, and **data visualization** capabilities.

---

### **🚀 Project Overview**

* **Information Retrieval**: Thematic extraction and search across the corpus of parliamentary speeches.
* **Visualization & Analysis**: Exploration of relationships, temporal trends, and concepts using charts and metrics.
* **Vector Representation**: Comparison of MPs based on semantic similarity (LSI).

---

### **🔍 Key Features**

* **TF-IDF & LSI**: Identification of key terms per MP or party and thematic grouping of speeches.
* **Apriori Algorithm**: Extraction of association rules among terms in large text corpora.
* **Search & Filter UI**: Interactive search and filtering by speaker, party, and keyword.
* **Temporal Analysis**: Visualization of the evolution of words or topics over time.

---

### **🛠️ Technical Highlights**

* **Python & Flask**: Backend server for data communication and processing.
* **HTML/CSS/JavaScript**: Responsive frontend UI with search and filtering capabilities.
* **Pandas & Scikit-Learn**: Data preprocessing and implementation of IR models.
* **Matplotlib/Seaborn/WordCloud**: Visualization of data and keyword distributions.

---

### **📂 Code Structure**

* **app.py**: Main Flask application – runs the server and serves endpoints.
* **initialize.py**: Data preparation and loading (stemming, filtering, vectorization).
* **templates/**: HTML files for the frontend.
* **static/**: CSS/JS for the user interface.
* **models/**: Implementation of LSI, TF-IDF, and Apriori models.
* **data/**: Sample dataset (CSV) for local testing.

---

## **📦 Installation**

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## **▶️ Run**

Start the Flask app:

```bash
python app.py
```

Open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **⚠️ Important Note**

To run the application correctly, modify the CSV path in `initialize.py`:

```python
Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')
```

The full dataset **Greek_Parliament_Proceedings_1989_2020.csv** is not available on GitHub due to size limitations. You can download it from:
[https://github.com/iMEdD-Lab/Greek_Parliament_Proceedings](https://github.com/iMEdD-Lab/Greek_Parliament_Proceedings)

---

**🏷️ Tags**: **Python**, **Flask**, **Information Retrieval**, **TF-IDF**, **LSI**, **Apriori**, **Data Visualization**, **NLP**, **Greek Parliament**, **Text Mining**
**🌟 Concept**: *"A tool for information retrieval and analysis of the proceedings of the Hellenic Parliament, utilizing modern IR techniques for thematic extraction, MP comparison, and keyword visualization over time."*
