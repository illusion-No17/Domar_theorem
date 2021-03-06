# Domar's theorem（ドーマー定理）

政府債務残高対ＧＤＰ比は，ある条件「Ｘ」のもとでは無限大に発散しない．

# 1. ある条件「X」の一例
名目成長率 > 政府債務の名目利子率かつ，プライマリーバランス赤字の対ＧＤＰ比が一定であるならば，
政府債務残高対ＧＤＰ比は無限大に発散しない．

※政府のプライマリーバランスは均衡しなくても良い（黒字化しなくても良い）．


# 2. ドーマーの定理の設定

## 2.1. 変数一覧

| 項目 | 概要 |
|:---|:---|
|D(t) |時点tにおける政府債務残高 |
|G(t) |時点tにおける政府支出 |
|T(t) |時点tにおける租税歳入 |
|Y(t) |時点tにおける名目GDP |
|d(t) = D(t)/Y(t) |時点tにおける政府債務の対名目ＧＤＰ比 |
|PB(t) = T(t) - G(t) |時点tにおけるプライマリーバランス |
|p(t) = PB(t)/Y(t) |時点tにおけるプライマリーバランスの対名目ＧＤＰ比 |
|r(t)|時点tにおける政府債務の名目利子率 |
|n(t) |時点tにおける名目成長率 |

※統合政府（政府と中央銀行の統合政府）は考慮しないものとする（より厳しい条件とする）．

## 2.2. 式展開

政府債務の名目利子率をr(t)とすると，政府債務残高D(t)の推移は以下の等式で与えられる．

<img src="resources/fig1.png" width="500">

式(1)は，現在の政府債務残高D(t)に利払いr(t)D(t)を足して政府のプライマリーバランスPB(t)を引いたものが，
次年度の政府債務残高D(t+1)になるという意味である．

一方で，n(t)を名目成長率とすると，名目ＧＤＰ成長は以下の等式で与えられる．

<img src="resources/fig2.png" width="500">

式(1)の両辺をY(t+1)で割ると，名目ＧＤＰ成長の式(2)より，

<img src="resources/fig3.png" width="500">

となる．
γ(t) = ( 1 + r(t) ) /( 1 + n(t) ) とし，
m(t) = 1  /( 1 + n(t) )とすると，式(3)は，

<img src="resources/fig4.png" width="500">

となる．

ここで，t = 0，1，2，3，・・・と順番に見ていくと，

<img src="resources/fig5.png" width="550">

のようになり，これを繰り返すと，時点tにおけるd(t)は，

<img src="resources/fig6.png" width="600">

となる．ただし，d(0) は，政府債務対ＧＤＰ比の初期値である．

## 2.3. 仮定
下記の３つを仮定する．

- 名目成長率 n(t) > 政府債務の名目利子率 r(t)である．

- 名目成長率 n(t) > 0 である．
- 政府プライマリーバランスの赤字の対GDP比 p(t) が一定である．

まず，n(t) > r(t) および n(t) > 0 より，
γ(t) = ( 1 + r(t) ) /( 1 + n(t) ) は
0 < γ(t) < 1 となる．

n(t) > 0 より，
m(t) = 1  /( 1 + n(t) ) は
0 < m(t) < 1 となる．

政府のプライマリーバランスの対ＧＤＰ比を赤字の定数値， p(t) ≒ - p_0,　p_0 > 0  とすると，式(8)は

<img src="resources/fig7.png" width="600">

となる．

## 2.4.   d(t) の t -> ∞ の極限
まず，以下の極限

<img src="resources/fig8.png" width="300">

について考える．

0 < γ(t) < 1により，式(10)は0に収束する．

次に，以下の極限

<img src="resources/fig9.png" width="400">

について考える．

𝑡=1のとき， 𝑚 (0) 𝑝_0

𝑡=2のとき，𝛾(1)𝑚 (0) 𝑝_0 + 𝑚 (1) 𝑝_0

𝑡=3のとき，𝛾(2)𝛾(1)𝑚 (0) 𝑝_0 + 𝛾(2)𝑚 (1) 𝑝_0 + 𝑚 (2) 𝑝_0

：

：

のようになるため，
0 < 𝛾_𝑎 ≤ 𝛾(𝑡) ≤ 𝛾_𝑏 < 1 となる定数 𝛾_𝑎 及び 𝛾_𝑏 により，

<img src="resources/fig10.png" width="700">

となる．

ここで，式(12)の右端の

<img src="resources/fig11.png" width="370">

について考える．

0 < 𝑚 (𝑡)< 1 より，
0 < 𝑚(𝑡) ≤ 𝑚_𝑏 < 1となる定数 𝑚_𝑏 があるとすると，

<img src="resources/fig12.png" width="420">

となる．このとき，式(14)の右辺の極限

<img src="resources/fig13.png" width="320">

は定数 

<img src="resources/fig14.png" width="100">

に収束する．

同様にして，式(12)の左端の

<img src="resources/fig15.png" width="370">

について考える．

0 < 𝑚 (𝑡) < 1 より，
0 < 𝑚_a ≤ 𝑚(𝑡) < 1となる定数 𝑚_a があるとすると，

<img src="resources/fig16.png" width="420">

となる．このとき，式(17)の左辺の極限

<img src="resources/fig17.png" width="350">

は定数 

<img src="resources/fig18.png" width="100">

に収束する．

したがって，

<img src="resources/fig19.png" width="900">

により，

<img src="resources/fig20.png" width="400">

となるので，d(t)は無限大には発散しない（上記範囲内での振動はするかもしれない）．

# 3. シミュレーション

## 3.1. 環境構築
### 3.1.1. Ubuntuの場合

```
$ sudo apt-get update
$ sudo apt-get install -y git
$ sudo apt-get install -y python3-dev
$ sudo apt-get install -y python3-pip 

$ pip3 install numpy
$ pip3 install matplotlib
```

### 3.1.2. Windowsの場合
```
準備中
```
## 3.2. シミュレーションの実行
Ubuntuなら端末，windowsならWindows PowerShellを開いて以下を実行する．
```
$ git clone https://github.com/illusion-No17/Domar_theorem.git
$ cd Domar_theorem 
$ cd python
$ python simulation.py
```

シミュレーションでは，政府債務の名目利子率と名目成長率は
一定の値としている．

政府債務の名目利子率 r_0 と名目成長率 n_0 の値を下表に示す．

| 項目 | 値 |
|:---|:---|
|r_0 | 0.01 |
|n_0 | 0.04 |

変数の初期値を下表に示す．

| 変数 | 初期値  |補足|
|:---|:---|:---|
|D(0) |1100 兆円 ||
|Y(0) |550 兆円 ||
|d(0) | 2.0 | d(0) = D(0)/Y(0) 
|PB(0)| - 80 兆円 | PB(t+1) = (1 + n_0) PB(t) に従ってPBの赤字を増やす． |


政府債務の対ＧＤＰ比d(t)の推移を下図に示す．

<img src="resources/simulation.png" width="600">

政府債務の対ＧＤＰ比d(t)が定数値に収束していることがわかる．