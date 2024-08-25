# Downloads Folder Organizer

Python script for macOS that automatically organizes downloaded files into folders based on course codes. 

## Features

- Automatically tracks new downloads.
- Organizes files based on course codes found in the file name.
- Case-insensitive and space-insensitive course code matching.
- Supports tracking incomplete `.crdownload` files until the download is finished.

## Installation

### Prerequisites

- macOS system
- Python 3.0 ^
- `watchdog` library

To install the required Python library, run:

```bash
pip install watchdog
