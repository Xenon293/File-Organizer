# File Organizer

Simple Python script to sort files in a folder into category subfolders by extension.

## Features
- Organizes files into: `Images`, `Documents`, `Music`, `Videos`, `Programs`, `Archives`, `Others`
- Handles extension matching case-insensitively
- Avoids filename collisions by default (adds ` (1)`, ` (2)`, etc.)
- Optional overwrite mode with `--overwrite`
- Preview mode with `--dry-run` (no file changes)
- Reports move and failure counts

## Requirements
- Python 3.8+

## Usage
Run against your default Downloads folder:

```bash
python file_organizer.py
```

Run against a specific folder:

```bash
python file_organizer.py "C:\\path\\to\\folder"
```

Overwrite files with the same name in target folders:

```bash
python file_organizer.py "C:\\path\\to\\folder" --overwrite
```

Preview planned moves without changing files:

```bash
python file_organizer.py "C:\\path\\to\\folder" --dry-run
```

## Changelog / Improvements
### 2026-02-22
- Added `--dry-run` flag to preview file moves before execution.
- Improved safety by allowing users to validate actions without modifying files.

## Notes
- The script only processes files directly inside the target folder (not nested subfolders).
- Existing subfolders are skipped.
- Unknown file extensions are moved to `Others`.

## Example
Before:
- `Downloads/photo.jpg`
- `Downloads/report.pdf`
- `Downloads/song.mp3`

After:
- `Downloads/Images/photo.jpg`
- `Downloads/Documents/report.pdf`
- `Downloads/Music/song.mp3`
