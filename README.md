# WPM Speed Test

A desktop typing speed test application built with Python and tkinter.

## Features

- **Random passages** — one of 5 passages is randomly loaded each session
- **Timed tests** — choose between 5, 10, or 60 second test durations
- **Live character highlighting** — correct characters turn green, incorrect turn red as you type
- **Live countdown** — a timer displays the remaining seconds in the window
- **Accurate WPM** — only fully and correctly typed words count toward your score
- **Replayability** — restart at any time with a new random passage

## Requirements

- Python 3.x
- No external dependencies — uses only the Python standard library (`tkinter`)

## Running

```bash
python main.py
```

## How to Use

1. Select a time duration using the radio buttons (5s, 10s, or 60s)
2. Click into the input field and start typing the passage shown above
3. The timer starts automatically on your first keystroke
4. When time runs out, your WPM score is displayed
5. Click **Restart** to play again with a new passage

## Project Structure

```
wpm_test/
├── main.py       # Application entry point and GUI
└── texts.py      # List of passages used in the test
```
