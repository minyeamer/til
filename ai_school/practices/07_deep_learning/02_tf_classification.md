# TF Classification

---

```python
from tensorflow.keras import datasets

(train_data, train_label), (test_data, test_label) = datasets.mnist.load_data()
```

- Keras에서 MNIST 데이터셋 가져오기

```python
import matplotlib.pyplot as plt

plt.imshow(train_data[0], cmap='gray')
```

- 첫번째 데이터에 들어있는 그림

이미지 데이터는 standard scaler 적용할 필요 없음

```python
from tensorflow.keras import utils

train_label = utils.to_categorical(train_label) # 0~9 -> one-hot vector
test_label = utils.to_categorical(test_label)
```

- keras 원핫인코딩


---

5.
학습이 끝나면 dropout 걷어내야됨
미리 dropout을 설정하면 걷어내기 어렵기 때문에 keep_prob를 설정


