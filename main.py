from binance_client import create_client, get_futures_symbols

def main():
    client = create_client()
    if not client:
        print("❌ Unable to connect to Binance API.")
        return

    symbols = get_futures_symbols(client)
    print("✅ Scanning the following symbols:", symbols)

if __name__ == "__main__":
    main()
