# Plan: Backend/Infra Fixes for Restaurant POS

## Goal
Make the Django backend runnable by registering missing apps, fixing broken URL routing, and correcting `docker-compose.yml` schema so it validates and starts locally.

## Root state (verified)
- `apps/backend/core/settings.py:20-44` — `INSTALLED_APPS` lists `'daily'` last; `notifications` and `backup` are missing though their modules/migrations exist on disk.
- `apps/backend/core/urls.py:4-17` — `urlpatterns` closes at line 17; lines 18-21 contain duplicated `api/daily`/`api/kds` routes **outside** the list (invalid placement, likely causing import/routing errors).
- `docker-compose.yml:39-64` — `web` and `mobile` services are nested **under `volumes`**, which is invalid Compose schema (`additional properties not allowed`).

## Decisions
1. Add `'notifications'` and `'backup'` to `INSTALLED_APPS` after `'daily'` in `settings.py`.
2. Move `web` and `mobile` from under `volumes` to `services` level in `docker-compose.yml`; place `volumes:` key after all service definitions.
3. Remove the three orphaned route lines (18-21) from `urls.py` — `api/daily/` and `api/kds/` are already declared once inside `urlpatterns` at lines 13/16.
4. Keep `env_file: ./apps/backend/.env.example` as-is; note that `.env` may need to be created separately for local runs.

## Ordered tasks
1. Edit `apps/backend/core/settings.py` — append `'notifications'` and `'backup'` to `INSTALLED_APPS` after `'daily'`.
2. Edit `apps/backend/core/urls.py` — delete lines 18-21 (orphaned duplicated routes).
3. Edit `docker-compose.yml` — move `web` and `mobile` service blocks above the `volumes:` key; ensure `volumes:` is defined once at root level after services.
4. Validate: confirm `INSTALLED_APPS` contains all three new apps; confirm `urlpatterns` closes cleanly with no lines after `]`; confirm `docker-compose.yml` structure has `services:` then `volumes:` at root.
5. (Optional, out of scope for this plan) Create `.env` from `.env.example` and run `docker compose config` / `docker compose up -d --build`.

## Validation
- `grep -n "'notifications'\|'backup'" apps/backend/core/settings.py` → both present after `'daily'`.
- `tail -n 5 apps/backend/core/urls.py` → ends at `]` of `urlpatterns`.
- `grep -n "^services:\|^volumes:" docker-compose.yml` → `services:` before `volumes:`, `web`/`mobile` indented under `services:`.

## Open questions / out of scope
- `apps/backend/.env` does not exist locally; creation deferred to implementation phase.
- Running migrations / `docker compose up` is deferred — this plan only fixes the config so those steps become possible.
