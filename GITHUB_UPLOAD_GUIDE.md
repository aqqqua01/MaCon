# 📤 Інструкція по завантаженню на GitHub

## Крок 1: Створи репозиторій на GitHub

1. Зайди на [github.com](https://github.com)
2. Натисни "New repository" (зелена кнопка)
3. Назва: `MaCon` або `mafiles-converter`
4. Опис: `Modern Steam Guard MaFiles Converter with multilingual Flet UI`
5. Вибери Public або Private
6. **НЕ додавай** README, .gitignore, license (вони вже є)
7. Натисни "Create repository"

## Крок 2: Ініціалізуй Git локально

Відкрий термінал в папці `D:\AI\MaCon 3` і виконай:

```bash
# Ініціалізація Git
git init

# Додай всі файли
git add .

# Перший commit
git commit -m "Initial commit: MaCon v3.0 - Steam Guard MaFiles Converter

Features:
- Modern Flet UI with dark/light theme
- Multilingual support (EN/UK/RU)
- XLSX file processing
- Configurable column settings
- Toast notifications
- Auto-save settings
- Standalone .exe build
- Web-based user guide"
```

## Крок 3: Підключи до GitHub

```bash
# Замість YOUR_USERNAME вставь свій username
git remote add origin https://github.com/YOUR_USERNAME/MaCon.git

# Перейменуй гілку на main (якщо потрібно)
git branch -M main

# Завантаж на GitHub
git push -u origin main
```

## Крок 4: Створи Release з .exe файлом

1. На GitHub перейди на вкладку "Releases"
2. Натисни "Create a new release"
3. Tag: `v3.0.0`
4. Title: `MaCon v3.0 - Initial Release`
5. Description:

```markdown
## 🎉 First Release of MaCon!

### What's Included
- ✅ Standalone Windows executable (MaCon.exe)
- ✅ User guide (index.html)
- ✅ Example XLSX template
- ✅ Full documentation

### Features
- 🌐 Multilingual (English, Ukrainian, Russian)
- 🎨 Modern Flet UI with dark/light theme
- 📊 XLSX file support
- ⚙️ Configurable column settings
- 🔔 Toast notifications
- 💾 Auto-save settings

### Installation
1. Download `MaCon-v3.0-Windows.zip`
2. Extract all files
3. Run `MaCon.exe`
4. Open `index.html` for detailed instructions

### Requirements
- Windows 10/11 (64-bit)
- No Python required!

### File Size
- MaCon.exe: ~285 MB (all dependencies included)
```

6. Додай файл: Створи ZIP архів з `build_output/` папки:
   - MaCon.exe
   - index.html
   - example_template.xlsx
   - README.txt

7. Назви архів: `MaCon-v3.0-Windows.zip`
8. Натисни "Publish release"

## Крок 5: Оновлення README з правильними посиланнями

Після створення репозиторію відкрий `README.md` і заміни:
- `yourusername` → твій GitHub username
- Додай скріншоти програми (необов'язково)

```bash
# Commit оновлення
git add README.md
git commit -m "Update README with correct repository links"
git push
```

## 🎯 Готово!

Твій репозиторій тепер доступний на GitHub:
`https://github.com/YOUR_USERNAME/MaCon`

## 📋 Додатково

### Створити ZIP архів для Release:

```powershell
# В PowerShell
cd "D:\AI\MaCon 3"
Compress-Archive -Path "build_output\MaCon.exe", "build_output\index.html", "build_output\example_template.xlsx", "build_output\README.txt" -DestinationPath "MaCon-v3.0-Windows.zip"
```

### Додати GitHub Topics:

На GitHub, в налаштуваннях репозиторію, додай topics:
- `flet`
- `python`
- `steam-guard`
- `converter`
- `desktop-app`
- `windows`
- `pyinstaller`
- `multilingual`

### Створити GitHub Pages для документації:

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / folder: `build_output`
4. Сайт буде доступний: `https://YOUR_USERNAME.github.io/MaCon/`

---

**Успіхів! 🚀**

