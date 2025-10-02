#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MaCon - MaFiles Converter v2 - Flet UI версія
Конвертує файли з логінами/паролями у формат для Steam Guard
"""

import os
import shutil
import logging
import json
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
import threading
import time
import asyncio

# Імпорти для парсингу
import pandas as pd

# Flet
import flet as ft

# Багатомовність
TRANSLATIONS = {
    "en": {
        "title": "MaCon",
        "subtitle": "MaFiles Converter",
        "credentials_file": "Credentials file (XLSX)",
        "mafiles_dir": ".maFile files directory",
        "output_dir": "Output directory",
        "select": "📂 Select",
        "files_dirs": "📁 Files and Directories",
        "column_settings": "⚙️ Column Settings",
        "login_column": "Login column",
        "password_column": "Password column",
        "start_row": "Start from row",
        "apply": "✓ Apply",
        "settings_help": "Column and row numbers match positions in Excel",
        "convert": "🚀 Convert",
        "logs": "📋 Logs",
        "hover_to_view": "(hover to view)",
        "language": "🌐 Language",
        "settings_applied": "Settings applied",
        "error": "Error",
        "select_credentials": "Select credentials file",
        "select_mafiles": "Select .maFile directory",
        "select_output": "Select output directory",
        "conversion_started": "🚀 Conversion started...",
        "reading_file": "📂 Reading file",
        "found_credentials": "✓ Found {count} login/password pairs",
        "processing_mafiles": "🔍 Processing .maFile files",
        "conversion_complete": "✅ Conversion completed successfully!",
        "copied_files": "📊 Copied {count} .maFile files",
        "saved_to": "💾 Results saved to",
        "success_title": "Success!",
        "success_message": "✅ Conversion completed!\n\n📊 Processed accounts: {count}\n📁 .maFile files copied: {count}\n💾 accounts.txt created\n\n📂 Saved to:\n{path}",
        "error_occurred": "❌ Error",
        "notification_success": "SUCCESS",
        "notification_processed": "Processed {count} files",
    },
    "uk": {
        "title": "MaCon",
        "subtitle": "Конвертер MaFiles",
        "credentials_file": "Файл з логінами/паролями (XLSX)",
        "mafiles_dir": "Директорія з .maFile файлами",
        "output_dir": "Вихідна директорія",
        "select": "📂 Обрати",
        "files_dirs": "📁 Файли та директорії",
        "column_settings": "⚙️ Налаштування стовпців",
        "login_column": "Стовпець логіна",
        "password_column": "Стовпець пароля",
        "start_row": "Почати з рядка",
        "apply": "✓ Застосувати",
        "settings_help": "Номери стовпців та рядка відповідають позиції в Excel",
        "convert": "🚀 Конвертувати",
        "logs": "📋 Логи",
        "hover_to_view": "(навести для перегляду)",
        "language": "🌐 Мова",
        "settings_applied": "Налаштування застосовано",
        "error": "Помилка",
        "select_credentials": "Оберіть файл з логінами/паролями",
        "select_mafiles": "Оберіть директорію з .maFile файлами",
        "select_output": "Оберіть вихідну директорію",
        "conversion_started": "🚀 Початок конвертації...",
        "reading_file": "📂 Читання файлу",
        "found_credentials": "✓ Знайдено {count} пар логін/пароль",
        "processing_mafiles": "🔍 Обробка .maFile файлів",
        "conversion_complete": "✅ Конвертація завершена успішно!",
        "copied_files": "📊 Скопійовано {count} .maFile файлів",
        "saved_to": "💾 Результат збережено в",
        "success_title": "Успіх!",
        "success_message": "✅ Конвертація завершена!\n\n📊 Оброблено акаунтів: {count}\n📁 Скопійовано .maFile файлів: {count}\n💾 Створено accounts.txt\n\n📂 Збережено в:\n{path}",
        "error_occurred": "❌ Помилка",
        "notification_success": "УСПІХ",
        "notification_processed": "Оброблено {count} файлів",
    },
    "ru": {
        "title": "MaCon",
        "subtitle": "Конвертер MaFiles",
        "credentials_file": "Файл с логинами/паролями (XLSX)",
        "mafiles_dir": "Директория с .maFile файлами",
        "output_dir": "Выходная директория",
        "select": "📂 Выбрать",
        "files_dirs": "📁 Файлы и директории",
        "column_settings": "⚙️ Настройки столбцов",
        "login_column": "Столбец логина",
        "password_column": "Столбец пароля",
        "start_row": "Начать со строки",
        "apply": "✓ Применить",
        "settings_help": "Номера столбцов и строки соответствуют позиции в Excel",
        "convert": "🚀 Конвертировать",
        "logs": "📋 Логи",
        "hover_to_view": "(навести для просмотра)",
        "language": "🌐 Язык",
        "settings_applied": "Настройки применены",
        "error": "Ошибка",
        "select_credentials": "Выберите файл с логинами/паролями",
        "select_mafiles": "Выберите директорию с .maFile файлами",
        "select_output": "Выберите выходную директорию",
        "conversion_started": "🚀 Начало конвертации...",
        "reading_file": "📂 Чтение файла",
        "found_credentials": "✓ Найдено {count} пар логин/пароль",
        "processing_mafiles": "🔍 Обработка .maFile файлов",
        "conversion_complete": "✅ Конвертация завершена успешно!",
        "copied_files": "📊 Скопировано {count} .maFile файлов",
        "saved_to": "💾 Результат сохранен в",
        "success_title": "Успех!",
        "success_message": "✅ Конвертация завершена!\n\n📊 Обработано аккаунтов: {count}\n📁 Скопировано .maFile файлов: {count}\n💾 Создан accounts.txt\n\n📂 Сохранено в:\n{path}",
        "error_occurred": "❌ Ошибка",
        "notification_success": "УСПЕХ",
        "notification_processed": "Обработано {count} файлов",
    }
}

class SettingsManager:
    """Клас для управління налаштуваннями програми"""
    
    def __init__(self, config_file: str = "mafiles_converter_config.json"):
        self.config_file = Path(config_file)
        self.default_settings = {
            "credentials_file": "",
            "mafiles_dir": "",
            "output_dir": "",
            "login_column": 1,
            "password_column": 2,
            "start_row": 1,
            "language": "en",
            "theme_mode": "dark",
        }
    
    def load_settings(self) -> Dict[str, Any]:
        """Завантаження налаштувань з файлу"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    merged_settings = self.default_settings.copy()
                    merged_settings.update(settings)
                    return merged_settings
            else:
                return self.default_settings.copy()
        except Exception as e:
            print(f"Помилка завантаження налаштувань: {e}")
            return self.default_settings.copy()
    
    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Збереження налаштувань у файл"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Помилка збереження налаштувань: {e}")
            return False

