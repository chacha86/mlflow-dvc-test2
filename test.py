import mlflow	
import mlflow.sklearn

data_url = dvc.api.get_url(
    path="data.txt",
    repo='https://github.com/iterative/dataset-registry',
    rev=""
)
mlflow.log_param("alpha", 1.0)

