# -*- mode: python -*-

block_cipher = None

add_files = [('clienticon.ico', '.'), ('fileformat.gif', '.')]

a = Analysis(['modisApp.py'],
             pathex=['C:\\Users\\AKO NA LNG\\Desktop\\Esquivel Files\\Final Thesis\\ModisDataRenderer'],
             binaries=None,
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='modisApp',
          debug=True,
          strip=False,
          upx=True,
          console=True , icon='clienticon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='modisApp')
