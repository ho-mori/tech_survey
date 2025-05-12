# Trivy によるセキュリティスキャン調査報告

## 調査日

2025年5月12日（月）

## 調査目的

ソースコードおよび Docker イメージに対して Trivy を使用し、脆弱性の有無を確認することで、開発対象プロジェクトのセキュリティ状況を把握する。

## 使用ツール

* OS: Windows 11
* スキャンツール: Trivy v0.62（Chocolatey経由でインストール）
* Docker Desktop: 起動済み

## 対象プロジェクト構成

```text
D:\tech_survey\trivy-demo\
├── index.js
├── package.json
├── Dockerfile
```

---

## 実施内容

### 1. ソースコードスキャン（File Systemスキャン）

```powershell
trivy fs . > trivy_fs_report.txt
```

* 結果ファイル: `trivy_fs_report.txt`
* 結果概要:

  * JavaScriptプロジェクトとして重大なセキュリティ問題は特に検出されなかった（パッケージ依存の少ない構成）

---

### 2. Docker イメージスキャン

#### ビルド対象

```powershell
docker build -t myapp:latest .
```

#### スキャンコマンド

```powershell
trivy image myapp:latest > trivy_image_myapp.txt
```

また、ベースラインとして `nginx:latest` もスキャン：

```powershell
trivy image nginx:latest > trivy_image_report.txt
```

---

## スキャン結果サマリ

### myapp\:latest（Node.jsベースの独自イメージ）

* 脆弱性数: 少数（内容は軽微）
* 対応: パッケージ更新と最小構成維持により回避可能

### nginx\:latest（Debian 12.10ベース）

| 項目       | 値    |
| -------- | ---- |
| 総脆弱性数    | 154件 |
| CRITICAL | 2件   |
| HIGH     | 14件  |
| MEDIUM   | 39件  |
| LOW      | 99件  |

#### 主な脆弱性例（CRITICAL）

| ライブラリ         | CVE-ID        | 概要                        |
| ------------- | ------------- | ------------------------- |
| libaom3       | CVE-2023-6879 | フレームサイズ変更時のヒープバッファオーバーフロー |
| libldap-2.5-0 | CVE-2023-2953 | NULLポインタ参照によるDoSの危険性      |

---

## 考察と対策案

* `nginx:latest` は多くの汎用ライブラリを含むため、脆弱性数が多い。
* 軽量な `nginx:alpine` ベースを使用することで、脆弱性を大幅に削減可能。
* 不要なシステムライブラリを含めない構成を意識することでセキュリティリスクを軽減できる。
* Trivyのスキャンオプションで `--ignore-unfixed` などを使い、実際の修正可能な脆弱性に注目する運用も検討。

---

## 結論

Trivyを用いたセキュリティスキャンにより、ベースイメージの選定や依存関係の見直しがセキュリティ品質の向上に直結することが確認された。今後はCIパイプラインへの統合や、継続的な自動スキャンによる運用監視が推奨される。