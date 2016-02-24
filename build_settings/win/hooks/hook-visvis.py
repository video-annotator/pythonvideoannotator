from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from visvis.freezeHelp import getIncludes

import visvis
import visvis.core
import visvis.processing

#modules = getIncludes('qt4');[collect_submodules(module) for module in modules]
hiddenimports = tuple([collect_submodules('visvis.core')+collect_submodules('visvis.processing')])

datas = collect_data_files('visvis', include_py_files=True)
