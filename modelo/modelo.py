import xgboost as xgb
import joblib
from pathlib import Path

__version__ = "1.0.1"
BASE_DIR = Path(__file__).resolve(strict=True).parent
#modelo = xgb.Booster()
#modelo.load_model(f"{BASE_DIR}/trained_xgboost-{__version__}.model")
joblib_in = open(f"{BASE_DIR}/trained_xgboost-{__version__}.joblib","rb")
modelo = joblib.load(joblib_in)
features = modelo.get_booster().feature_names
feature_types = modelo.get_booster().feature_types
categorias = [
    "No Abandona - Es probable que el estudiante continue con sus estudios",
    "Abandona - Es probable que el estudiante abandone sus estudios",
] 



