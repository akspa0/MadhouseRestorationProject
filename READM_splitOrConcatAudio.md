# Audio Split and Concatenate Script

This script allows you to split large audio files into smaller segments and concatenate audio segments back into a single file.

## Features

- **Splitting Audio:**
  - Specify an input audio file to split.
  - Choose the segment length in seconds.
  - Output segments are named with a numerical prefix.
  - Supports various audio formats like WAV, MP3, FLAC, OGG, etc.

- **Concatenating Audio Segments:**
  - Provide an input folder containing audio segments to concatenate.
  - Handles sub-segmented filenames with prefix and suffix numbers.
  - Detects and processes primary and secondary segments for proper concatenation.
  - Output file format is determined by the extension of the output file name.

## Usage

1. **Splitting Audio:**
   - Run the script with `--operation split`.
   - Specify the input audio file using `--input_file`.
   - Set the output folder for segments using `--output_folder`.
   - Optionally, adjust the segment length in seconds using `--segment_length`.

2. **Concatenating Audio Segments:**
   - Run the script with `--operation concat`.
   - Provide the input folder containing segments using `--input_folder`.
   - Specify the output file for concatenated audio using `--output_file`.

## Example Commands

- Splitting Audio:
  ```bash
  python splitOrConcatAudio.py --operation split --input_file input_audio.mp3 --output_folder output_segments --segment_length 900
  ```

- Concatenating Audio Segments:
  ```bash
  python splitOrConcatAudio.py --operation concat --input_folder input_segments --output_file output_audio.mp3
  ```

For more details and options, run the script with the `--help` flag.

**Note:** Ensure the necessary Python libraries (`pydub`, `audioread`, etc.) are installed before running the script.
```

Feel free to adjust and expand upon this README as needed for your project documentation.
