# skill-public-api

A Claude skill that turns the community list [public-apis/public-apis](https://github.com/public-apis/public-apis) into a searchable catalog: **1,953 free APIs in 51 categories**, each with auth type, HTTPS and CORS.

Ask Claude things like *"find me a free weather API with no key that works from the browser"* and it searches the catalog, then returns 2–5 ranked candidates instead of a link dump.

## What's inside

```
public-apis/                 # the skill (copy this folder)
├── SKILL.md                 # when to trigger + how to search and recommend
├── references/catalog.tsv   # category, name, description, auth, https, cors, url
├── scripts/search.py        # keyword search with --no-auth / --https / --cors filters
└── LICENSE
tools/build_catalog.py       # regenerates catalog.tsv from the upstream README
```

The sponsored sections of the upstream README were removed, and UTM tracking was stripped from links.

## Install

**Claude Code**: copy the `public-apis` folder into `~/.claude/skills/`:

```bash
git clone https://github.com/Chinorab/skill-public-api.git
cp -r skill-public-api/public-apis ~/.claude/skills/
```

**claude.ai**: download `public-apis.zip` from the [latest release](https://github.com/Chinorab/skill-public-api/releases/latest) and upload it under *Settings → Capabilities → Skills*.

## Search from the command line

```bash
python public-apis/scripts/search.py weather --no-auth --https --cors
python public-apis/scripts/search.py --category "Currency Exchange" --no-auth
```

## Refresh the catalog

```bash
git clone --depth 1 https://github.com/public-apis/public-apis.git upstream
python tools/build_catalog.py upstream/README.md public-apis/references/catalog.tsv
```

Snapshot date: 2026-09-29. The upstream list is community-curated, so some entries may be outdated. The skill tells Claude to check that an API is still live before relying on it.

## License

MIT. The catalog data comes from [public-apis/public-apis](https://github.com/public-apis/public-apis) (MIT, © 2022 public-apis).
