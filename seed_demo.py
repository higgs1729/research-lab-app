"""Create a self-contained, synthetic scroll-flattening research example."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from tools.lab import Lab

DEMO_ROOT = Path(__file__).resolve().parent / "projects" / "demo"


def signed_area(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) / 2


def measurements():
    """Two triangles sharing a diagonal, with one free vertex repositioned."""
    faces = [(0, 1, 2), (0, 2, 3)]
    before = [(0, 0), (1, 0), (1, 1), (1, 0)]
    after = [(0, 0), (1, 0), (1, 1), (0, 1)]
    result = {"faces": faces, "before_uv": before, "after_uv": after}
    for name, points in (("before", before), ("after", after)):
        areas = [signed_area(*(points[i] for i in face)) for face in faces]
        result[name] = {"signed_areas": areas, "inverted": sum(a < 0 for a in areas),
                        "degenerate": sum(a == 0 for a in areas)}
    result["fixed_vertices_unchanged"] = before[:3] == after[:3]
    return result


def seed_demo(root=DEMO_ROOT):
    root = Path(root).resolve()
    marker = root / "runtime" / "demo-seeded.json"
    if marker.is_file():
        if not (root / "runtime" / "lab.sqlite3").is_file():
            raise ValueError("デモのDBがありません。別の空フォルダを --root に指定してください。")
        return root
    if root.exists() and any(root.iterdir()):
        raise ValueError("デモは空のフォルダに作成してください。既存データは上書きしません。")
    evidence = root / "evidence"
    evidence.mkdir(parents=True, exist_ok=True)
    result = measurements()
    (evidence / "01-plan.txt").write_text(
        "教材用の研究計画：巻物表面の平坦化\n"
        "Vesuvius Challengeでは、巻物の3次元表面を2次元へ対応させる処理が研究対象になる。\n"
        "このデモは実CTデータ・文字発見・受賞成果を含まない。2枚の三角形の合成例のみ。\n"
        "問い：固定した3頂点を動かさず、自由頂点の移動で反転面を除けるか。\n"
        "評価：符号つき面積、反転数、縮退数、固定頂点の不変性。\n"
        "未確認：大規模メッシュ、周辺面との重なり、面積・角度の歪み、読字品質。\n",
        encoding="utf-8")
    (evidence / "02-measurements.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    before, after = result["before"], result["after"]
    (evidence / "03-verification.txt").write_text(
        "教材用検証：2次元三角形の外積を2で割り、面の向きと縮退を確認。\n"
        f"移動前の符号つき面積: {before['signed_areas']}\n"
        f"移動後の符号つき面積: {after['signed_areas']}\n"
        f"反転面: {before['inverted']} → {after['inverted']}\n"
        f"縮退面: {before['degenerate']} → {after['degenerate']}\n"
        f"固定頂点0,1,2が不変: {result['fixed_vertices_unchanged']}\n"
        "手計算：面(0,2,3)の外積は移動前-1、移動後+1。\n"
        "これは独立した研究者による実データの検証ではなく、教材の算術確認である。\n"
        "反転0だけでは全体の品質を保証しない。周辺面の重なりと歪みは次の評価項目。\n",
        encoding="utf-8")
    (evidence / "04-resources.txt").write_text(
        "資源記録（教材）\n外部計算の利用なし。GPUなし。追加支出0 JPY。\n"
        "計算はseed_demo.py内の2面の外積のみ。所要時間と本人の対応時間は未計測。\n"
        "次の試行の投入目安：ローカルCPUで周辺面の交差を調べる。\n"
        "実データへの適用や大きな計算への移行前に、比較条件と停止条件を決め直す。\n",
        encoding="utf-8")
    (root / "PROJECT.txt").write_text(
        "巻物平坦化の研究管理デモ\n生成: python seed_demo.py\n"
        "全て教材用の合成数値例。個人情報や実運用の記録は含まない。\n"
        "再計算: python -m unittest tests.test_demo\n"
        "再起動でデータは初期化されない。初期状態を試す場合は別の空フォルダを指定する。\n",
        encoding="utf-8")
    lab = Lab(root)
    try:
        lab.activate("flattening-lead", "local")
        entries = [
            {"kind": "decision", "claim_status": "hypothesis", "summary": "巻物平坦化の最小例で、固定頂点を保った反転除去を調べる。実データへの有効性は未確認。", "evidence": ["evidence/01-plan.txt"]},
            {"kind": "experiment", "claim_status": "observed", "summary": "2面の合成例で自由頂点を移動。反転1→0、縮退0、固定3頂点は不変。", "evidence": ["evidence/02-measurements.json"]},
            {"kind": "verification", "claim_status": "verified", "summary": "外積の手計算と照合し、最小例の反転数を確認。全体の重なり・歪みは未評価。", "evidence": ["evidence/02-measurements.json", "evidence/03-verification.txt"]},
            {"kind": "cost", "claim_status": "observed", "summary": "ローカルCPUの教材計算のみ。追加支出0。次回の投入と停止条件は実データへ進む前に見直す。", "evidence": ["evidence/04-resources.txt"], "resources": {"cost": 0, "currency": "JPY", "compute": "ローカルCPU / 外部ジョブなし / 所要時間は未計測"}},
        ]
        for entry in entries:
            lab.record(entry)
        proposals = [
            {"problem": "反転数だけでは周辺面との重なりを見落とす。", "change": "周辺三角形との交差判定を次の小試験に追加する。", "benefit": "反転除去と全体品質を混同せずに採用判断できる。", "cost": "ローカルCPUの小試験と比較記録。", "evidence": ["evidence/03-verification.txt"]},
            {"problem": "結果の要約だけでは反転1→0の根拠を追えない。", "change": "移動前後のUV座標と符号つき面積を一緒に保存する。", "benefit": "外積による再計算ができる。", "cost": "数値JSONを1ファイル保存する。", "evidence": ["evidence/02-measurements.json"]},
            {"problem": "最小例では大規模メッシュ上の効果が分からない。", "change": "実データの大きな領域を使って追試する。", "benefit": "実用上の評価へ近づく可能性がある。", "cost": "データ準備と比較条件の設定が必要。", "evidence": ["evidence/01-plan.txt", "evidence/04-resources.txt"]},
            {"problem": "反転0をそのまま読字品質の改善と主張しかねない。", "change": "反転0だけを根拠に、実巻物の読字改善として成果化する。", "benefit": "成果説明を短くできる可能性。", "cost": "未検証の主張をする危険がある。", "evidence": ["evidence/03-verification.txt"]},
        ]
        ids = [lab.propose(p)["id"] for p in proposals]
        lab.delivered(ids[1], "flattening-lead", "local")
        lab.decide(ids[1], "accept", "小さな保存変更で数値を追試できるため。")
        lab.outcome(ids[1], "座標と面積をJSONに残し、手計算と一致することを確認した（合成2面の範囲）。")
        lab.decide(ids[2], "defer", "周辺面との交差・歪みの評価方法を先に整えるため。")
        lab.decide(ids[3], "reject", "最小合成例から実巻物の読字品質を主張する根拠がないため。")
        marker.write_text(json.dumps({"version": 1, "description": "教材用合成例"}, ensure_ascii=False), encoding="utf-8")
    finally:
        lab.close()
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEMO_ROOT)
    args = parser.parse_args()
    try:
        print(seed_demo(args.root))
    except (ValueError, OSError) as exc:
        parser.exit(2, f"デモを作成できません: {exc}\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
