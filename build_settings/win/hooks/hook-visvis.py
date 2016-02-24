from PyInstaller.utils.hooks import collect_submodules, collect_data_files

import visvis
import visvis.core
import visvis.processing
import visvis.functions

hiddenimports = (collect_submodules('visvis.core') +
                 collect_submodules('visvis.processing') +
                 collect_submodules('visvis.functions'))

datas = collect_data_files('visvis', include_py_files=True)
