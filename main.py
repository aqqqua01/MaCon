#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MaCon - Entry point for Flet build
"""

from mafiles_converter_flet import MaFilesConverterGUI

def main():
    """Головна функція"""
    app = MaFilesConverterGUI()
    app.run()

if __name__ == "__main__":
    main()

