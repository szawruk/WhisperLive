# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['run_server.py'],
    pathex=[],
    binaries=[],
       datas=[ 
        ('faster_whisper', './faster_whisper'),
        ('onnxruntime', './onnxruntime')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=1,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # Important: set to True for onedir
    name='napisowa_note_parser',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='logo_square_white.ico',
    contents_directory="napisowa_note_parser_lib"
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='napisowa_note_parser'
)
