import argparse
from pydub import AudioSegment
import os

def split_audio(input_file, output_folder, segment_length_ms=15*60*1000):
    # Load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the number of segments
    num_segments = len(audio) // segment_length_ms + 1

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Split the audio into segments of specified length
    for i in range(num_segments):
        start_time = i * segment_length_ms
        end_time = min((i + 1) * segment_length_ms, len(audio))
        segment = audio[start_time:end_time]
        segment.export(os.path.join(output_folder, f"segment_{i+1}.{input_file.split('.')[-1]}"), format=input_file.split('.')[-1])

    print(f"{num_segments} audio segments created successfully.")

def concatenate_segments(input_folder, output_file):
    # Get a list of all audio segments in the input folder
    segment_files = [file for file in os.listdir(input_folder) if file.startswith('segment_') and file.endswith('.wav')]
    segment_files.sort()  # Ensure segments are concatenated in order

    # Initialize the combined audio segment
    combined_audio = AudioSegment.empty()

    # Concatenate each audio segment to the combined audio segment
    for file in segment_files:
        audio_segment = AudioSegment.from_file(os.path.join(input_folder, file))
        combined_audio += audio_segment

    # Ensure the output folder exists
    output_folder = os.path.dirname(output_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Export the combined audio to the output file
    combined_audio.export(output_file, format='wav')

    print("Audio segments concatenated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split and concatenate audio files.")
    parser.add_argument("--input_file", help="Path to the input audio file to split.")
    parser.add_argument("--output_folder", help="Path to the output folder for segments.")
    parser.add_argument("--segment_length", type=int, default=900, help="Segment length in seconds (default: 900).")
    parser.add_argument("--operation", choices=["split", "concat"], help="Specify 'split' to split the audio file or 'concat' to concatenate segments.")
    parser.add_argument("--input_folder", help="Path to the input folder containing segments (for concatenation operation).")
    parser.add_argument("--output_file", help="Path to the output file for concatenated audio (for concatenation operation).")

    args = parser.parse_args()

    if args.operation == "split":
        split_audio(args.input_file, args.output_folder, args.segment_length * 1000)  # Convert seconds to milliseconds
    elif args.operation == "concat":
        concatenate_segments(args.input_folder, args.output_file)
