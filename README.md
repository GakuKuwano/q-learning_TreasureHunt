# q-learning_TreasureHunt
# Q学習 　*〜宝探し〜*
確率ロボティクスの講義で作成した強化学習（Q学習）による宝探し

## 概要
エージェントが迷路の中を探索して宝物までの最適な経路を見つける．  
- **状態**  
エージェントの位置：2次元
- **行動**  
上，下，左，右：4次元
- **報酬**  
宝が見つかったら，+100を与える  
それ以外は，ペナルティとして毎ステップ-1を与える
- **終了条件**  
宝が見つかる or 最大ステップ数(max_step)試行する  
（終了条件が成立すると1episodeが終了する）

## シミュレーション環境
12×12マスのマップの中で行う  

### シミュレーションの見方
- 青色のマス： スタート位置
- 黒色のマス： 壁
- 赤色の丸　： 現在のエージェントの位置
- 黄色の星　： 宝物（ゴール）
  
![Screenshot from 2022-01-07 01-34-15](https://user-images.githubusercontent.com/39427885/148420344-31e1a48e-0ddc-4d5f-a089-6ff9702de29e.png)

## インストールが必要なライブラリ
- gym
- numpy
- matplotlib

## 実行方法
```bash
$ git clone git@github.com:GakuKuwano/q-learning_TreasureHunt.git
$ cd q-learning_TreasureHunt
$ python train.py
```
Jupyter Notebookの場合
```bash
$ git clone git@github.com:GakuKuwano/q-learning_TreasureHunt.git
$ cd q-learning_TreasureHunt/jupyter
Jupyter Notebookを起動して，train.ipynbを実行する
```

## DEMO
time_intervalの値を変更することでシミュレーションを可視化する回数を変更できます．

### time_interval = 100 の場合

https://user-images.githubusercontent.com/39427885/148424777-7f6ee6dc-6739-4f98-b085-a02468944b73.mp4

