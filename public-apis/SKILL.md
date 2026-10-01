---
name: public-apis
description: Catalog of ~1,950 free public APIs in 51 categories (from the community list github.com/public-apis/public-apis), with auth type, HTTPS and CORS for each. Use when the user needs a free API or data source for a project, asks "is there an API for X", "free weather / geocoding / currency / crypto / news / sports / jobs API", wants an API that needs no key, or one callable straight from the browser (CORS). Triggers FR: "trouve-moi une API", "API gratuite pour", "source de données", "API sans clé". NOT for paid enterprise API comparisons or for designing your own API.
---

# Public APIs catalog

`references/catalog.tsv` holds every entry of the public-apis list (snapshot 2026-09-29, MIT license), one API per line:

```
category	name	description	auth	https	cors	url
```

- **auth**: `No` (no key), `apiKey`, `OAuth`, `X-Mashape-Key`, `User-Agent`
- **https**: `Yes` / `No`
- **cors**: `Yes` (callable from front-end JS), `No` (needs a backend/proxy), `Unknown`

Sponsored sections of the upstream README (APILayer ads, MCP servers) were dropped and UTM tracking stripped from links.

## How to find an API

Never load the whole file into context (250 KB). Search it:

1. **Grep** the TSV with keywords (case-insensitive), e.g. pattern `weather` or `^Geocoding\t`. Each matching line is self-contained.
2. Or run the helper (filters by auth/HTTPS/CORS):
   ```bash
   python scripts/search.py weather --no-auth --https --cors
   python scripts/search.py --category "Currency Exchange" --no-auth
   python scripts/search.py football score --limit 20
   ```
3. No match? Try synonyms (e.g. `football` / `soccer`, `movie` / `film`, `recipe` / `food`) and the category name.

Categories: Animals, Anime, Anti-Malware, Art & Design, Authentication & Authorization, Blockchain, Books, Business, Calendar, Cloud Storage & File Sharing, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Development, Dictionaries, Documents & Productivity, Email, Entertainment, Environment, Events, Finance, Food & Drink, Games & Comics, Geocoding, Government, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Phone, Photography, Programming, Science & Math, Security, Shopping, Social, Sports & Fitness, Test Data, Text Analysis, Tracking, Transportation, URL Shorteners, Vehicle, Video, Weather.

## How to recommend

- Give 2–5 candidates, not a dump. For each: name, what it does, auth, HTTPS/CORS, link.
- Rank by fit to the project's constraints:
  - Static site / browser-only app → prefer `cors=Yes`, `auth=No` (a key in front-end code is public: never ship one there; route keyed APIs through a backend or serverless function).
  - Backend → CORS doesn't matter; `apiKey` is fine, keep it in env vars.
  - Production → prefer HTTPS=Yes and well-known providers.
- The list is community-curated and can be stale: **verify the docs page is alive and the free tier still exists** (fetch the URL) before building on an API, and say so if you couldn't check.
- Mention rate limits / free-tier terms when the docs show them.
