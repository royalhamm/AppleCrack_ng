import os, sys, importlib, pkgutil

project_root = '/home/fsaociety/Projects/applecrack_ng'
sys.path.insert(0, project_root)

errors = []
def import_all_submodules(package_name):
    try:
        package = importlib.import_module(package_name)
    except Exception as e:
        print(f"FAILED to import {package_name}: {e}")
        return

    print(f"SUCCESS importing {package_name}")

    if hasattr(package, '__path__'):
        for _, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            if module_name == "applecrack_ng.__main__": continue
            try:
                importlib.import_module(module_name)
                print(f"SUCCESS importing {module_name}")
            except Exception as e:
                print(f"FAILED to import {module_name}: {e}")
                errors.append(module_name)

import_all_submodules('applecrack_ng')
if errors:
    sys.exit(1)
else:
    print("ALL IMPORTS SUCCESSFUL")
