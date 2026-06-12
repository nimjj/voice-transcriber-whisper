from RealtimeSTT import AudioToTextRecorder

def main():
    print("🎙️ Initializing recorder... Please wait.")
    
    # Initialize the recorder wrapper
    recorder = AudioToTextRecorder(
        model="base",             # Sweet spot for your AMD CPU
        device="cpu",             # Forces CPU usage on your AMD machine
        compute_type="int8"       # Low-memory quantized compression
    )
    
    print("✅ System Ready! Speak into your microphone...")
    
    while True:
        # This keeps listening and prints text as soon as it detects you stopped speaking
        text = recorder.text()
        print(f"📋 Transcribed: {text}")

if __name__ == '__main__':
    # This block shields Windows from multiprocessing crash loops
    main()