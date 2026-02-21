import argparse
import os
import shutil

# Map destination folders to supported file extensions.
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Programs": [".exe", ".msi", ".dmg"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}


def get_folder_for_file(extension: str) -> str:
    """Return the matching category folder for a file extension."""
    extension = extension.lower()
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return "Others"


def unique_destination_path(dest_dir: str, filename: str) -> str:
    """Return a non-colliding file path in dest_dir for filename."""
    base, extension = os.path.splitext(filename)
    candidate = os.path.join(dest_dir, filename)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dest_dir, f"{base} ({counter}){extension}")
        counter += 1
    return candidate


def organize_folder(folder_path: str, overwrite: bool = False) -> None:
    """Move files in folder_path into category subfolders."""
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder path.")
        return

    moved_count = 0
    failed_count = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip subfolders; only organize files.
        if not os.path.isfile(item_path):
            continue

        _, extension = os.path.splitext(item)
        target_folder = get_folder_for_file(extension)
        dest_dir = os.path.join(folder_path, target_folder)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, item)
        if os.path.exists(dest_path) and not overwrite:
            dest_path = unique_destination_path(dest_dir, item)

        try:
            shutil.move(item_path, dest_path)
            moved_count += 1
        except PermissionError:
            failed_count += 1
            print(f"Permission denied: {item_path}")
        except OSError as error:
            failed_count += 1
            print(f"Failed to move '{item_path}': {error}")
            continue

    print(
        "Organizing complete. "
        f"Moved: {moved_count}, Failed: {failed_count}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize files in a folder into categorized subfolders."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=os.path.expanduser("~/Downloads"),
        help="Folder to organize (default: ~/Downloads).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite files with the same name in destination folders.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    organize_folder(args.folder, overwrite=args.overwrite)
