# 技術調査レポート：GitHub Copilot による自動テストコード生成

## 調査日

2025 年 5 月 7 日（水）

## 調査目的

GitHub Copilot を活用してユニットテストコードを自動生成し、その実用性・補完精度・開発効率への影響を検証する。

## 調査対象

- 関数：`sum(a: number, b: number): number`（2 つの数値の加算）
- テスト環境：TypeScript + Jest

## 実施環境

- OS：Windows 11
- エディタ：Visual Studio Code（最新版）
- Node.js：v20.x
- GitHub Copilot 拡張：有効化済み（個人アカウント）

## 実施手順

1. フォルダ作成とプロジェクト初期化  
   `copilot-test-sample/` フォルダを作成し、`npm init -y` で初期化。

2. 開発環境構築

   - `typescript`, `jest`, `ts-jest`, `@types/jest` を導入
   - `tsconfig.json` と `jest.config.js` を設定

3. サンプル関数 `sum.ts` を作成

   ```ts
   export function sum(a: number, b: number): number {
     return a + b;
   }
   ```

4. テストファイル `__tests__/sum.test.ts` にて以下コメントを記述

   ```ts
   // write a test for sum
   ```

5. GitHub Copilot が以下のようなテストコードを自動生成

   ```ts
   describe("sum", () => {
     it("should return the sum of two numbers", () => {
       expect(sum(1, 2)).toBe(3);
       expect(sum(-1, -1)).toBe(-2);
       expect(sum(0, 0)).toBe(0);
       expect(sum(1.5, 2.5)).toBe(4);
     });
   });
   ```

6. `npx jest` を実行し、テストはすべて成功

   ```
   PASS  __tests__/sum.test.ts
     sum
       √ should return the sum of two numbers (2 ms)
   ```

## 成果と考察

### 良かった点

- コメントを記述するだけで即座に実用的なテストが生成された
- 正常系・負数・小数など複数パターンが含まれていた
- テスト構文（Jest 形式）を自動で認識

### 改善点・注意点

- テストケースが 1 つの `it(...)` に集約されていたため、個別の失敗が特定しにくい
- 異常系（例：null, undefined, 型不一致など）は自動では生成されなかった
- 自動生成された内容の正当性は、開発者がレビューする必要がある

## 今後の展望

- Copilot Chat を活用して異常系テストやコメント付きコードの自動生成を試す
- 自社業務コードに対するカバレッジ拡大への適用を検討
- チームでのテスト設計補助ツールとして導入可否を議論する

## フォルダ構成（調査終了時点）

```
copilot-test-sample/
├── __tests__/
│   └── sum.test.ts
├── src/
│   └── sum.ts
├── jest.config.js
├── package.json
└── tsconfig.json
```

## 結論

GitHub Copilot はユニットテスト作成の「初期生成」において非常に有効であり、特に正常系テストに関しては即戦力となる補完精度を示した。ただし、すべてを任せるのではなく、生成結果のレビューと拡張が前提となる。
