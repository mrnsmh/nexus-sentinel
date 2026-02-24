# Skill: Nexus-Sentinel (V1.0) - The Autonomous SRE

Nexus-Sentinel is more than a watchdog; it is your server's autonomous reliability engineer. It monitors health, optimizes performance, and handles recovery without user intervention.

## Core Intelligence
- **Proactive Optimization**: Automatically cleans logs and temporary files when disk usage > 80%.
- **Contextual Recovery**: Analyzes stack traces before restarting. If it detects a database connection error, it restarts the database *before* the application.
- **Smart Briefing**: Generates concise, human-readable status reports.
- **Event-Driven Backups**: Monitors critical files (.env, docker-compose.yml) and triggers an incremental backup to Google Drive upon change detection.

## Commands
- **/nexus brief** : Get a human-style summary of server activity over the last 24h.
- **/nexus optimize** : Manually trigger log cleaning and memory optimization.
- **/nexus recover <project>** : Deep diagnostic and multi-step recovery attempt for a specific service.
- **/nexus status** : High-level dashboard of all projects and server vitals.

## Proactive Rules (Autonomous)
1. **Disk Pressure**: If disk > 85%, run `pm2 flush` and clean `~/.npm/_logs`.
2. **RAM Pressure**: If RAM > 90%, identify the top 3 memory-hungry containers and notify via WhatsApp with an "Optimization Suggestion".
3. **Ghost Containers**: Detects and prunes unused Docker networks and dangling images weekly.

## Configuration (Optional)
- `NEXUS_REPORT_CHANNEL`: Channel for briefings (default: WhatsApp).
- `NEXUS_BACKUP_PATH`: GDrive folder ID for automated event-based backups.
