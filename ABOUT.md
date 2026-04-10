# Seam — useseam.ai

## One-liner

Seam is a data sync platform that keeps workspace tools like Notion, Airtable, Linear, and Google Sheets in sync — in any direction — so ops and data teams don't have to do it manually.

## Problem

Companies adopt tools like Notion, Airtable, Linear, and Asana organically. Over time, critical data ends up fragmented across these tools with no connections between them. The result: ops teams become human middleware — copy-pasting, exporting CSVs, and manually keeping everything consistent. Existing solutions are either one-directional API connectors or require engineering resources to set up and maintain.

## Vision

Seam treats a company's tool ecosystem as a data graph, not a hub-and-spoke model. Any tool can be a source, any tool can be a destination. Users define the edges — which data flows where, in which direction, on what schedule. The long-term vision includes bidirectional sync with conflict resolution, natural language schema mapping, a cross-tool queryable analytics layer, and full audit/time-travel history. The end state: any ops-heavy company (20–2,000 people) gets the data coherence of a company with a full data team, without hiring one.

## Current state

- Working CLI tool that bulk-updates Notion databases from CSV, Python compute functions, or SQL queries (open-source, Python)
- Web-based operator UI for managing Notion connections, database schemas, and job execution
- Public landing page live at https://useseam.ai with waitlist capture and email notifications
- Deployed on Fly.io with persistent storage and Resend for email forwarding

## Technical highlights

- FastAPI backend, single-file HTML frontend with three swappable CSS themes (warm, minimal, dark)
- SQLite-backed page cache with adaptive pagination and parallel partition fetching for the Notion API
- Plan-based execution model: all bulk operations generate a reviewable plan before writing, with dry-run as the default
- DuckDB integration for SQL-based transformations against Notion data

## Target audience

Ops, growth, and data teams at companies where productivity tools have grown beyond the manual-input use case — teams that need their data to flow between tools without engineering involvement.
