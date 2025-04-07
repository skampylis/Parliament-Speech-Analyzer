# **ParliamentSpeechAnalyzer**

## **Περιγραφή**
Πρόγραμμα σε **Python/Flask** που υλοποιεί ένα σύστημα αναζήτησης και ανάλυσης 1.28 εκατομμυρίων ομιλιών από το **Ελληνικό Κοινοβούλιο (1989–2020)**. Περιλαμβάνει τεχνικές **Information Retrieval** όπως **TF-IDF**, **Latent Semantic Indexing (LSI)** και **Apriori**, επιτρέποντας θεματική κατηγοριοποίηση, εξαγωγή λέξεων-κλειδιών, ανίχνευση ομοιοτήτων μεταξύ βουλευτών και εξαγωγή κανόνων συσχέτισης. Παρέχει διαδραστική **Web εφαρμογή** με δυνατότητα αναζήτησης, φιλτραρίσματος και **οπτικοποίησης** αποτελεσμάτων.

---

### **🚀 Project Overview**
- **Ανάκτηση Πληροφορίας**: Θεματική εξόρυξη και αναζήτηση από σώμα κοινοβουλευτικών ομιλιών.
- **Οπτικοποίηση & Ανάλυση**: Διερεύνηση σχέσεων, χρονικών τάσεων και εννοιών με διαγράμματα και metrics.
- **Διανυσματική Αναπαράσταση**: Συγκρίσεις βουλευτών με βάση semantic similarity (LSI).

---

### **🔍 Key Features**
- **TF-IDF & LSI**: Εντοπισμός σημαντικών όρων ανά βουλευτή ή κόμμα και θεματική προσέγγιση ομιλιών.
- **Apriori Algorithm**: Εξαγωγή κανόνων συσχέτισης μεταξύ όρων σε μεγάλο σώμα κειμένου.
- **Search & Filter UI**: Διαδραστική αναζήτηση και φιλτράρισμα με βάση ομιλητή, κόμμα και λέξη.
- **Χρονική Ανάλυση**: Οπτικοποίηση εξέλιξης λέξεων ή θεμάτων μέσα στο χρόνο.

---

### **🛠️ Technical Highlights**
- **Python & Flask**: Backend server για επικοινωνία και επεξεργασία δεδομένων.
- **HTML/CSS/JavaScript**: Responsive frontend UI με δυνατότητα search & filter.
- **Pandas & Scikit-Learn**: Επεξεργασία δεδομένων και υλοποίηση μοντέλων IR.
- **Matplotlib/Seaborn/WordCloud**: Οπτικοποίηση δεδομένων και λέξεων-κλειδιών.

---

### **📂 Code Structure**
- **app.py**: Main Flask app – τρέχει τον server και σερβίρει τα endpoints.
- **initialize.py**: Προετοιμασία και φόρτωση δεδομένων (stemming, filtering, vectors).
- **templates/**: HTML αρχεία για το frontend.
- **static/**: CSS/JS για το UI.
- **models/**: Υλοποίηση LSI, TF-IDF και Apriori.
- **data/**: Sample dataset (CSV) για local testing.

---

## **📦 Installation**
Εγκατάσταση των απαιτούμενων βιβλιοθηκών:
```bash
pip install -r requirements.txt
```

---

## **▶️ Run**
Εκκίνηση του Flask app:
```bash
python app.py
```
Ανοίξτε τον browser σας στη διεύθυνση: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **⚠️ Σημαντική Σημείωση**
Για να τρέξει σωστά η εφαρμογή πρέπει να αλλάξετε το CSV στο `initialize.py`:
```python
Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')
```
Το πλήρες αρχείο **Greek_Parliament_Proceedings_1989_2020.csv** δεν είναι διαθέσιμο στο GitHub λόγω μεγέθους. Μπορείτε να το κατεβάσετε από:
[https://github.com/iMEdD-Lab/Greek_Parliament_Proceedings](https://github.com/iMEdD-Lab/Greek_Parliament_Proceedings)

---

**🏷️ Tags**: **Python**, **Flask**, **Information Retrieval**, **TF-IDF**, **LSI**, **Apriori**, **Data Visualization**, **NLP**, **Greek Parliament**, **Text Mining**
**🌟 Concept**: *"Ένα εργαλείο ανάκτησης και ανάλυσης πληροφορίας από τα κοινοβουλευτικά πρακτικά της Ελλάδας, αξιοποιώντας σύγχρονες IR τεχνικές για θεματική εξαγωγή, σύγκριση βουλευτών και οπτικοποίηση λέξεων μέσα στον χρόνο."*
