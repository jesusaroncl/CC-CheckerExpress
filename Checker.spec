# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['Checker.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\gonza\\OneDrive\\Documentos\\GitHub\\Repository\\dist\\CheckerProtect.py', '_obf')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Checker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='CheckerExpress.ico',
    manifest='CheckerExpress.manifest',
)