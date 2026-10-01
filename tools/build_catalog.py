"""Parse public-apis README into a grep-friendly TSV catalog for the skill."""
import re, sys, collections
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

src, out = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().splitlines()

def clean_url(u):
    p = urlsplit(u.strip())
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not k.lower().startswith("utm_")]
    return urlunsplit((p.scheme, p.netloc, p.path, urlencode(q), p.fragment))

def cell(s):
    s = s.strip().strip("`").strip()
    return re.sub(r"\s+", " ", s).replace("\t", " ")

rows, counts = [], collections.Counter()
cat, in_list = None, False
for ln in lines:
    if ln.startswith("## Index"):
        in_list = True
    if ln.startswith("## License"):
        break
    if not in_list:
        continue
    m = re.match(r"^### (.+)$", ln)
    if m:
        cat = m.group(1).strip()
        continue
    if cat and ln.startswith("| [") :
        parts = [p for p in ln.strip().strip("|").split("|")]
        if len(parts) < 5:
            continue
        nm = re.match(r"\s*\[(.+?)\]\((.+?)\)", parts[0])
        if not nm:
            continue
        name, url = nm.group(1), clean_url(nm.group(2))
        desc, auth, https, cors = (cell(p) for p in parts[1:5])
        auth = auth or "No"
        rows.append((cat, cell(name), desc, auth, https, cors, url))
        counts[cat] += 1

with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("category\tname\tdescription\tauth\thttps\tcors\turl\n")
    for r in rows:
        f.write("\t".join(r) + "\n")

print(len(rows), "APIs in", len(counts), "categories")
for c, n in counts.items():
    print(f"{n:4d}  {c}")
