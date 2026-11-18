# R229 source and input findings

取得日: 2026-11-15 JST。以下は保存原文と固定コードに基づく。推論結果の品質判定は別記する。

- [一次] 11月15日はPHerc0211 First Lettersの公式受賞発表日。対象のsoft-lossリリース公開は2026-10-28T21:18:39Z。0211を未受賞対象には数えない。この受賞は他者の成果。
- [一次] Git固定 `235e3be8a06749344862c89a1e52c81d90b15e0e`。公式 `model.py` SHA `efbb390b6208c480fa8e8681137690b7df897c3e406956b9e804fa66645316d7`、`inference.py` SHA `09752cf7aa0b682c6ca9a46e41bf1f9f279e30d74d35eaab8fc0311504223ec0`。
- [一次] リリースassetは893,443,724 B、SHA `96b326286e38de99047f7cab36170c53749a18d5f43e5fde0c7c20f2980b0e90`。全文取得後のハッシュ照合とCPU strict loadで214テンソル・223,355,921パラメータを確認。キャッシュ本体は親の許可で解放したが、出典・ヘッダ・照合原票・CPU参照を保持。

## 来歴と比較の意味

作者の固定記録は、814/841/9Bの疎ラベルからscratchで9epoch・74,250更新、他巻の12groupへ30,000更新の継続学習と毎batchの元巻replay、続いてsoft-loss3,000更新のEMAという鎖を記載する。新たに訓練を再現したのではなく、公開記録を確認した。[一次: sources/README.md、sources/studio-multiscroll-cpt-20261023/README.md、sources/studio-softloss-20261023/README.md]

継続段階にはExpanded9の69行とReader v2/v3の47面が含まれる。Reader由来は0139、0500P2、0343P、0172。0343Pは5行で、公開manifestのCTは `PHerc0343P/.../8.64um-1.2m-116keV-volume-20250521134555.zarr`。今回の既知対照は `PHerc0343/volumes/20250521140437-8.640um-1.2m-116keV-masked.zarr` の別キー。物理partの関係や全ラベル座標との重複までは検証していない。[一次: mixture.json、reader-labels-manifest.csv、R173 ct-result.json]

作者は0211画素を訓練しないとするが、0211の評価値を見て継続学習やlossを選んでいる。ラベル作成時にStudio系予測を見た可能性もsoft-loss文書が明記する。公称APを独立した盲検性能として扱わない。またReaderラベルの共有があるため、異なる構造の応答を得ても、ラベルまで独立した証拠とは呼ばない。

既済seed42/dense-nativeは公式 `vesuvius_unet_3d_stem_2d`、17層、robust-MADの系列。dense-nativeの固定checkpoint SHAは `d3d95dc41dcb24ed76b84b5e12ca5dae25d7fb34edf1dfbb93e0186f91e6fc6d`、モデル34,546,498パラメータ。Reader V3も同じモデル型を用いるが384²の文脈と別重み（SHA `ea405417450abd8ace1b8ff79ebce3adb646c5e48ab95da46844d77efe984d8a`）。HecateはResNet152 3Dと深さattention、16×64²、uint8/255、SHA `809f4f10f7cb7afa19b4bee0f7d2ab31edd7e11b664f9f210cc9c17f22fcfe5d`。今回の全3D residual U-Net・GroupNorm・16層global softmax pool・223Mパラメータは、これら既済重みの別名ではない。[一次: R172 source/preflight、R189、R222 cpu/model.json、本件固定model.py/CPU strict]

## 公式入力契約

- uint8 `[16,H,W]`。nativeの学習例には8.64、9.362、9.366 µmがあり、9.6 µmへ必ず再標本化するモデルではない。
- 提供31層面の23..8という順は中心15に対して+8..−7。本件はR222の法線を維持し、保存された昇順−8..+8の17層からstorage indices16..1を採る。異なる面の法線の向きまで普遍的に証明したわけではない。別の深さ/順序は試さない。
- 入力128²、中央96²を使用、halo各16。公式最終レシピはstride64とpixel-centred Hann。Hannに床値なし。全面の開始位置は0からstride刻みと末端位置の追加。本件の主域に寄与する96位置を全面基準で列挙し、必要入力は全て保存CT内にあるためreflect paddingは使わない。
- `clip(raw,0,200)/255` のfloat32。robust-MADや個別contrast補正はしない。モデルは深さを学習softmaxでpoolした2D logitsを返す。中央96²にsigmoidをかけてからHann加重平均する。過去のstride48/logits-blend実験表と混同しない。
- 最後に全16層0の画素を0へ戻す。空のpatchをスキップする規則ではない。FP32/batch1/TF32off、compile/TTAなしで固定。

## ライセンスと取得

固定READMEの宣言はコードMIT、重み・訓練データ・提出出力CC BY-NC 4.0、第三者ReaderラベルはMIT。訓練データ本体は取得していない。依存のLinux safetensors0.8.0 wheelはPyPIメタデータのSHA `fd6f3f93c9a0a7cc2788ee63fb763353d4bd2e89b0751bc78fcf7dda00bea774` を照合し、専用Podだけにoffline展開する。

GitHub connectorは親の独立確認と単一ファイルの読取りに使用。根拠の固定にはGitHub API、raw.githubusercontent.com、Hugging Faceの固定revision、公式発表を直接HTTP取得し、bytes/SHA/URLを `acquisition-sources.jsonl` へ残した。web openはSubstackで失敗したが直接HTTP200で原文を保存できた。親のconnector保存物は担当の受信量へ二重計上しない。

主な公開出典: https://scrollprize.substack.com/p/first-letters-emerge-from-pherc-211 · https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt/tree/235e3be8a06749344862c89a1e52c81d90b15e0e · https://github.com/priyankaranke/vesuvius-studio-multiscroll-cpt/releases/tag/studio-softloss-20261023
