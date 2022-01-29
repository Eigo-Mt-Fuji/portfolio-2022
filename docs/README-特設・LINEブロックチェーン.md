
## 概要

* LINEブロックチェーンを使ってみる


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

https://github.com/Eigo-Mt-Fuji/eigo-nft
