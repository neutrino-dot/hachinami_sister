# yanami_project(8bit-music-lib追加機能)

``` bash
#使用時、必ずm8のexperimentを用いること
git clone -b experiment https://github.com/neutrino-dot/8bit-music-lib
cd 8bit-music-lib
pip install .
```
母音再生プログラム完了済み

①母音のフォルマントの決定
* 平均よりも少し高めに
* 高音域に500Hzの帯域で音追加

②子音の作成
* 候補
  * numpy配列で振幅値をすべて入力
  * 既存の矩形波にフィルタをかけて近づける

③子音と母音の結合
* 結合前に子音と母音の間にフェードをnp.linspaceでかける
