#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Головний скрипт для запуску MaFiles Converter v2
"""

import sys
import os
from pathlib import Path

def check_dependencies():
    """Перевірка наявності необхідних залежностей"""
    required_modules = ['pandas', 'openpyxl', 'bs4', 'lxml', 'flet']
    missing_modules = []
    
    for module in required_modules:
        try:
            if module == 'bs4':
                import bs4
            else:
                __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print("Помилка: Відсутні необхідні модулі:")
        for module in missing_modules:
            print(f"  - {module}")
        print("\nВстановіть їх командою:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Головна функція"""
    print("MaFiles Converter v2 - XLSX/HTML")
    print("=" * 40)
    
    # Перевіряємо залежності
    if not check_dependencies():
        sys.exit(1)
    
    # Імпортуємо та запускаємо GUI (Flet версія)
    try:
        from mafiles_converter_flet import MaFilesConverterGUI
        app = MaFilesConverterGUI()
        app.run()
    except Exception as e:
        print(f"Помилка запуску програми: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

