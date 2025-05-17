import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer as TVR
from sklearn.metrics.pairwise import cosine_similarity as CS
b = pd.read_csv("Books.csv")
b["combined"] = b["title"] + " " + b["genre"]
tvr = TVR()
tvrm = tvr.fit_transform(b["combined"])
def rb(bt):
    if bt not in b["title"].values:
        return ["Book not found"]
    idx = b[b["title"] == bt].index[0]
    cs = CS(tvrm[idx],tvrm).flatten()
    si = cs.argsort()[-6:-1][::-1]
    return b["title"].iloc[si].tolist()
r = rb(str(input("Enter a book title : ")))
print("Recommend Books :")
for book in r:
    print(f"- {book}")