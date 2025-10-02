# 🎨 Гід по іконкам для MaCon

## 📁 Формати іконок

### Підтримувані формати:
1. **PNG** (рекомендовано) - найкраща якість
   - Розмір: 512x512 або 1024x1024 пікселів
   - Прозорий фон
   
2. **SVG** (векторний) - масштабується без втрати якості
   - Ідеально для будь-яких розмірів
   - Малий розмір файлу
   
3. **ICO** (Windows стандарт)
   - Може містити кілька розмірів (16x16, 32x32, 48x48, 256x256)
   - Краще для Windows exe файлів

## 🔧 Як додати іконку

### 1. Іконка у вікні програми (runtime)

Помісти файл іконки в корінь проекту (`D:\AI\MaCon 3\`) і розкоментуй в `mafiles_converter_flet.py`:

```python
# У функції main():
page.window_icon = "icon.png"  # або icon.svg, icon.ico
```

### 2. Іконка для скомпільованого .exe файлу

При компіляції використовуй команду:

```bash
# Windows
flet build windows --icon icon.png

# macOS
flet build macos --icon icon.png

# Linux
flet build linux --icon icon.png

# Android
flet build apk --icon icon.png

# iOS
flet build ipa --icon icon.png
```

## 📦 Структура файлів

```
MaCon 3/
├── run.py
├── mafiles_converter_flet.py
├── icon.png           # Основна іконка (512x512 або більше)
├── icon.svg           # Альтернатива (векторний формат)
└── icon.ico           # Для Windows (опціонально)
```

## 🎨 Створення іконки

### Онлайн інструменти:
- **Figma** / **Canva** - для дизайну
- **RealFaviconGenerator.net** - генерація всіх форматів
- **CloudConvert.com** - конвертація PNG → ICO/SVG

### Рекомендації дизайну:
- ✅ Простий і зрозумілий дизайн
- ✅ Контрастні кольори
- ✅ Працює як на темному, так і на світлому фоні
- ✅ Добре виглядає в малих розмірах (16x16)
- ✅ Використовуй прозорий фон (PNG/SVG)

### Приклад концепції для MaCon:
- 🔐 Ікона Shield (щит) + літери "MC"
- 📱 Іконка Mobile + Steam лого стилістика
- 🔄 Стрілки конвертації + файл

## 🚀 Швидкий старт

1. Створи іконку 512x512 PNG з прозорим фоном
2. Збережи як `icon.png` в корені проекту
3. Розкоментуй `page.window_icon = "icon.png"` в коді
4. Запусти: `python run.py`
5. Для .exe: `flet build windows --icon icon.png`

## 🔍 Тестування іконки

```python
# Тимчасовий тест іконки
page.window_icon = "https://example.com/your-icon.png"  # URL працює теж!
```

## 📝 Додаткові параметри компіляції

```bash
flet build windows \
  --icon icon.png \
  --name MaCon \
  --description "MaFiles Converter" \
  --product-name "MaCon" \
  --file-version "3.0.0" \
  --copyright "© 2024"
```

## ⚠️ Важливо

- PNG іконки **ПОВИННІ** мати прозорий фон для кращого вигляду
- SVG підтримується, але PNG краще для Windows
- ICO формат оптимальний для Windows .exe
- Розмір файлу іконки має бути < 1MB

## 🎯 Чеклист

- [ ] Створив іконку 512x512 PNG
- [ ] Помістив `icon.png` в корінь проекту
- [ ] Розкоментував `page.window_icon` в коді
- [ ] Протестував запуск програми
- [ ] Зкомпілював з іконкою: `flet build windows --icon icon.png`
- [ ] Перевірив .exe файл - іконка відображається

---

**Рекомендація:** Почни з простого PNG 512x512, а потім експериментуй з SVG для професійного вигляду!

