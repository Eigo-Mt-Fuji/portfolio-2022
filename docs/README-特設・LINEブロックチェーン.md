
## 概要

* LINEブロックチェーンを使ってみる

https://docs-blockchain.line.biz/ja/service-tutorial/

```
サービス	取得	GET /v1/services/{serviceId}	CD	
サービス	変更	X	CD	
    サービストークン	一覧の取得	GET /v1/service-tokens/	CD	
    サービストークン	取得	GET /v1/service-tokens/{contractId}	CD	
    サービストークン	変更	PUT /v1/service-tokens/{contractId}	CD	
    サービストークン	作成	X	CD	
    サービストークン	鋳造	POST /v1/service-tokens/{contractId}/mint	CD	
    サービストークン	焼却	POST /v1/service-tokens/{contractId}/burn-from	CD	
    サービストークン	保有者の取得	GET /v1/service-tokens/{contractId}/holders	CD	Restricted 
    アイテムトークン	Contractの取得	GET /v1/item-tokens/{contractId}	CD	
    アイテムトークン	すべてのfungibleトークンの一覧	GET /v1/item-tokens/{contractId}/fungibles	CD	
    アイテムトークン	Fungibleトークの取得	GET /v1/item-tokens/{contractId}/fungibles/{tokenType}	CD	
    アイテムトークン	Fungibleトークンの保有者を取得	GET /v1/item-tokens/{contractId}/fungibles/{tokenType}/holders	CD	Restricted 
    アイテムトークン	すべてのnon Fungibleトークンの一覧	GET /v1/item-tokens/{contractId}/non-fungibles	CD	
    アイテムトークン	Non fungible token typeの取得	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}	CD	
    アイテムトークン	Non Fungibleトークンの取得	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}/{tokenIndex}	CD	
    アイテムトークン	Non fungibleの特定Token Typeを保有するユーザー一覧	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}/holders	CD	Restricted 
    アイテムトークン	特定のnon Fungibleトークンを保有するユーザーを取得	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}/{tokenIndex}/holder	CD	
    アイテムトークン	子トークンをすべて取得	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}/{tokenIndex}/children	CD	
    アイテムトークン	親トークンの取得	GET /v1/item-tokens/{contractId}/non-fungibles/{tokenType}/{tokenIndex}/parent	CD	
```

## 理解度UP

- サービストークン
  - サービストークンは、LINE Blockchainで取り引きの媒体として使用されます。
  - サービストークンはERC-20と似ているので、利用するのは簡単とのこと。

- アイテムトークン https://docs-blockchain.line.biz/ja/service-tutorial/Step2
  - アイテムトークンとは、サービスで使用する財貨やアイテムのこと
    - サービストークンとは違ってすべて同じContract IDを持ち
    - Token IDで区別します
  - アイテムトークンは、fungiblesとnon-fungiblesに分けることができ、性質に応じて適切なタイプを選択する必要があります
    - Fungibleアイテムトークン
      - 同じToken IDでトークンの価値や性格も同じ
    - Non-fungibleアイテムトークン
      - それぞれのトークンが固有のToken IDを持っているため、トークンの価値や性格も異なります  

- LINE BITMAX Wallet
  - ユーザーは、LINE BITMAX Walletに登録する必要がある
    - これはサービス登録とは別に行われます。
      - サービスへの登録手続きにLINE BITMAX Walletへの登録を含めることもできます。
    - LINE BITMAX Walletに登録した後
      - ユーザーは自分のLINE IDに1対1で紐付けられるウォレットを取得
      - 保有するトークンの取得や転送ができるようになります
    -  ユーザーウォレットからサービスにトークンを転送する方法
      - https://docs-blockchain.line.biz/ja/service-tutorial/Step5
        - ユーザーはLINE BITMAX WalletにあるTest Coin (TC)でLINKシネマの映画鑑賞券を購入
          - Test Coinで映画鑑賞券を購入するということは
            - ユーザーウォレットにあるTest Coin
            - と
            - サービスのサービスウォレットにあるMovieTicketアイテムトークン
        - 購入額の一部を会員ポイントとして与える
          - サービストークンのMovieToken (MOV)を会員ポイントとして使用
            - 映画鑑賞券を購入した観客のウォレットに、200 MOVを転送
              - https://docs-blockchain.line.biz/ja/api-guide/category-service-wallets/transfer#v1-wallets-walletAddress-service-tokens-contractId-transfer-post

## 実際にやってみる

https://github.com/Eigo-Mt-Fuji/eigo-nft
