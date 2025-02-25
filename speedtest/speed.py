import speedtest

def run_speedtest():
    try:
        # Initialize the Speedtest object
        st = speedtest.Speedtest()

        print("\nTesting download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        # Get results
        results = st.results.dict()

        # Print results
        print(
            f"\nDownload Speed: {download_speed:.2f} Mbps\n"
            f"Upload Speed: {upload_speed:.2f} Mbps\n"
            f"Ping: {results['ping']} ms\n"
        )

    except speedtest.SpeedtestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

run_speedtest()
