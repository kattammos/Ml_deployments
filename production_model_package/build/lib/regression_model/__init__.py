import sys

sys.path.append(C:\\Users\\User\\OneDrive\\Документы\\KV_DW_JL_5\\Ml_deployments\\production_model_package)

import logging

from regression_model.config.core import PACHAGE_ROOT, config

logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler()) #разработчик

with open(PACHAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()