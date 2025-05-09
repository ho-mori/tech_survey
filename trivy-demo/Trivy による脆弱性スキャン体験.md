# Trivy による脆弱性スキャン体験

## 調査日

2025年5月9日（金）

## 調査目的

DevSecOps の第一歩として、脆弱性スキャナ「Trivy」を使用し、ソースコードに対する自動スキャンの実用性を確認する。

## 実施環境

- OS：Windows 11
- ターミナル：PowerShell（管理者モード）
- 使用ツール：Trivy v0.62（Chocolatey経由でインストール）

## 使用手順

1. 作業ディレクトリを作成  
   `D:\tech_survey\trivy-demo`

2. Chocolatey にて Trivy をインストール  
   ```powershell
   choco install trivy -y
   ```

3. サンプルアプリ（脆弱性を含む）をクローン

   ```powershell
   git clone https://github.com/juice-shop/juice-shop.git juice-shop-app
   cd juice-shop-app
   ```

4. Trivy によるスキャン実行

   ```bash
   trivy fs .
   ```

## 結果

### スキャン出力サマリ

| ファイルパス                                                           | 検出種別   | 重大度    | 内容                  |
| ---------------------------------------------------------------- | ------ | ------ | ------------------- |
| `frontend/src/app/app.guard.spec.ts`                             | Secret | MEDIUM | JWT トークンが埋め込まれていた   |
| `frontend/src/app/last-login-ip/last-login-ip.component.spec.ts` | Secret | MEDIUM | JWT トークンが埋め込まれていた   |
| `lib/insecurity.ts`                                              | Secret | HIGH   | RSA 非対称秘密鍵が埋め込まれていた |

### 分析ポイント

* `jwt-token` の埋め込みはセッションの乗っ取りに繋がる恐れあり
* `RSA private key` の漏洩は致命的なセキュリティリスクとなる
* Trivy はスキャン時に自動で DB を更新し、CLI 1行で機密情報の検出が可能だった

## 考察と結論

* Trivy は CLI 単体でソースコード内の秘密情報や脆弱性を効率的に検出できた
* DevSecOps における初期スクリーニングツールとして実用性が高い
* 今後は CI/CD パイプラインへの統合や、Docker イメージ・IaC ファイル（Terraform/YAML）へのスキャン拡張を検討できる

## 補足

結果の JSON 出力などは以下の形式で可能：

```bash
trivy fs . --format json --output trivy-result.json
```