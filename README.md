# Database config check tool


## Overview
> 設計と実際に設定されている値が同じかどうかをチェックする。違う場合はlogへ出力する。

## 想定使用場面
定期実行, 構築後

## ロジック
> テキストで格納してある設定書を読み込み、同じ設定になっているか実際にアクセスして確認する。  
> ACS Manager, KVM Agentはデータベースから接続先を取得する。
> ACSの

## 比較対象
> 比べる内容は以下。

1. Global Config(DB)
2. ACS Manager
  - JavaのHeapサイズ
3. KVM Agent
  - Agentコンフィグに記載されているパラメータ全て
  - JaveHeapのサイズ

## オプション
TBD
