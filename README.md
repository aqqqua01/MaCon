# 🔐 MaCon v3.0 - MaFiles Converter

<div align="center">

![Version](https://img.shields.io/badge/version-3.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

**Modern desktop application for converting Steam Guard MaFiles with login credentials from XLSX files**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Build](#-build-from-source) • [Documentation](#-documentation)

</div>

---

## 📖 About

**MaCon** (MaFiles Converter) is a powerful desktop application that helps you manage Steam Guard authentication files (.maFile) by matching them with login credentials from Excel files. Built with modern Flet framework, it offers a beautiful, user-friendly interface with multilingual support.

### ✨ Features

- 🌐 **Multilingual** - English, Ukrainian, Russian
- 🎨 **Modern UI** - Built with Flet framework
- 🌓 **Dark/Light Theme** - Comfortable for any lighting
- 📊 **XLSX Support** - Import from Excel files
- ⚙️ **Flexible Settings** - Configure column numbers and start row
- 💾 **Auto-save** - Settings persist between sessions
- 🔔 **Toast Notifications** - Visual feedback on completion
- 📝 **Detailed Logs** - Toggle logging view
- 🚀 **Standalone** - Compiled .exe available (no Python needed)

## 🖼️ Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x500?text=MaCon+Main+Interface)

### Settings & Configuration
![Settings](https://via.placeholder.com/800x500?text=Column+Settings)

## 📥 Installation

### Option 1: Download Compiled Version (Recommended)

1. Go to [Releases](../../releases)
2. Download `MaCon-v3.0-Windows.zip`
3. Extract and run `MaCon.exe`
4. No Python installation required! ✅

### Option 2: Run from Source

**Requirements:**
- Python 3.10 or higher
- pip (Python package manager)

**Steps:**

```bash
# Clone the repository
git clone https://github.com/yourusername/MaCon.git
cd MaCon

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
# or
python run.py
```

## 🚀 Usage

### Quick Start

1. **Launch** `MaCon.exe` or `python main.py`
2. **Select XLSX file** with login/password pairs
3. **Select .maFile directory** where your Steam Guard files are stored
4. **Select output directory** for results
5. **Configure columns** (if needed) - default is Column 1 = Login, Column 2 = Password
6. **Click "Convert"** and wait for completion!

### XLSX File Structure

Your Excel file should have at least 2 columns:

| Column A (Login) | Column B (Password) | Column C (Optional) |
|------------------|---------------------|---------------------|
| steam_user1      | Password123         | Notes               |
| steam_user2      | SecurePass456       | More info           |
| steam_user3      | MyPass789           | Comments            |

**Default Settings:**
- Login Column: 1 (Column A)
- Password Column: 2 (Column B)
- Start Row: 1 (First data row)

**Custom Structure:**
If your data is in different columns, use the "Column Settings" section to specify the correct column numbers.

### Output

After conversion, you'll get:
- `accounts.txt` - Text file with login:password pairs
- Copied `.maFile` files matching the logins
- Toast notification with results

**Example output structure:**
```
output_folder/
├── accounts.txt
├── steam_user1.maFile
├── steam_user2.maFile
└── steam_user3.maFile
```

## 🔧 Configuration

### Column Settings
- **Login Column** - Specify which column contains logins (1, 2, 3...)
- **Password Column** - Specify which column contains passwords (1, 2, 3...)
- **Start Row** - Which row to start reading from (1 = first row, 2 = second...)

### Language
Click the language dropdown in the top-right corner to switch between:
- 🇬🇧 English
- 🇺🇦 Українська
- 🇷🇺 Русский

### Theme
Click the theme button (🌓) to toggle between dark and light modes.

All settings are automatically saved to `mafiles_converter_config.json`.

## 🛠️ Build from Source

### Build Standalone Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build Windows executable
pyinstaller --name="MaCon" --onefile --windowed --distpath="./build_output" --workpath="./build_output/temp" --specpath="./build_output" main.py

# Executable will be in build_output/MaCon.exe
```

### Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run in development mode
python run.py

# Test the application
python main.py
```

## 📚 Documentation

- 📖 [User Guide](build_output/index.html) - Open in browser for detailed instructions
- 📄 [README.txt](build_output/README.txt) - Text version of documentation
- 🎨 [ICON_GUIDE.md](ICON_GUIDE.md) - How to add custom icons
- 📊 [Example Template](build_output/example_template.xlsx) - Sample XLSX file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Flet](https://flet.dev/) - Beautiful cross-platform apps in Python
- Uses [pandas](https://pandas.pydata.org/) for Excel file processing
- Uses [openpyxl](https://openpyxl.readthedocs.io/) for XLSX support

## 📧 Contact

Project Link: [https://github.com/yourusername/MaCon](https://github.com/yourusername/MaCon)

## 🗺️ Roadmap

- [ ] Support for CSV files
- [ ] Batch processing for multiple XLSX files
- [ ] Import/Export settings profiles
- [ ] Cross-platform support (Linux, macOS)
- [ ] Web version

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you find it helpful!

</div>
