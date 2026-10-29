# Public source preview — 2026-10-29

Experimental source-only LAN RTS. The reachable source history was reviewed for publication;
no protected-data/credential blocker was found. No opaque game assets are bundled.

## Fixed and verified

- ClientSession uses object identity and stays hashable after the player joins, so registration
  in the server's session set no longer fails.
- Server, CLI and batch-launcher defaults now bind 127.0.0.1. A LAN address must be explicit.
- Added the missing pytest-asyncio development dependency.
- Two new session/default-bind tests and four existing server-logic tests pass (6 total).

The full suite has **10 existing failures and 24 passes**. The unchanged base has the same
10 failures and 22 passes (configuration constructor/roundtrip and upgrade-research expectations).
These failures were reproduced on Python 3.13 with pytest/pytest-asyncio; the focused tests pass.
Run with `PYTHONPATH=src python -m pytest` after installing development dependencies.

The protocol still has no authentication/frame/queue limits suitable for untrusted networks.
Do not expose this prototype to the Internet. Gameplay/client graphics were not verified here.
