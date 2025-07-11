# SRT to TXT Converter

A simple Python script to convert `.srt` subtitle files into clean `.txt` text files by removing timestamps and line numbers.

## Features

- Removes timestamps and numbering
- Extracts clean dialogue/text only
- Saves output to a `txts/` directory

## How to Use

1. Run the script:
   ```bash
   python srt_to_txt.py
   ```
2. Enter the path to the .srt file when prompted. (inside double qoutation)

3. The converted .txt file will be saved to the txts/ folder automatically.

Example

Input (example.srt):
```sql
1
00:00:01,000 --> 00:00:03,000
Hello there.

2
00:00:03,500 --> 00:00:05,000
How are you?
```
Output (txts/example.txt):
```sql
Hello there.
How are you?
```
