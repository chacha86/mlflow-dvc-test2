import mlflow	
import mlflow.sklearn

data_url = dvc.api.get_url(
    path="data.txt",
    repo='https://github.com/chacha86/mlflow-dvc-test2.git',
    rev="68be4afcc135f1b4e108d5beef4f8f41357cf102"
)
mlflow.log_param("alpha", 1.0)


