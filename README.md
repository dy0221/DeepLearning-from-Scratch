# DeepLearning-from-Scratch

## conda 가상환경으로 code runner를 실행하는 방법

### https://github.com/WegraLee/deep-learning-from-scratch/blob/master/dataset/mnist.py

왼쪽 위에 File에 Save Workspace As를 눌러서 .code-workspace파일을 만든다.

그 후 setting을 고친다. [Stackoverflow juso](https://stackoverflow.com/questions/72556952/code-runner-in-vs-code-not-running-conda-python)

```json
{
    "folders": [
        {
            "path": "."
        }
    ],
    "settings": {
        "code-runner.executorMap": {
            "python": "C:\\Users\\wjm25\\anaconda3\\envs\\DL\\python.exe"
        },
        "python.defaultInterpreterPath": "C:\\Users\\wjm25\\anaconda3\\envs\\DL\\python.exe"
    }
}