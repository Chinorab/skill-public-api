"""Search the public-apis catalog.

Usage: python search.py [keywords...] [--category TEXT] [--no-auth] [--https] [--cors] [--limit N]
Keywords match name + description + category (all must match, case-insensitive).
"""
import argparse, csv, os, sys

ap = argparse.ArgumentParser()
ap.add_argument("keywords", nargs="*")
ap.add_argument("--category", "-c")
ap.add_argument("--no-auth", action="store_true", help="only APIs needing no key")
ap.add_argument("--https", action="store_true", help="only HTTPS APIs")
ap.add_argument("--cors", action="store_true", help="only APIs with CORS=Yes (callable from a browser)")
ap.add_argument("--limit", type=int, default=50)
a = ap.parse_args()

path = os.path.join(os.path.dirname(__file__), "..", "references", "catalog.tsv")
with open(path, encoding="utf-8") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))

kw = [k.lower() for k in a.keywords]
hits = []
for r in rows:
    hay = f"{r['name']} {r['description']} {r['category']}".lower()
    if kw and not all(k in hay for k in kw):
        continue
    if a.category and a.category.lower() not in r["category"].lower():
        continue
    if a.no_auth and r["auth"] != "No":
        continue
    if a.https and r["https"] != "Yes":
        continue
    if a.cors and r["cors"] != "Yes":
        continue
    hits.append(r)

sys.stdout.reconfigure(encoding="utf-8")
for r in hits[: a.limit]:
    print(f"[{r['category']}] {r['name']} — {r['description']} | auth={r['auth']} https={r['https']} cors={r['cors']} | {r['url']}")
print(f"\n{len(hits)} match(es){' (showing %d)' % a.limit if len(hits) > a.limit else ''}")
