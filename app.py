from shadow import add_entry, analyze, weekly_summary

print("\n Digital Shadow")
print("Write freely.")
print("Commands:")
print("  /i     - reflect")
print("  /w     - weekly summary")
print("  /e     - quit\n")

try:
    while True:
        text = input("> ")

        if text == "/x":
            print("Goodbye.")
            break

        if text == "/i":
            print("\n" + analyze() + "\n")
            continue

        if text == "/w":
            print("\n" + weekly_summary() + "\n")
            continue

        add_entry(text)
        print("Noted.")

except KeyboardInterrupt:
    print("\nGoodbye.")