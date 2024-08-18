# PyJsonX

[Switch to English: 英語](https://github.com/nnnnnnn0090/PyJsonX/blob/main/README.md)

### 概要

`PyJsonX` は、PHP のテンプレート内にコードを埋め込む機能に触発された Python ライブラリです。これにより、JSON ファイル内に Python コードを埋め込むことができ、動的でプログラム可能な JSON コンテンツの生成が容易になります。このライブラリは、PHP が HTML 内にコードを埋め込むのと同様に、Python を使って直接柔軟な JSON 構造を作成する方法を提供します。

### インストール

`PyJsonX` は pip を使ってインストールできます：

```bash
pip3 install PyJsonX
pip3 install git+https://github.com/nnnnnnn0090/PyJsonX
```

### 拡張子

- `PyJsonX` では `.pyjsonX` 拡張子を使用します。[example.pyjsonX](https://github.com/nnnnnnn0090/PyJsonX/blob/main/PyJsonX/example.pyjsonX)  
  VSCode には `.pyjsonX` ファイル用の拡張機能があります。[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=nnnnnnn0090.pyjsonX)

### 使用方法

#### JSON 内に Python コードを埋め込む

JSON 内に Python コードを埋め込むには、`<?py ... ?>` タグを使用します。以下に例を示します：
<img width="660" alt="スクリーンショット 2024-08-18 19 32 56" src="https://github.com/user-attachments/assets/0af18fc9-6aa5-4c01-b3aa-072660347d17">

↓
```json
{
    "static_field": "value",
    "unixtime": 1723977194,
    "dynamic_0": "0",
    "dynamic_1": "2",
    "dynamic_2": "4",
    "dynamic_3": "6",
    "dynamic_4": "8",
    "another_static_field": "another_value"
}
```

#### 埋め込まれた Python コードの実行

1. **JSON 文字列からの実行:**

    ```python
    import PyJsonX

    json_str = '''
    {
        "static_field": "value",
        <?py
            result = ""
            # 0 から 4 までの値を持つ動的フィールドを生成
            for i in range(5):
                result += f'"dynamic_{i}": "{i * 2}", \n'
            return result
        ?>
        "another_static_field": "another_value"
    }
    '''

    # JSON 文字列を処理し、埋め込まれた Python コードを実行
    processed_str = PyJsonX.execute(json_str)
    print(processed_str)  # 処理された JSON を出力
    ```

2. **JSON ファイルからの実行:**

    ```python
    import PyJsonX

    input_json_path = 'input.json'  # 入力 JSON ファイルのパス
    output_json_path = 'output.json'  # 出力 JSON ファイルのパス

    # JSON ファイルを処理し、埋め込まれた Python コードを実行
    PyJsonX.execute_file(input_json_path, output_json_path)
    ```

### 特徴

- **動的コンテンツ生成:** JSON 内に Python コードを埋め込んで、動的なコンテンツを生成できます。
- **柔軟なデータ作成:** プログラムロジックに基づいて複雑な JSON 構造を動的に生成します。
- **PHP に触発された:** PHP のテンプレート機能に触発され、JSON 内にコードを埋め込むのと同様の機能を提供します。

### ドキュメント

より詳細な情報は [PyJsonX ドキュメント](https://github.com/nnnnnnn0090/PyJsonX) をご覧ください。（準備中）

### コントリビューション

貢献を歓迎します！プルリクエストを送るか、[GitHub リポジトリ](https://github.com/nnnnnnn0090/PyJsonX) に問題を報告してください。

### ライセンス

`PyJsonX` は MIT ライセンスの下でライセンスされています。詳細については [LICENSE](https://github.com/nnnnnnn0090/PyJsonX/blob/main/LICENSE) を参照してください。

---
