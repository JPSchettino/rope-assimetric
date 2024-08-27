


## Reproduction



```python
git clone https://github.com/JPSchettino/rope-assimetric.git
cd rope-assimetric
pip install -e .
```

### Training

To train the models, run `accelerate config` and enable DeepSpeed acceleration. `deepspeed/zero3.json` was the configuration file used for training.

```sh
# ./train.sh
```

### Evaluation

To reproduce the evaluations, install [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) with `pip install git+https://github.com/EleutherAI/lm-evaluation-harness` and then run the two provided scripts.

```sh
# ./eval.sh
# ./eval-harness.sh
```

### Citation


