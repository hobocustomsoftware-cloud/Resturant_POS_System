# Plan: Backend/Infra Fixes for Restaurant POS

## Goal
Make the Django backend runnable by registering missing apps, fixing broken URL routing, correcting `docker-compose.yml` schema, and adding notifications websocket routing.

## Root state (verified)
- `apps/backend/core/settings.py:20-44` — `INSTALLED_APPS` lists `'daily'` last; `notifications` and `backup` are missing though their modules/migrations exist on disk.
- `apps/backend/core/urls.py:4-17` — `urlpatterns` closes at line 17; lines 18-21 contain duplicated `api/daily`/`api/kds` routes **outside** the list (invalid placement).
- `docker-compose.yml:39-64` — `web` and `mobile` services are nested **under `volumes`**, which is invalid Compose schema.
- `apps/backend/core/asgi.py:10-18` — Only includes `kds.routing`; missing `notifications.routing` for `ws/notifications/`.
- `apps/backend/notifications/migrations/` has no migration files (only `__init__.py`).
- `apps/backend/backup/migrations/` has no migration files (only `__init__.py`).

## Decisions
1. Add `'notifications'` and `'backup'` to `INSTALLED_APPS` after `'daily'` in `settings.py`.
2. Remove orphaned duplicated route lines from `urls.py`; add `api/notifications/` and `api/backup/` routes.
3. Move `web` and `mobile` from under `volumes` to `services` level in `docker-compose.yml`; place `volumes:` key after all service definitions.
4. Update `asgi.py` to import `notifications.routing` and combine websocket URL patterns: `kds.routing.websocket_urlpatterns + notifications.routing.websocket_urlpatterns`.
5. Create `0001_initial.py` migrations for `notifications` and `backup` apps.
6. Keep `env_file: ./apps/backend/.env.example` as-is; note `.env` may need creation for local runs.

## Ordered tasks
1. Edit `apps/backend/core/settings.py` — append `'notifications'` and `'backup'` to `INSTALLED_APPS` after `'daily'`.
2. Edit `apps/backend/core/urls.py` — replace orphaned routes with clean routes inside `urlpatterns` including `api/notifications/` and `api/backup/`.
3. Edit `docker-compose.yml` — move `web` and `mobile` service blocks above the `volumes:` key.
4. Edit `apps/backend/core/asgi.py` — import `notifications.routing` and combine URL patterns.
5. Create `apps/backend/notifications/migrations/0001_initial.py` for `DeviceToken` and `Notification` models.
6. Create `apps/backend/backup/migrations/0001_initial.py` for `BackupPlan` and `TenantBackup` models.
7. Validate: check all imports resolve, migrations exist, compose structure valid.

## Validation
- `grep -n "'notifications'\|'backup'" apps/backend/core/settings.py` → both present.
- `tail -n 6 apps/backend/core/urls.py` → ends cleanly with notifications/backup routes inside list.
- `grep -n "^services:\|^volumes:" docker-compose.yml` → services before volumes.
- `grep -n "notifications.routing" apps/backend/core/asgi.py` → present.
- `ls apps/backend/notifications/migrations/ apps/backend/backup/migrations/` → show 0001_initial.py and __init__.py.

## Open questions / out of scope
- `apps/backend/.env` does not exist locally; create from `.env.example` for local runs.
- Running migrations / `docker compose up` deferred to implementation/test phase.

