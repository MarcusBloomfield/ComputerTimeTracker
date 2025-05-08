# Computer Time Tracker

A simple desktop application built with Python and Tkinter to help users track their time spent on 'Idle' activities versus 'Work' activities.

## Features

*   **Dual Timers**: Tracks "Idle Time" and "Work Time" separately.
*   **Toggle Active Timer**: Easily switch between the Idle and Work timers. The inactive timer is paused.
*   **Status Indicators**: Clearly shows which timer is currently "RUNNING" (green) and which is "PAUSED" (red).
*   **Time Display**: Shows elapsed time for both timers in HH:MM:SS format.
*   **Reset Functionality**: Allows resetting both timers back to zero.
*   **Graphical User Interface**: Simple and intuitive UI built with Tkinter.

## Getting Started

### Prerequisites

*   Python 3.x
*   Tkinter (usually included with standard Python installations)

### Running the Script

To run the application directly from the Python script:

```bash
python ComputerTimeTracker.py
```

## Building the Executable

You can create a standalone executable using PyInstaller.

1.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2.  **Build the Executable**:
    Navigate to the project directory in your terminal and run:
    ```bash
    python -m PyInstaller --onefile --windowed --noupx ComputerTimeTracker.py
    ```
    *   `--onefile`: Creates a single executable file.
    *   `--windowed`: Prevents a console window from appearing when the application runs.
    *   `--noupx`: Disables UPX compression, which can help reduce false-positive detections by antivirus software.

    The executable will be located in the `dist` directory.

## Troubleshooting

### Antivirus Detections (False Positives)

Executables created by PyInstaller, especially those that are not digitally signed, can sometimes be flagged as malware by antivirus software or Windows SmartScreen. This is often a false positive.

Steps taken to mitigate this:
*   The build command now includes `--noupx` to disable UPX compression, which is a common trigger for such flags.

If you still encounter issues:
*   **VirusTotal**: You can upload the generated `.exe` file to [VirusTotal.com](https://www.virustotal.com/) to see how many security vendors flag it. A low number of detections usually indicates a false positive.
*   **Code Signing**: For broader distribution or to further reduce warnings, consider digitally signing the executable with a code signing certificate. This establishes the publisher's identity and improves trust.
*   **Exclusions**: For personal use, you can add an exclusion for the file or folder in your antivirus software.

## Changelog

For a history of changes and updates to this project, please see `Changelog.txt`. 