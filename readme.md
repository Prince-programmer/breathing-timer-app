# Breathing Timer Application

## Overview
The Breathing Timer Application is a simple, interactive tool built using Python and Tkinter. It guides users through breathing exercises by timing inhalation, holding, and exhalation phases. Users can customize the duration of each inhale cycle and the total number of cycles for the exercise. The app is designed to promote relaxation and mindfulness.

## Features
- **Customizable Inhale Time**: Set the duration for inhalation in seconds.
- **Customizable Cycles**: Choose how many breathing cycles to complete.
- **Hold and Exhale Timing**: Automatic adjustments for holding and exhaling after inhaling.
- **Audio Feedback**: A beep sound plays to mark the end of each phase.
- **Cycle Display Option**: Show or hide the current cycle count during the exercise.
- **Clean and Modern UI**: Designed with a clean aesthetic using Tkinter's ttk widgets.
- **Stop Button**: Easily stop the exercise and return to the settings menu.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)
- **winsound** (only available on Windows for sound alerts)

## Installation
1. Ensure Python is installed on your system. Download it from python.org if necessary.

2. Clone this repository or download the script file:
    ```bash
    git clone https://github.com/yourusername/breathing-timer-app.git

3. Navigate to the project directory:
    ```bash
    cd breathing-timer-app

4. Run the script:
    ```bash
    python breathing_timer.py

## Usage
1. **Set Inhale Time**: Enter the desired inhale duration in seconds (default is 4 seconds).
2. **Set Number of Cycles**: Specify how many cycles to complete (default is 3 cycles).
3. **Show Cycle Checkbox**: Check or uncheck to display the current cycle count.
4. Click **Start** to begin the breathing exercise.
5. Use the **Stop** button to end the exercise early if needed.

## Example Flow
1. Inhale for the set duration (displayed on the screen).
2. Hold the breath for one second longer than the inhale duration.
3. Exhale for two seconds longer than the inhale duration.
4. Repeat until the set number of cycles is complete.

## Notes
- This application is designed for relaxation purposes and should not be used as a medical tool.
- Sound alerts (**winsound.Beep**) are only available on Windows.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT license.

## Acknowledgements
- Tkinter for providing a simple GUI framework.
- Python community for continuous support and resources.
