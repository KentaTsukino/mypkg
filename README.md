# mypkg

![test](https://github.com/KentaTsukino/mypkg/actions/workflows/test.yml/badge.svg)

# 本リポジトリの概要
このリポジトリは千葉工業大学先進工学部未来ロボティクス学科4Semesterの講義で扱われているROS2のパッケージです。
## 本リポジトリの使用方法
- terminalで以下のものを実行
```
$ git clone https://github.com/KentaTsukino/mypkg.git
```

# パッケージ内容
- talker.py
  - countupというトピックを通じて、メッセージを送信する。メッセージの型は16ビットの符号付き整数。
- litener.py
  - countupというトピックからメッセージを受信する。またtalker.pyから送信したものをターミナルに出力する。
- talk_listen.launch.py
  - 本リポジトリに含まれている2つのノードを一度に立ち上げることが出来る。

# 実行方法(run)
1. terminalで以下のコマンドを実行
```
$ ros2 run mypkg talker
```
2. 新しいterminalを起動し、以下のコマンドを実行
```
$ ros2 run mypkg listener
```
3. `Ctrl + \`で終了

## 実行結果
- 実行方法の2で新たに起動したterminalに以下のようなものが出力される
```
[INFO] [1672913822.655170100] [listener]: Listen: 24
[INFO] [1672913823.146982000] [listener]: Listen: 25
[INFO] [1672913823.645814200] [listener]: Listen: 26
[INFO] [1672913824.146852200] [listener]: Listen: 27
[INFO] [1672913824.646694000] [listener]: Listen: 28
[INFO] [1672913825.146771900] [listener]: Listen: 29
[INFO] [1672913825.646214500] [listener]: Listen: 30
[INFO] [1672913826.146734300] [listener]: Listen: 31
[INFO] [1672913826.646048200] [listener]: Listen: 32
[INFO] [1672913827.146795800] [listener]: Listen: 33
[INFO] [1672913827.646769600] [listener]: Listen: 34
[INFO] [1672913828.146660700] [listener]: Listen: 35
[INFO] [1672913828.646931100] [listener]: Listen: 36
[INFO] [1672913829.146775300] [listener]: Listen: 37
[INFO] [1672913829.646912200] [listener]: Listen: 38
[INFO] [1672913830.146936100] [listener]: Listen: 39
[INFO] [1672913830.646572800] [listener]: Listen: 40
[INFO] [1672913831.146958800] [listener]: Listen: 41
[INFO] [1672913831.646947800] [listener]: Listen: 42
[INFO] [1672913832.146798500] [listener]: Listen: 43
```

# 実行方法(launch)
1. terminalで以下のコマンドを実行
```
$ros2 launch mypkg talk_listen.launch.py
```
2. `Ctrl + \`で終了

## 実行結果
- 以下のようなものが出力される
```
[INFO] [launch]: All log files can be found below /home/kentatuskino/.ros/log/2023-01-05-20-11-47-136199-LAPTOP-STQ4IF8A-3715
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [3717]
[INFO] [listener-2]: process started with pid [3719]
[listener-2] [INFO] [1672917107.953255500] [listener]: Listen: 0
[listener-2] [INFO] [1672917108.444751000] [listener]: Listen: 1
[listener-2] [INFO] [1672917108.944555000] [listener]: Listen: 2
[listener-2] [INFO] [1672917109.443778700] [listener]: Listen: 3
[listener-2] [INFO] [1672917109.945518800] [listener]: Listen: 4
[listener-2] [INFO] [1672917110.445268900] [listener]: Listen: 5
[listener-2] [INFO] [1672917110.945238400] [listener]: Listen: 6
[listener-2] [INFO] [1672917111.444510000] [listener]: Listen: 7
[listener-2] [INFO] [1672917111.945305000] [listener]: Listen: 8
[listener-2] [INFO] [1672917112.444658500] [listener]: Listen: 9
[listener-2] [INFO] [1672917112.943941700] [listener]: Listen: 10
[listener-2] [INFO] [1672917113.444734600] [listener]: Listen: 11
```

# 動作確認済み環境
- ROS
  - ROS2 foxy
  - ROS2 Humble
- OS
  - Ubuntu 20.04 LTS

# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです
  -  [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
- © 2022 Kenta Tsukino