class MaFilesConverter:
    def __init__(self):
        self.setup_logging()
        self.credentials = []
        self.mafiles_dir = ""
        self.output_dir = ""
        self.login_column = 1
        self.password_column = 2
        self.start_row = 1
        
    def setup_logging(self):
        """Налаштування системи логування"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('mafiles_converter.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def _clean(self, s) -> str:
        """Очищення рядка від зайвих пробілів"""
        return str(s).strip() if s is not None else ""
    
    def set_column_settings(self, login_column: int, password_column: int):
        """Встановлення налаштувань стовпців для логінів та паролів"""
        if login_column < 1 or password_column < 1:
            raise ValueError("Номери стовпців повинні бути більше 0")
        if login_column == password_column:
            raise ValueError("Стовпці для логіна та пароля не можуть бути однаковими")
        
        self.login_column = login_column
        self.password_column = password_column
        self.logger.info(f"Встановлено стовпці: логін={login_column}, пароль={password_column}")
    
    def set_start_row(self, start_row: int):
        """Встановлення початкового рядка для читання даних"""
        if start_row < 1:
            raise ValueError("Початковий рядок повинен бути більше 0")
        
        self.start_row = start_row
        self.logger.info(f"Встановлено початковий рядок: {start_row}")
    
    def parse_xlsx_credentials(self, xlsx_path: str, sheet_index: int = 0, header: int = None) -> List[Tuple[str, str]]:
        """Парсинг XLSX файлу з логінами/паролями"""
        try:
            self.logger.info(f"Парсинг XLSX файлу: {xlsx_path}")
            self.logger.info(f"Використовую стовпці: логін={self.login_column}, пароль={self.password_column}, початковий рядок={self.start_row}")
            
            df = pd.read_excel(xlsx_path, sheet_name=sheet_index, header=None, engine="openpyxl")
            
            required_columns = max(self.login_column, self.password_column)
            if df.shape[1] < required_columns:
                raise ValueError(f"У XLSX недостатньо стовпців. Знайдено: {df.shape[1]}, потрібно: {required_columns}")
            
            creds = []
            for i in range(self.start_row - 1, len(df)):
                row = df.iloc[i]
                
                login = self._clean(row.iloc[self.login_column - 1])
                password = self._clean(row.iloc[self.password_column - 1])
                
                if login and password:
                    creds.append((login, password))
                    self.logger.info(f"Рядок {i+1}: додано {login}")
                else:
                    self.logger.warning(f"Рядок {i+1}: порожній логін або пароль")
            
            if not creds:
                raise ValueError("Не знайдено валідних пар логін/пароль у XLSX.")
            
            self.logger.info(f"XLSX: знайдено {len(creds)} пар логін/пароль")
            return creds
            
        except Exception as e:
            self.logger.error(f"Помилка парсингу XLSX: {e}")
            raise
    
    def extract_credentials(self, path: str) -> List[Tuple[str, str]]:
        """Автовизначення формату файлу та витягування логінів/паролів"""
        ext = Path(path).suffix.lower()
        self.logger.info(f"Обробка файлу: {path} (розширення: {ext})")
        
        if ext in {".xlsx", ".xls"}:
            return self.parse_xlsx_credentials(path)
        else:
            raise ValueError(f"Непідтримуваний тип файлу: {ext}. Підтримується тільки XLSX/XLS")
    
    def find_mafiles(self, directory: str) -> List[str]:
        """Пошук .maFile файлів у директорії"""
        mafiles = []
        for file in Path(directory).rglob("*.maFile"):
            mafiles.append(str(file))
        return mafiles
    
    def read_mafile_login(self, mafile_path: str) -> Optional[str]:
        """Читання логіна з .maFile файлу"""
        try:
            with open(mafile_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                login = data.get('account_name', '').strip()
                if login:
                    self.logger.info(f"Прочитано логін з {Path(mafile_path).name}: {login}")
                    return login
                else:
                    self.logger.warning(f"Не знайдено account_name в {Path(mafile_path).name}")
                    return None
        except Exception as e:
            self.logger.error(f"Помилка читання {mafile_path}: {e}")
            return None
    
    def get_mafiles_with_logins(self, directory: str) -> List[Tuple[str, str]]:
        """Отримання .maFile файлів з їх логінами"""
        mafiles = self.find_mafiles(directory)
        mafiles_with_logins = []
        
        for mafile_path in mafiles:
            login = self.read_mafile_login(mafile_path)
            if login:
                mafiles_with_logins.append((mafile_path, login))
            else:
                filename = Path(mafile_path).stem
                mafiles_with_logins.append((mafile_path, filename))
                self.logger.warning(f"Використовую ім'я файлу як логін: {filename}")
        
        return mafiles_with_logins
    
    def process_mafiles(self, credentials: List[Tuple[str, str]], mafiles_dir: str, output_dir: str):
        """Обробка .maFile файлів та створення accounts.txt"""
        try:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            mafiles_with_logins = self.get_mafiles_with_logins(mafiles_dir)
            self.logger.info(f"Знайдено {len(mafiles_with_logins)} .maFile файлів з логінами")
            
            if not mafiles_with_logins:
                raise ValueError("Не знайдено .maFile файлів у вказаній директорії")
            
            credentials_dict = dict(credentials)
            self.logger.info(f"Доступні логіни в credentials: {list(credentials_dict.keys())}")
            
            filtered_mafiles = []
            for mafile_path, mafile_login in mafiles_with_logins:
                if mafile_login in credentials_dict:
                    filtered_mafiles.append((mafile_path, mafile_login))
                    self.logger.info(f"Додано до обробки: {mafile_login} (є пароль)")
                else:
                    self.logger.warning(f"Пропущено: {mafile_login} (немає пароля в credentials)")
            
            self.logger.info(f"Після фільтрації залишилося {len(filtered_mafiles)} .maFile файлів")
            
            if not filtered_mafiles:
                raise ValueError("Не знайдено .maFile файлів з логінами, для яких є паролі в credentials")
            
            accounts_path = Path(output_dir) / "accounts.txt"
            with open(accounts_path, 'w', encoding='utf-8') as f:
                for mafile_path, mafile_login in filtered_mafiles:
                    password = credentials_dict[mafile_login]
                    f.write(f"{mafile_login}:{password}\n")
                    self.logger.info(f"Додано в accounts.txt: {mafile_login}:{password}")
            
            self.logger.info(f"Створено accounts.txt з {len(filtered_mafiles)} акаунтами")
            
            copied_count = 0
            for mafile_path, mafile_login in filtered_mafiles:
                new_name = f"{mafile_login}.maFile"
                dest_path = Path(output_dir) / new_name
                
                try:
                    shutil.copy2(mafile_path, dest_path)
                    self.logger.info(f"Скопійовано: {Path(mafile_path).name} -> {new_name}")
                    copied_count += 1
                except Exception as e:
                    self.logger.error(f"Помилка копіювання {mafile_path}: {e}")
            
            self.logger.info(f"Успішно оброблено {copied_count} .maFile файлів")
            return copied_count
            
        except Exception as e:
            self.logger.error(f"Помилка обробки .maFile файлів: {e}")
            raise

class MaFilesConverterGUI:
    def __init__(self):
        self.converter = MaFilesConverter()
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.load_settings()
        self.current_lang = self.settings.get("language", "en")
        
    def t(self, key: str, **kwargs) -> str:
        """Отримання перекладу"""
        text = TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"]).get(key, key)
        if kwargs:
            text = text.format(**kwargs)
        return text
    
    def main(self, page: ft.Page):
        """Головна функція Flet"""
        page.title = "MaCon"
        page.theme_mode = self.settings.get("theme_mode", "dark")
        page.padding = 20
        page.window_min_width = 600
        page.window_min_height = 500
        page.window_width = 900
        page.window_height = 700
        
        # Іконка вікна (підтримує PNG, ICO, SVG)
        page.window_icon = "MaCon.svg"
        
        # Налаштування теми
        page.theme = ft.Theme(
            color_scheme_seed="blue",
        )
        page.dark_theme = ft.Theme(
            color_scheme_seed="blue",
        )
        
        # Змінні для шляхів
        credentials_file_text = ft.TextField(
            value=self.settings.get("credentials_file", ""),
            label=self.t("credentials_file"),
            read_only=True,
            expand=True,
        )
        
        mafiles_dir_text = ft.TextField(
            value=self.settings.get("mafiles_dir", ""),
            label=self.t("mafiles_dir"),
            read_only=True,
            expand=True,
        )
        
        output_dir_text = ft.TextField(
            value=self.settings.get("output_dir", ""),
            label=self.t("output_dir"),
            read_only=True,
            expand=True,
        )
        
        # Налаштування стовпців
        login_column_field = ft.TextField(
            value=str(self.settings.get("login_column", 1)),
            label=self.t("login_column"),
            width=150,
            keyboard_type="number",
        )
        
        password_column_field = ft.TextField(
            value=str(self.settings.get("password_column", 2)),
            label=self.t("password_column"),
            width=150,
            keyboard_type="number",
        )
        
        start_row_field = ft.TextField(
            value=str(self.settings.get("start_row", 1)),
            label=self.t("start_row"),
            width=150,
            keyboard_type="number",
        )
        
        # Dropdown для мови
        language_dropdown = ft.Dropdown(
            width=150,
            value=self.current_lang,
            options=[
                ft.dropdown.Option("en", "English"),
                ft.dropdown.Option("uk", "Українська"),
                ft.dropdown.Option("ru", "Русский"),
            ],
        )
        
        # Перемикач теми
        def toggle_theme(e):
            if page.theme_mode == "dark":
                page.theme_mode = "light"
                theme_icon_button.icon = "dark_mode"
                theme_icon_button.tooltip = "Темна тема"
            else:
                page.theme_mode = "dark"
                theme_icon_button.icon = "light_mode"
                theme_icon_button.tooltip = "Світла тема"
            
            self.settings["theme_mode"] = page.theme_mode
            self.settings_manager.save_settings(self.settings)
            page.update()
        
        theme_icon_button = ft.IconButton(
            icon="light_mode" if page.theme_mode == "dark" else "dark_mode",
            tooltip="Світла тема" if page.theme_mode == "dark" else "Темна тема",
            on_click=toggle_theme,
        )
        
        # Лог область (прихована за замовчуванням)
        log_view = ft.ListView(
            expand=True,
            spacing=5,
            auto_scroll=True,
        )
        
        log_container = ft.Container(
            content=log_view,
            bgcolor="black12",
            border_radius=5,
            padding=10,
            height=200,
        )
        
        def log_message(message: str):
            """Додавання повідомлення до логів"""
            log_view.controls.append(
                ft.Text(message, size=12, selectable=True)
            )
            page.update()
        
        def update_ui_language():
            """Оновлення мови інтерфейсу"""
            credentials_file_text.label = self.t("credentials_file")
            mafiles_dir_text.label = self.t("mafiles_dir")
            output_dir_text.label = self.t("output_dir")
            login_column_field.label = self.t("login_column")
            password_column_field.label = self.t("password_column")
            start_row_field.label = self.t("start_row")
            
            files_dirs_title.value = self.t("files_dirs")
            column_settings_title.value = self.t("column_settings")
            settings_help_text.value = self.t("settings_help")
            apply_button.text = self.t("apply")
            convert_button.text = self.t("convert")
            logs_title.value = f"{self.t('logs')} {self.t('hover_to_view')}"
            select_button_1.text = self.t("select")
            select_button_2.text = self.t("select")
            select_button_3.text = self.t("select")
            subtitle_text.value = self.t("subtitle")
            
            page.update()
        
        def change_language(e):
            """Зміна мови"""
            self.current_lang = language_dropdown.value
            self.settings["language"] = self.current_lang
            self.settings_manager.save_settings(self.settings)
            update_ui_language()
        
        language_dropdown.on_change = change_language
        
        def apply_settings(e):
            """Застосування налаштувань"""
            try:
                login_col = int(login_column_field.value)
                password_col = int(password_column_field.value)
                start_row = int(start_row_field.value)
                
                self.converter.set_column_settings(login_col, password_col)
                self.converter.set_start_row(start_row)
                
                self.settings["login_column"] = login_col
                self.settings["password_column"] = password_col
                self.settings["start_row"] = start_row
                self.settings_manager.save_settings(self.settings)
                
                log_message(f"✓ {self.t('settings_applied')}")
                
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(self.t("settings_applied"), color="white"),
                    bgcolor="green",
                )
                page.snack_bar.open = True
                page.update()
                
            except Exception as ex:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"{self.t('error')}: {ex}", color="white"),
                    bgcolor="red",
                )
                page.snack_bar.open = True
                page.update()
        
        def pick_credentials_file(e: ft.FilePickerResultEvent):
            """Вибір файлу з логінами/паролями"""
            if e.files:
                file_path = e.files[0].path
                credentials_file_text.value = file_path
                self.settings["credentials_file"] = file_path
                self.settings_manager.save_settings(self.settings)
                apply_settings(None)
                page.update()
        
        def pick_mafiles_dir(e: ft.FilePickerResultEvent):
            """Вибір директорії з .maFile файлами"""
            if e.path:
                mafiles_dir_text.value = e.path
                self.settings["mafiles_dir"] = e.path
                self.settings_manager.save_settings(self.settings)
                page.update()
        
        def pick_output_dir(e: ft.FilePickerResultEvent):
            """Вибір вихідної директорії"""
            if e.path:
                output_dir_text.value = e.path
                self.settings["output_dir"] = e.path
                self.settings_manager.save_settings(self.settings)
                page.update()
        
        # File pickers
        credentials_file_picker = ft.FilePicker(on_result=pick_credentials_file)
        mafiles_dir_picker = ft.FilePicker(on_result=pick_mafiles_dir)
        output_dir_picker = ft.FilePicker(on_result=pick_output_dir)
        
        page.overlay.extend([credentials_file_picker, mafiles_dir_picker, output_dir_picker])
        
        def show_success_notification(copied_count: int, output_path: str):
            """Показати toast-сповіщення"""
            # Створюємо просте зелене сповіщення в правому нижньому куті
            notification = ft.Container(
                content=ft.Container(
                    content=ft.Row([
                        ft.Text("✅", size=35),
                        ft.Column([
                            ft.Text(self.t("notification_success"), size=24, weight="bold", color="white"),
                            ft.Text(self.t("notification_processed", count=copied_count), size=14, color="white"),
                        ], spacing=0),
                    ], spacing=15),
                    padding=20,
                    bgcolor="#4CAF50",
                    border_radius=10,
                ),
                right=20,
                bottom=20,
                animate_opacity=300,
            )
            
            # Додаємо в overlay
            page.overlay.append(notification)
            notification.opacity = 0
            page.update()
            
            # Анімація появи
            notification.opacity = 1
            page.update()
            
            # Автоматично ховаємо через 5 секунд
            def hide_notification():
                time.sleep(5)
                notification.opacity = 0
                page.update()
                time.sleep(0.3)
                page.overlay.remove(notification)
                page.update()
            
            threading.Thread(target=hide_notification, daemon=True).start()
        
        def show_success_dialog(copied_count: int, output_path: str):
            """Показати діалог успіху"""
            def close_dialog(e=None):
                dialog.open = False
                page.update()
            
            def open_folder(e):
                import subprocess
                try:
                    if os.name == 'nt':  # Windows
                        os.startfile(output_path)
                    elif os.name == 'posix':  # macOS/Linux
                        subprocess.Popen(['xdg-open', output_path])
                except:
                    pass
                close_dialog()
            
            dialog = ft.AlertDialog(
                modal=True,
                bgcolor="#2D2D2D",
                title=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text("✅", size=50),
                            ft.Text("УСПІХ!", size=32, weight="bold", color="#4CAF50"),
                        ], alignment="center"),
                        ft.Text(
                            "Конвертація завершена",
                            size=16,
                            color="white",
                            text_align="center",
                        ),
                    ], horizontal_alignment="center", spacing=10),
                    bgcolor="#1B5E20",
                    padding=20,
                    border_radius=10,
                ),
                content=ft.Container(
                    content=ft.Column([
                        ft.Container(height=20),
                        # Кількість файлів
                        ft.Container(
                            content=ft.Column([
                                ft.Text("📁 .maFile файлів", size=14, color="grey"),
                                ft.Text(f"{copied_count}", size=50, weight="bold", color="#2196F3"),
                            ], horizontal_alignment="center", spacing=5),
                            bgcolor="#0D47A1",
                            padding=20,
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        # accounts.txt
                        ft.Container(
                            content=ft.Row([
                                ft.Text("📄", size=30),
                                ft.Text("accounts.txt", size=18, weight="bold", color="#FF9800"),
                                ft.Text("✓", size=30, color="#4CAF50"),
                            ], alignment="center"),
                            bgcolor="#E65100",
                            padding=15,
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        ft.Divider(height=2, color="grey"),
                        ft.Container(height=10),
                        # Шлях
                        ft.Container(
                            content=ft.Column([
                                ft.Text("📂 Збережено в:", size=14, color="grey", weight="bold"),
                                ft.Container(height=5),
                                ft.Text(output_path, size=13, selectable=True, color="white"),
                            ], horizontal_alignment="start"),
                            bgcolor="#424242",
                            padding=15,
                            border_radius=10,
                        ),
                    ], spacing=0, horizontal_alignment="center"),
                    padding=20,
                    width=500,
                ),
                actions=[
                    ft.TextButton(
                        "📂 Відкрити папку",
                        on_click=open_folder,
                        style=ft.ButtonStyle(color="blue"),
                    ),
                    ft.ElevatedButton(
                        "OK",
                        on_click=close_dialog,
                        bgcolor="green",
                        color="white",
                    ),
                ],
                actions_alignment="spaceBetween",
            )
            
            page.dialog = dialog
            dialog.open = True
            page.update()
        
        def convert_files():
            """Основна логіка конвертації"""
            try:
                log_view.controls.clear()
                log_message(self.t("conversion_started"))
                page.update()
                
                log_message(f"{self.t('reading_file')}: {credentials_file_text.value}")
                credentials = self.converter.extract_credentials(credentials_file_text.value)
                log_message(self.t("found_credentials", count=len(credentials)))
                
                log_message(f"{self.t('processing_mafiles')}: {mafiles_dir_text.value}")
                copied_count = self.converter.process_mafiles(
                    credentials,
                    mafiles_dir_text.value,
                    output_dir_text.value
                )
                
                log_message(self.t("conversion_complete"))
                log_message(self.t("copied_files", count=copied_count))
                log_message(f"{self.t('saved_to')}: {output_dir_text.value}")
                
                # Повертаємо результат для показу в основному потоці
                return copied_count, output_dir_text.value
                
            except Exception as ex:
                log_message(f"{self.t('error_occurred')}: {ex}")
                
                # Показуємо діалог помилки
                error_dialog = ft.AlertDialog(
                    modal=True,
                    bgcolor="#1E1E1E",
                    title=ft.Row([
                        ft.Text("❌", size=40),
                        ft.Text(self.t("error"), size=24, weight="bold", color="red"),
                    ], alignment="center"),
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(str(ex), size=16, selectable=True),
                            ft.Container(height=10),
                            ft.Text("Перевірте логи для деталей", size=12, color="grey", italic=True),
                        ]),
                        padding=20,
                    ),
                    actions=[
                        ft.TextButton(
                            "Закрити",
                            on_click=lambda e: setattr(error_dialog, 'open', False) or page.update(),
                            style=ft.ButtonStyle(color="red"),
                        ),
                    ],
                    actions_alignment="end",
                )
                page.dialog = error_dialog
                error_dialog.open = True
                page.update()
        
        async def start_conversion(e):
            """Запуск процесу конвертації"""
            if not credentials_file_text.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(self.t("select_credentials"), color="white"),
                    bgcolor="red",
                )
                page.snack_bar.open = True
                page.update()
                return
            
            if not mafiles_dir_text.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(self.t("select_mafiles"), color="white"),
                    bgcolor="red",
                )
                page.snack_bar.open = True
                page.update()
                return
            
            if not output_dir_text.value:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(self.t("select_output"), color="white"),
                    bgcolor="red",
                )
                page.snack_bar.open = True
                page.update()
                return
            
            # Показуємо прогрес
            convert_button.disabled = True
            convert_button.text = "⏳ Обробка..."
            page.update()
            
            try:
                # Виконуємо конвертацію в окремому потоці але чекаємо результат
                loop = asyncio.get_event_loop()
                result = await loop.run_in_executor(None, convert_files)
                
                # Повертаємо кнопку в нормальний стан
                convert_button.disabled = False
                convert_button.text = self.t("convert")
                page.update()
                
                # Показуємо сповіщення якщо є результат
                if result:
                    copied_count, output_path = result
                    show_success_notification(copied_count, output_path)
                    
            except Exception as ex:
                convert_button.disabled = False
                convert_button.text = self.t("convert")
                page.update()
        
        # Кнопка конвертації
        convert_button = ft.ElevatedButton(
            self.t("convert"),
            on_click=start_conversion,
            bgcolor="#2196F3",
            color="white",
            height=56,
            width=180,
        )
        
        # Автозастосування налаштувань при запуску
        try:
            self.converter.set_column_settings(
                int(login_column_field.value),
                int(password_column_field.value)
            )
            self.converter.set_start_row(int(start_row_field.value))
        except:
            pass
        
        # Текстові елементи для оновлення мови
        subtitle_text = ft.Text(
            self.t("subtitle"),
            size=14,
        )
        
        files_dirs_title = ft.Text(self.t("files_dirs"), size=18, weight="bold")
        column_settings_title = ft.Text(self.t("column_settings"), size=18, weight="bold")
        settings_help_text = ft.Text(
            self.t("settings_help"),
            size=11,
            italic=True,
        )
        
        select_button_1 = ft.ElevatedButton(
            self.t("select"),
            on_click=lambda _: credentials_file_picker.pick_files(
                allowed_extensions=["xlsx", "xls"],
                dialog_title=self.t("select_credentials")
            ),
        )
        
        select_button_2 = ft.ElevatedButton(
            self.t("select"),
            on_click=lambda _: mafiles_dir_picker.get_directory_path(
                dialog_title=self.t("select_mafiles")
            ),
        )
        
        select_button_3 = ft.ElevatedButton(
            self.t("select"),
            on_click=lambda _: output_dir_picker.get_directory_path(
                dialog_title=self.t("select_output")
            ),
        )
        
        apply_button = ft.ElevatedButton(
            self.t("apply"),
            on_click=apply_settings,
        )
        
        logs_title = ft.Text(
            f"{self.t('logs')} {self.t('hover_to_view')}",
            size=16,
            weight="bold",
        )
        
        # Card для логів (створюємо окремо щоб мати посилання)
        logs_card = ft.Card(
            content=ft.Container(
                content=log_container,
                padding=15,
            ),
            visible=False,
        )
        
        # Функція для переключення логів
        def toggle_logs_func():
            logs_card.visible = not logs_card.visible
            page.update()
        
        # Компоненти UI
        main_column = ft.Column([
            # Заголовок з мовою та темою
            ft.Row([
                ft.Column([
                    ft.Text(
                        self.t("title"),
                        size=32,
                        weight="bold",
                        color="blue",
                    ),
                    subtitle_text,
                ], expand=True),
                ft.Row([
                    theme_icon_button,
                    ft.Column([
                        ft.Text(self.t("language"), size=12),
                        language_dropdown,
                    ]),
                ], spacing=10),
            ]),
            
            ft.Divider(),
                    
                    # Вибір файлів
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                files_dirs_title,
                                ft.Row([
                                    credentials_file_text,
                                    select_button_1,
                                ]),
                                ft.Row([
                                    mafiles_dir_text,
                                    select_button_2,
                                ]),
                                ft.Row([
                                    output_dir_text,
                                    select_button_3,
                                ]),
                            ]),
                            padding=15,
                        ),
                    ),
                    
                    # Налаштування стовпців
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                column_settings_title,
                                ft.Row([
                                    login_column_field,
                                    password_column_field,
                                    start_row_field,
                                    apply_button,
                                    convert_button,
                                ], wrap=True, alignment="center", spacing=10),
                                settings_help_text,
                            ]),
                            padding=15,
                        ),
                    ),
                    
                    # Логи (ховаються/показуються)
                    ft.Container(
                        content=logs_title,
                        on_click=lambda e: toggle_logs_func(),
                        padding=10,
                    ),
            logs_card,
        ], 
        spacing=10,
        scroll="auto",
        )
        
        page.add(main_column)
    
    def run(self):
        """Запуск GUI"""
        ft.app(target=self.main)

def main():
    """Головна функція"""
    try:
        app = MaFilesConverterGUI()
        app.run()
    except Exception as e:
        print(f"Критична помилка: {e}")
        raise

if __name__ == "__main__":
    main()
