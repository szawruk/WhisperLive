from whisper_live.client import TranscriptionClient
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run WhisperLive client with microphone input')
    parser.add_argument('--host', type=str, default='localhost', help='Server host address')
    parser.add_argument('--port', type=int, default=9090, help='Server port')
    parser.add_argument('--lang', type=str, default='pl', help='Language for transcription')
    parser.add_argument('--translate', action='store_true', help='Translate to English')
    parser.add_argument('--model', type=str, default='small', help='Whisper model size')
    parser.add_argument('--use_vad', action='store_true', help='Use Voice Activity Detection')
    parser.add_argument('--save_recording', action='store_true', help='Save microphone input to WAV file')
    parser.add_argument('--output_file', type=str, default='./output_recording.wav', 
                        help='Output WAV file path for recording')
    
    args = parser.parse_args()

    # Initialize the client
    client = TranscriptionClient(
        args.host,
        args.port,
        lang=args.lang,
        translate=args.translate,
        model=args.model,
        use_vad=args.use_vad,
        save_output_recording=args.save_recording,
        output_recording_filename=args.output_file
    )

    print(f"Starting transcription with microphone input...")
    print(f"Press Ctrl+C to stop")
    
    try:
        # Start transcription from microphone
        client()
    except KeyboardInterrupt:
        print("\nStopping transcription...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 