# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['C:\\Users\\danil\\Desktop\\projeto\\Individual-DiffAlgorithm'],
             binaries=[],
             datas=[('C:\\Program Files (x86)\\Python38-32\\lib\\site-packages\\eel\\eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['astroid', 'auto-py-to-exe', 'cffi', 'colorama', 'Command', 'cycler', 'isort', 'kiwisolver', 'lazy-object-proxy', 'matplotlib', 'mccabe', 'numpy', 'pandas', 'pefile', 'pycparser', 'pygame', 'pylint', 'pyparsing', 'python-dateutil', 'pytz', 'pywin32-ctypes', 'setuptools', 'six', 'wrapt'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
